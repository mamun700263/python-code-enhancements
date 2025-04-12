from logger import logger
import json
import os

USER_FILE = "logger/users.json"




def load_users():
    if not os.path.exists(USER_FILE):
        logger.warning(f"[load_users] File '{USER_FILE}' does not exist. Returning empty user list.")
        return []

    try:
        with open(USER_FILE, "r") as f:
            data = json.load(f)

        if not isinstance(data, list):
            logger.error("[load_users] Invalid data format in file. Expected list, got %s. Returning empty list.", type(data).__name__)
            return []

        logger.info("[load_users] Successfully loaded %d user(s).", len(data))
        return data

    except json.JSONDecodeError as e:
        logger.error("[load_users] JSON decode error: %s. Returning empty list.", str(e))
        return []

    except Exception as e:
        logger.critical("[load_users] Unexpected error: %s", str(e))
        return []


def save_users(users):
    try:
        with open(USER_FILE, "w") as f:
            json.dump(users, f, indent=4)
        logger.info("Users saved successfully.")
    except Exception:
        logger.exception("Failed to save users to file.")



def add_user(name, email):
    # Load existing users from the file
    users = load_users()

    # Validate input
    if not name or not email:
        logger.error("[add_user] Name and email are required.")
        return

    # Check if user already exists by email
    if any(u['email'] == email for u in users):
        logger.warning("[add_user] User with email '%s' already exists. Skipping addition.", email)
        return

    # Add new user to the list
    users.append({"name": name, "email": email})
    
    # Save updated user list to file
    save_users(users)

    # Log the successful addition
    logger.info("[add_user] Added user: %s (%s)", name, email)



def list_users():
    """
    Loads and prints all users from the file.
    Logs a warning if no users exist.
    """
    users = load_users()

    # Handle empty user list
    if not users:
        logger.warning("[list_users] No users found.")
        return

    # Log how many users are about to be printed
    logger.info("[list_users] Listing %d user(s).", len(users))

    # Print each user's details
    for idx, user in enumerate(users, start=1):
        try:
            print(f"{idx}. {user['name']} - {user['email']}")
        except KeyError as e:
            logger.error("[list_users] Missing key: %s in user data: %s", e, user)



def delete_user(email):
    users = load_users()
    if not users:
        logger.warning("[delete_user] No users found to delete.")
        return
    
    new_users = [u for u in users if u["email"] != email]
    if len(new_users) == len(users):
        logger.warning(f"User with email {email} not found.")
    else:
        save_users(new_users)
        logger.info(f"Deleted user with email: {email}")
