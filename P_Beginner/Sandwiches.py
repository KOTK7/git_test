def make_sandwich(*items):
    print('The sandwich will have:')
    for item in items:
        print(f'-{item}')
    print('your sandwich is ready!')
make_sandwich('Salami')
make_sandwich('Salami', 'Beef')
make_sandwich('Salami', 'Beef', 'Salad')