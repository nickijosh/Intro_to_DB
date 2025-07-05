import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL Server (adjust user/password if needed)
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Nicholas2joshua$'  # Update this if your MySQL server uses a password
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Create database without using SHOW or SELECT
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

if __name__ == "__main__":
    create_database()
