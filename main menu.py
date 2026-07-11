from database import load_users
from users import login, register


users = load_users()


while True:
    print("\n<<<< MENU >>>>")
    print("1. Login")
    print("2. Register")
    print("3. Exit")

    choice = input("Choose option > ")

    if choice == "1":
        login(users)

    elif choice == "2":
        register(users)

    elif choice == "3":
        print("Goodbye")
        break

    else:
        print("Invalid choice")