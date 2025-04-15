pizza_size = {'small':'10$','Medium':'15$','Large':'20$'}
toppings = []
active = True
Pizzas = []
while active:
    print(f'Hey there!, what size of pizza would you like? {pizza_size}')
    print("once you are finished you can type 'done'")
    pizza = input('did you decide yet?: ')
    Pizzas.append(pizza)
    topping = input('and what topping you want with that?: ')
    toppings.append(topping)

    end = input('are you done?: ')
    if end == 'done':
        break

def show_result():
    print(f'Your {Pizzas} with {toppings} is ready!')

def the_cost():
    for Pizza in Pizzas:
        if Pizza == "small":
            print(f'your total will be 10$')
        elif Pizza == "medium":
            print(f'your total will be 15$')
        else:
            print(f'your total will be 20$')

show_result()
the_cost()