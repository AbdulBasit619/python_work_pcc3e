def describe_pet(pet_name, animal_type="dog"):
    """Display information about a pet"""
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}")


describe_pet("Cat", "Harry")
describe_pet("Dog", "Willie")

describe_pet(animal_type="Cat", pet_name="Harry")
describe_pet(pet_name="Harry", animal_type="Cat")
describe_pet(animal_type="Dog", pet_name="Willie")
describe_pet(pet_name="Willie")
