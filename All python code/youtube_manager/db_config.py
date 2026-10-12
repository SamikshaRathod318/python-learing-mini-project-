import mysql.connector

def connect():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Samiksha@123",
        database="youtube_manager"
    )
    return connection
