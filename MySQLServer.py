import mysql.connector
from mysql.connector import Error

try:
    # Connect to MySQL Server (adjust user and password as needed)
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Nicholas2joshua$'  # Replace with your MySQL root password
    )

    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        # Optional: print("MySQL connection closed.")
