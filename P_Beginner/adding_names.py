usernames = {}

while True:
    name = input('Please enter your name: ')
    username = input('Please enter your username: ')
    usernames[name] = username
    done = input('if done enter q: ')
    if done == 'q':
        break

print(usernames)