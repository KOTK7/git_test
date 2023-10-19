responses = {}
polling_active = True
while polling_active:
    name = input("what is your name?")
    response = input("which mountain you want to climb one day?")
    responses[name]= response
    repeat= input("would you like to let another vote?")
    if repeat =="no":
        polling_active=False
    