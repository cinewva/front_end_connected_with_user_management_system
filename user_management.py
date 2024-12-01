from database import connect_to_database
from user import User
from for_testing import ForTesting

class UserManagementSystem(ForTesting):
    def __init__(self):
        try:
            self.connection = connect_to_database()
            self.cursor = self.connection.cursor()
        except Exception as e:
            print(f"Error connecting to database: {e}")

    def add_user(self, id, first_name, last_name, email, age):
        try:
            query = "INSERT INTO users (id, first_name, last_name, email, age) VALUES (%s, %s, %s, %s, %s)"
            values = (id, first_name, last_name, email, age)
            self.cursor.execute(query, values)
            self.connection.commit()
            print(f"User added: {first_name} {last_name}")
        except Exception as e:
            print(f"Error adding user: {e}")

    def remove_user(self, id):
        try:
            query = "DELETE FROM users WHERE id = %s"
            self.cursor.execute(query, (id,))
            self.connection.commit()
            print(f"User with ID {id} removed")
        except Exception as e:
            print(f"Error removing user: {e}")

    def update_first_name(self, id, new_first_name):
        try:
            query = "UPDATE users SET first_name = %s WHERE id = %s"
            self.cursor.execute(query, (new_first_name, id))
            self.connection.commit()
            print(f"First name updated for user with ID {id}")
        except Exception as e:
            print(f"Error updating first name: {e}")

    def update_email(self, id, new_email):
        try:
            query = "UPDATE users SET email = %s WHERE id = %s"
            self.cursor.execute(query, (new_email, id))
            self.connection.commit()
            print(f"Email updated for user with ID {id}")
        except Exception as e:
            print(f"Error updating email: {e}")

    def display_user_by_id(self, id):
        try:
            query = "SELECT * FROM users WHERE id = %s"
            self.cursor.execute(query, (id,))
            user_data = self.cursor.fetchone()
            if user_data:
                return User(*user_data)
            else:
                print(f"No user found with ID {id}")
                return None
        except Exception as e:
            print(f"Error displaying user by ID: {e}")
            return None

    def display_all_users(self):
        try:
            query = "SELECT * FROM users"
            self.cursor.execute(query)
            users = [User(*user_data) for user_data in self.cursor.fetchall()]
            for user in users:
                print(user)
            return users
        except Exception as e:
            print(f"Error displaying all users: {e}")
            return []

    def delete_all_users(self):
        try:
            query = "DELETE FROM users"
            self.cursor.execute(query)
            self.connection.commit()
            print("All users deleted")
        except Exception as e:
            print(f"Error deleting all users: {e}")

    def close_connection(self):
        if self.connection.is_connected():
            self.cursor.close()
            self.connection.close()
            print("Database connection closed.")
