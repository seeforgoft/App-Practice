from operator import add


def load_users():
    users = {}

    file = open("users.txt", "r")

    for line in file:
        username, password = line.strip().split(",")
        users[username] = password

    file.close()

    return users


users = load_users()

def save_users():
    file = open("users.txt", "w")

    for username in users:
        file.write(username + "," + users[username] + "\n")

    file.close()



def login():
    username = input("Enter username > ")
    password = input("Enter password > ")

    if username in users and users[username] == password:
        print("Login Successful")
    else:
        print("Login Invalid")


def register():
    username = input("Create username > ")

    if username in users:
        print("Username already exists")
    else:
        password = input("Create password > ")
        users[username] = password
        print("Account Created")
        users[username] = password
        save_users()


while True:
    print("\n<<<< MENU >>>>")
    print("1. Login")
    print("2. Register")
    print("3. Exit")

    choice = input("Choose option > ")

    if choice == "1":
        login()

    elif choice == "2":
        register()

    elif choice == "3":
        print("Goodbye")
        break

    else:
        print("Invalid choice")

