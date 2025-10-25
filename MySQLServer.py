#!/usr/bin/env python3
"""
Task 1: Create a MySQL database named 'alx_book_store'
Handles exceptions and closes connection properly
No SELECT or SHOW statements used
"""

import mysql.connector
from mysql.connector import Error

def create_database():
    connection = None
    cursor = None

    try:
        # Establish connection to MySQL server
        connection = mysql.connector.connect(
            host="localhost",        # change if needed
            user="root",             # your MySQL username
            password="yourpassword"  # replace with your MySQL password
        )

        # Check if connection is established
        if connection.is_connected():
            cursor = connection.cursor()
            # Create the database if it does not exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        # Handle connection or query errors
        print(f"Error while connecting to MySQL: {e}")

    finally:
        # Ensure all resources are properly closed
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()
