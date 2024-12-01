from database import connect_to_database
from user import User
from for_testing import ForTesting

class UserManagementSystem(ForTesting):
    def __init__(self):
        self.connection = connect_to_database()
        self.cursor = self.connection.cursor()

    def add_user(self, id, first_name, last_name, email, age):
        query = "INSERT INTO users (id, first_name, last_name, email, age) VALUES (%s, %s, %s, %s, %s)"
        values = (id, first_name, last_name, email, age)
        self.cursor.execute(query, values)
        self.connection.commit()
        print(f"User added: {first_name} {last_name}")

    def remove_user(self, id):
        query = "DELETE FROM users WHERE id = %s"
        self.cursor.execute(query, (id,))
        self.connection.commit()
        print(f"User with ID {id} removed")

    def update_first_name(self, id, new_first_name):
        query = "UPDATE users SET first_name = %s WHERE id = %s"
        self.cursor.execute(query, (new_first_name, id))
        self.connection.commit()
        print(f"First name updated for user with ID {id}")

    def update_email(self, id, new_email):
        query = "UPDATE users SET email = %s WHERE id = %s"
        self.cursor.execute(query, (new_email, id))
        self.connection.commit()
        print(f"Email updated for user with ID {id}")

    def display_user_by_id(self, id):
        query = "SELECT * FROM users WHERE id = %s"
        self.cursor.execute(query, (id,))
        user_data = self.cursor.fetchone()
        if user_data:
            return User(*user_data)
        else:
            print(f"No user found with ID {id}")
            return None

    def display_all_users(self):
        query = "SELECT * FROM users"
        self.cursor.execute(query)
        users = [User(*user_data) for user_data in self.cursor.fetchall()]
        for user in users:
            print(user)
        return users

    def add_users(self, id, first_name, last_name, email, age):
        self.add_user(id, first_name, last_name, email, age)

    def delete_all_users(self):
        query = "DELETE FROM users"
        self.cursor.execute(query)
        self.connection.commit()
        print("All users deleted")

    def close_connection(self):
        if self.connection.is_connected():
            self.cursor.close()
            self.connection.close()
            print("Database connection closed.")