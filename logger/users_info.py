from logger import logger
import json
import os

USER_FILE = "logger/users.json"

def load_users():

    if not os.path.exists(USER_FILE):
        return []
    with open(USER_FILE, "r") as f:
        return json.load(f)
    


def save_users(users):
    try:
        with open(USER_FILE, "w") as f:
            json.dump(users, f, indent=4)
        logger.info("Users saved successfully.")
    except Exception:
        logger.exception("Failed to save users to file.")


def add_user(name, email):
    users = load_users()
    users.append({"name": name, "email": email})
    save_users(users)
    logger.info(f"Added user: {name}, {email}")

def list_users():
    users = load_users()
    logger.info(f"Listing {len(users)} user(s).")
    for user in users:
        print(f"{user['name']} - {user['email']}")

def delete_user(email):
    users = load_users()
    new_users = [u for u in users if u["email"] != email]
    if len(new_users) == len(users):
        logger.warning(f"User with email {email} not found.")
    else:
        save_users(new_users)
        logger.info(f"Deleted user with email: {email}")
