Sandwiches = ['Pastrami', 'Salami', 'Eggs', 'Tuna']
Finished_sandwiches = []

while Sandwiches:
    currently_making = Sandwiches.pop()
    print(f'we are making {currently_making}')
    Finished_sandwiches.append(currently_making)

print(Finished_sandwiches)
# print(Sandwiches)