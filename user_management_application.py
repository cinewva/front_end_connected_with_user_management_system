from user_management import UserManagementSystem

def main():
    user_management_system = UserManagementSystem()

    while True:
        print("\nUser Management System")
        print("1. Display user by ID")
        print("2. Display all users")
        print("3. Add user")
        print("4. Remove user")
        print("5. Update first name")
        print("6. Update email")
        print("7. Add many users for testing")
        print("8. Remove all users")
        print("9. Exit")
        choice = input("Enter your choice: ")

        try:
            if choice == '1':
                id = int(input("Enter user ID: "))
                user = user_management_system.display_user_by_id(id)
                if user:
                    print(user)
            elif choice == '2':
                user_management_system.display_all_users()
            elif choice == '3':
                id = int(input("Enter user ID: "))
                first_name = input("Enter first name: ")
                last_name = input("Enter last name: ")
                email = input("Enter email: ")
                age = int(input("Enter age: "))
                user_management_system.add_user(id, first_name, last_name, email, age)
            elif choice == '4':
                id = int(input("Enter user ID: "))
                user_management_system.remove_user(id)
            elif choice == '5':
                id = int(input("Enter user ID: "))
                new_first_name = input("Enter new first name: ")
                user_management_system.update_first_name(id, new_first_name)
            elif choice == '6':
                id = int(input("Enter user ID: "))
                new_email = input("Enter new email: ")
                user_management_system.update_email(id, new_email)
            elif choice == '7':
                test_users = [
                    (1, "test1", "user1", "user1@test.com", 1),
                    (2, "test2", "user2", "user2@test.com", 2),
                ]
                for user in test_users:
                    user_management_system.add_user(*user)
            elif choice == '8':
                user_management_system.delete_all_users()
            elif choice == '9':
                print("Exiting application...")
                user_management_system.close_connection()
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter the correct data type.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
