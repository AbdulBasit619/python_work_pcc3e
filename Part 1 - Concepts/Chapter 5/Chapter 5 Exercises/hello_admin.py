# usernames = ["admin", "bob", "john", "manta", "flora"]
# usernames = []
# if usernames:
#     for username in usernames:
#         if username == "admin":
#             print(f"Hello {username}, would you like to see a status report?")
#         else:
#             print(f"Hello {username}, thank you for logging again!")
# else:
#     print("We need to find some users!")

# current_users = ["jordan", "bob", "john", "manta", "flora"]
# new_users = ["valentina", "michael", "manta", "tom", "bob"]

# current_users_lower = [current_user.lower() for current_user in current_users]
# new_users_lower = [new_user.lower() for new_user in new_users]

# for new_user in new_users_lower:
#     if new_user in current_users_lower:
#         print("Username already exists. Please enter a new username!")
#     else:
#         print("Username is available")

numbers = [i for i in range(1, 10)]

for number in numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")
