from db_config import connect

def create_account():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    balance = float(input("Enter initial balance: "))
    db = connect()
    cursor = db.cursor()
    sql = "INSERT INTO accounts (name, email, balance) VALUES (%s, %s, %s)"
    values = (name, email, balance)
    cursor.execute(sql, values)
    db.commit()
    print("Account created successfully!")
    db.close()


def view_account():
    db = connect()
    cursor = db.cursor()
    cursor.execute("SELECT FROM accounts")
    accounts = cursor.fetchall()
    print("ALL Accounts")
    for account in accounts:
        print(f"Account ID: {account[0]}, Name: {account[1]}, Email: {account[2]}, Balance: {account[3]}")
    db.close()

def deposit_money():
    account_id = input("Enter your account ID: ")
    amount = float(input("Enter the amount to deposit: "))
    db = connect()
    cursor = db.cursor()
    cursor.execute("UPDATE accounts SET balance = balance + %s WHERE account_id = %s", (amount, account_id))
    db.commit()
    print("Deposit successful!")
    db.close()


def withdraw_money():
    account_id = input("Enter your account ID: ")
    amount = float(input("Enter the amount to withdraw: "))
    db = connect()
    cursor = db.cursor()
    cursor.execute("SELECT balance FROM accounts WHERE account_id = %s", (account_id,))
    result = cursor.fetchone()
    if result:
        current_balance = result[0]
        if current_balance >= amount:
            cursor.execute("UPDATE accounts SET balance = balance - %s WHERE account_id = %s", (amount, account_id))
            db.commit()
            print("Withdrawal successful!")
        else:
            print("Insufficient funds!")
    else:
            print("Account not found!")     
    db.close()


def check_balance():
    account_id = input("Enter your account ID: ")
    db = connect()
    cursor = db.cursor()
    cursor.execute("SELECT name,balance FROM accounts WHERE account_id = %s", (account_id,))
    result = cursor.fetchone()
    if result:
        print(f"Account Holder: {result[0]}, Current Balance: {result[1]}")
    else:
        print("Account not found!")
    db.close()