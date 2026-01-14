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


# class IceCreamStand(Restaurant):
#     def __init__(self, restaurant_name, cuisine_type, flavours, number_served=0):
#         super().__init__(restaurant_name, cuisine_type, number_served)
#         self.flavours = flavours

#     def display_flavours(self):
#         """Display flavours on the Ice cream stand"""
#         for flavour in self.flavours:
#             print(flavour)


# available_flavours = ["mango", "kulfa", "pista", "chocolate", "strawberry"]
# ice_cream_stand = IceCreamStand("AB Desserts", "International", available_flavours, 40)
# ice_cream_stand.display_flavours()


# class Users:
#     def __init__(self, first_name, last_name, user_name, email, login_attempts):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.user_name = user_name
#         self.email = email
#         self.login_attempts = login_attempts

#     def describe_user(self):
#         print("\n--- Summary of user ---")
#         print(f"First name: {self.first_name}")
#         print(f"Last name: {self.last_name}")
#         print(f"Username: {self.user_name}")
#         print(f"Email: {self.email}")

#     def greet_user(self):
#         print(f"Welcome, {self.first_name.title()} {self.last_name.title()}!")

#     def increment_login_attempts(self):
#         self.login_attempts += 1

#     def reset_login_attempts(self):
#         self.login_attempts = 0


# class Admin(Users):
#     def __init__(self, first_name, last_name, user_name, email, login_attempts):
#         super().__init__(first_name, last_name, user_name, email, login_attempts)
#         self.privileges = Privileges(admin_privileges)


# class Privileges:
#     def __init__(self, privileges):
#         self.privileges = privileges

#     def show_privileges(self):
#         for privilege in self.privileges:
#             print(privilege)


# admin_privileges = ["can add post", "can delete post", "can ban user"]

# # admin1 = Admin("Abdul", "Basit", "admin", "admin@xyz.co", 1, admin_privileges)
# # admin1.show_privileges(admin_privileges)

# admin2 = Admin("John", "Doe", "admin", "admin@abc.co", 1)
# admin2.privileges.show_privileges()


class Car:
    """A simple attempt to represent a car"""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to given value.
        Reject the change if it attempts to roll the odometer back.
        """

        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can not roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

    def fill_gas_tank(self):
        """Simulation to fill the car's gas tank"""
        print("The gas tank is full!")


class Battery:
    def __init__(self, battery_size=40):
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size"""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides"""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

        print(f"This car can go about {range} miles on a full charge")

    def upgrade_battery(self):
        if self.battery_size != 65:
            self.battery_size = 65


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles"""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        """Electric vehicles do not have gas tanks."""
        print("This car does not have a gas tank!")


leaf = ElectricCar("nissan", "leaf", 2024)
leaf.battery.get_range()
leaf.battery.upgrade_battery()
leaf.battery.get_range()
