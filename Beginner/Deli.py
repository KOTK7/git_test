sandwich_orders = ["tuna","pepperoni","falafel","kebab","pastrami","pastrami","pastrami"]
finished_sandwiches = []
for sandwich in sandwich_orders:
    print(f" I made your {sandwich} sandwich")
    finished_sandwiches.append(sandwich)
print("Deli has run out of pastrami")
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")
print(sandwich_orders)