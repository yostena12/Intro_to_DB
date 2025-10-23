#!/usr/bin/env python3
"""
A simple Python script to create a MySQL database called 'alx_book_store'
"""

import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server (adjust host, user, password if needed)
        connection = mysql.connector.connect(
            host='localhost',      # or '127.0.0.1'
            user='root',           # your MySQL username
            password='yourpassword'  # replace with your actual MySQL password
        )

        if connection.is_connected_
