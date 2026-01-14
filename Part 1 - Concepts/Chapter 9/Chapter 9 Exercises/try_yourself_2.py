# class Restaurant:
#     def __init__(self, restaurant_name, cuisine_type, number_served=0):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#         self.number_served = number_served

#     def describe_restaurant(self):
#         print(f"Restaurant name: {self.restaurant_name}")
#         print(f"Cuisine type: {self.cuisine_type}")

#     def open_restaurant(self):
#         print("The restaurant is open!")

#     def set_number_served(self, num_served):
#         self.number_served = num_served

#     def increment_number_served(self, inc):
#         self.number_served += inc


# restaurant = Restaurant("AB Foods", "Pakistani", 56987)
# restaurant.set_number_served(42168)
# restaurant.increment_number_served(60)


# print(restaurant.number_served)


class Users:

    def __init__(self, first_name, last_name, user_name, email, login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.email = email
        self.login_attempts = login_attempts

    def describe_user(self):
        print("\n--- Summary of user ---")
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Username: {self.user_name}")
        print(f"Email: {self.email}")

    def greet_user(self):
        print(f"Welcome, {self.first_name.title()} {self.last_name.title()}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


user_a = Users("abdul", "basit", "abdul_basit", "@bdul_bas!t", 5)
user_a.increment_login_attempts()
user_a.increment_login_attempts()
user_a.increment_login_attempts()
user_a.increment_login_attempts()
user_a.increment_login_attempts()

print(user_a.login_attempts)

user_a.reset_login_attempts()

print(user_a.login_attempts)
