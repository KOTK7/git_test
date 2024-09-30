usernames = ["hub_player12","plain_cracker77","jadon_banjo45","child_maker66","gojo_lover82"]
new_usernames = ["hub_player12","plain_cracker77","newyorker22","space_invader9","ron_burgandy1"]
for user in new_usernames:
    if user in usernames:
        print(f"{user} is taken, please choose another")
    else:
        print(f"Hello {user}")