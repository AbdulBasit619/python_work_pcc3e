# class Restaurant:
#     def __init__(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type

#     def describe_restaurant(self):
#         print(f"Restaurant name: {self.restaurant_name}")
#         print(f"Cuisine type: {self.cuisine_type}")

#     def open_restaurant(self):
#         print("The restaurant is open!")


# restaurant1 = Restaurant("AB Restaurant", "Pakistani")
# # print(restaurant.restaurant_name)
# # print(restaurant.cuisine_type)

# # restaurant.describe_restaurant()
# # restaurant.open_restaurant()

# restaurant2 = Restaurant("LM Lodges", "Chinese")
# restaurant3 = Restaurant("XY Group of Hotels", "Italian")

# restaurant1.describe_restaurant()
# restaurant2.describe_restaurant()
# restaurant3.describe_restaurant()


class Users:

    def __init__(self, first_name, last_name, user_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.email = email

    def describe_user(self):
        print("\n--- Summary of user ---")
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Username: {self.user_name}")
        print(f"Email: {self.email}")

    def greet_user(self):
        print(f"Welcome, {self.first_name.title()} {self.last_name.title()}!")


user_a = Users("alice", "smith", "al1ce_sm1th", "alicesmith@mail.com")
user_b = Users("john", "doe", "doejohn147", "doe.john@mail.com")

user_a.describe_user()
user_a.greet_user()

user_b.describe_user()
user_b.greet_user()
