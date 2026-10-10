import mysql.connector as myconn

def  connect():
    return myconn.connect(
        host="localhost",
        user="root",
        password="Samiksha@123",
        database="bank_system"
    )