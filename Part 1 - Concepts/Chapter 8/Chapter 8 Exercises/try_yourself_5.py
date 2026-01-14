# def build_sandwich(*items):
#     print("\nMaking a sandwich with the following items:")
#     for item in items:
#         print(f"- {item}")


# build_sandwich("egg")
# build_sandwich("egg", "butter")
# build_sandwich("egg", "jam", "cheese")


# def build_profile(first, last, **user_info):
#     """Build a dictionary containing everything we know about the user"""
#     user_info["first_name"] = first
#     user_info["last_name"] = last
#     return user_info


# user_profile = build_profile(
#     "abdul", "basit", location="sohawa", field="data science", age=20
# )

# print(user_profile)


def make_car(manufacturer, model_name, **specs):
    specs["manufacturer"] = manufacturer
    specs["model_name"] = model_name

    print(specs)


make_car("subaru", "outback", color="blue", tow_package=True)
