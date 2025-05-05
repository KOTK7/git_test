responses = {}
poll_active = True

while poll_active:
    name = input('what is your name?: ')
    response = input('what is your dream vacation?: ')

    responses[name] = response

    repeat = input('would you like to let someone else join the poll? (yes/ no)')

    if repeat == "no":
        poll_active = False
print('---Poll Results---')
for name, response in responses.items():
    print(f'{name.title()} would love to go to {response.title()} ')