import sqlite3


class DatabaseHandler:
    def __init__(self, db_name='user_data.db'):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    address TEXT NOT NULL,
                    mobile TEXT NOT NULL,
                    email TEXT NOT NULL
                )
            ''')
        self.connection.commit()

    def user_exists(self, username, address):
        self.cursor.execute(
            'SELECT * FROM users WHERE username=? AND address=?', (username, address))
        return self.cursor.fetchone()

    def add_user(self, username, address, mobile, email):
        self.cursor.execute('''
                INSERT INTO users (username, address, mobile, email)
                VALUES (?, ?, ?, ?)
            ''', (username, address, mobile, email))
        self.connection.commit()

    def fetch_user_details(self, username, address):
        self.cursor.execute(
            'SELECT * FROM users WHERE username=? AND address=?', (username, address))
        return self.cursor.fetchone()

    def close_connection(self):
        self.connection.close()


class UserManagement:
    def __init__(self):
        self.db_handler = DatabaseHandler()
        self.populate_initial_data()

    def populate_initial_data(self):
        users = [
            ('Abhishek', 'PG-DAI', '1234567890', 'abhi@example.com'),
            ('Jay', 'PG-DAI', '2345678901', 'jay@example.com'),
            ('Dhanu', 'PG-DAI', '3456789012', 'Dhanu@example.com'),
            ('Samak', 'PG-DAI', '4567890123', 'chutiya@example.com'),
            ('Vivek', 'PG-DAI', '5678901234', 'vivek@example.com'),
            ('Gagan', 'PG-DAI', '6789012345', 'gagan@example.com'),
            ('Alisha', 'PG-DAI', '7890123456', 'ali@example.com'),
            ('Samiksha', 'PG-DBDA', '8901234567', 'samu@example.com'),
            ('Rucha', 'PG-DITIS', '9012345678', 'rucha@example.com'),
            ('Prachi', 'PG-VLSI', '0123456789', 'prachu@example.com')
        ]

        for user in users:
            self.db_handler.add_user(*user)

    def manage_user(self):
        username = input("Enter username: ")
        address = input("Enter address: ")

        user = self.db_handler.user_exists(username, address)

        if user:
            print("User details found:")
            print(
                f"Username: {user[1]}, Address: {user[2]}, Mobile: {user[3]}, Email: {user[4]}")
        else:
            mobile = input("Enter mobile number: ")
            email = input("Enter email ID: ")
            self.db_handler.add_user(username, address, mobile, email)
            print("User added successfully.")

    def close(self):
        self.db_handler.close_connection()


if __name__ == "__main__":
    user_management = UserManagement()
    user_management.manage_user()
