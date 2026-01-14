### Without functions
# # Start with some designs that need to be printed
# unprinted_designs = ["phone case", "robot pendant", "dodecahedron"]
# completed_models = []

# # Simulate printing each design, until none are left
# # Move each design to completed_models after printing

# while unprinted_designs:
#     unprinted_design = unprinted_designs.pop()
#     print(f"Printing design: {unprinted_design.title()}")

#     completed_models.append(unprinted_design)

# # Display all completed models.
# print("\nThe following models have been printed:")
# for model in completed_models:
#     print(model.title())


### With functions
def print_models(unprinted_designs, printed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        unprinted_design = unprinted_designs.pop()
        print(f"Printing design: {unprinted_design.title()}")
        printed_models.append(unprinted_design)


def show_printed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for model in completed_models:
        print(model.title())


unprinted_designs = ["phone case", "robot pendant", "dodecahedron"]
completed_models = []

# Modifies original list
# print_models(unprinted_designs, completed_models)

# Does not modify original list
print_models(unprinted_designs[:], completed_models)


show_printed_models(completed_models)
