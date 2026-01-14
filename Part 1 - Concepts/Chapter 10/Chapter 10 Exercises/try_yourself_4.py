"""Program that prompts for user's favourite number."""

from pathlib import Path
import json

# path = Path("favourite_number.txt")


# try:
#     favourite_number = int(input("Tell me your favourite number: "))
# except ValueError:
#     print("Please enter a valid number!")
# else:
#     contents = json.dumps(favourite_number)
#     path.write_text(contents)


# try:
#     favourite_number = int(input("Tell me your favourite number: "))
# except ValueError:
#     print("Please enter a valid number!")
# else:
#     contents = json.dumps(favourite_number)
#     path.write_text(contents)

#     if path.exists():
#         contents = path.read_text()
#         favourite_number = json.loads(contents)
#         print(f"I know your favourite number! It's {favourite_number}")
#     else:
#         print(f"The file {path} does not exist!")


# def get_stored_user_info(path):
#     """Get stored user info if available"""
#     if path.exists():
#         contents = path.read_text()
#         user = json.loads(contents)
#         return user
#     else:
#         return None


# def get_new_user_info(path):
#     """Prompt for new username, email and login status."""
#     username = input("What is your name? ")
#     email = input("What is your email? ")
#     login_status = input("Are you currently logged in? ")

#     user = {"username": username, "email": email, "login_status": login_status}

#     contents = json.dumps(user)
#     path.write_text(contents)
#     return user


# def summarize_user():
#     """Summarize the user"""
#     path = Path("user_info.json")
#     user = get_stored_user_info(path)
#     if user:
#         print(
#             f"Welcome back, {user['username']}! We remember your email to be {user['email']}, and your login status is set to {user['login_status']}!"
#         )
#     else:
#         user = get_new_user_info(path)
#         print(
#             f"We'll remember you when you come back, {user['username']}! Your email is {user['email']}, and your login status after you come back will be {user['login_status']}!"
#         )


# summarize_user()


def get_stored_username(path):
    """Get stored username if available"""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None


def get_new_username(path):
    """Prompt for a new username."""
    username = input("What is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username


def greet_user():
    """Greet the user by name."""
    path = Path("username.json")
    username = get_stored_username(path)
    if username:
        status = input(f"Is this username, {username}, correct? (yes/no) ")
        if status == "no":
            username = get_new_username(path)
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username(path)
        print(f"We'll remember you when you come back, {username}!")


greet_user()
