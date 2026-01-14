import printing_functions


unprinted_designs = ["phone case", "robot pendant", "dodecahedron"]
completed_models = []

# Modifies original list
# print_models(unprinted_designs, completed_models)

# Does not modify original list
printing_functions.print_models(unprinted_designs[:], completed_models)
printing_functions.show_printed_models(completed_models)
