from users_info import add_user, list_users, delete_user

add_user("Mamun", "mamun@email.com")
add_user("Test", "test@email.com")

list_users()

delete_user("test@email.com")

list_users()
