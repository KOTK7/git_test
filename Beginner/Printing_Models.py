def print_models(unprinted_designes, completed_models):
    while unprinted_designes:
        current_design = unprinted_designes.pop()
        print(f"Printing design : {current_design}")
        completed_models.append(current_design)
def show_completed_models(completed_models):
    print("\nthe following designs have been printed:")
    for completed_design in completed_models:
        print(completed_design)
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)