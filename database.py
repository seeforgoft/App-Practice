def load_users():
    users = {}

    try:
        with open("users.txt", "r") as file:
            for line in file:
                username, password = line.strip().split(",")
                users[username] = password

    except FileNotFoundError:
        with open("users.txt", "w"):
            pass

    return users


def save_users(users):
    with open("users.txt", "w") as file:
        for username in users:
            file.write(username + "," + users[username] + "\n")