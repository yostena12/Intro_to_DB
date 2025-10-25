#!/usr/bin/env python3
"""
Task 1: Create a MySQL database named 'alx_book_store'
Handles exceptions, no SELECT or SHOW statements used
"""

import mysql.connector
from mysql.connector import Error

def create_database():
    connection = None
    cursor = None

    try:
        # Try connecting to MySQL server
        connection = mysql.connector.connect(
            host="localhost",       # Change if needed
            user="root",            # Your MySQL username
            password="yourpassword" # Replace with your actual MySQL password
        )

        # Check connection
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        # Handles any connection or query error
        print(f"Error while connecting to MySQL: {e}")

    finally:
        # Ensures resources are closed properly
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()
