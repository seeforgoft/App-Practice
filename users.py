from database import save_users


def login(users):
    username = input("Enter username > ")
    password = input("Enter password > ")

    if username in users and users[username] == password:
        print("Login Successful")
    else:
        print("Login Invalid")


def register(users):
    username = input("Create username > ")

    if username in users:
        print("Username already exists")

    else:
        password = input("Create password > ")
        users[username] = password
        save_users(users)
        print("Account Created")