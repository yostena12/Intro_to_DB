import mysql.connector

try:
    # Connect to MySQL server (no database specified)
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password"
    )

    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store;")
    print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
