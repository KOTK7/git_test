current_users = ['john24', 'jack25', 'paul26', 'riley22', 'lara23', 'JOHN24', 'JACK25']
new_users = ['JOHN24', 'JACK25', 'mario44', 'luigi11', 'lolo77']
for user in new_users:
    if user in current_users:
        print(f'sorry {user} you have to use another name')
    else:
        print(f'Hello {user}')