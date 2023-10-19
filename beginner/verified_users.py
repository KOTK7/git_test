unconfirmed_users = ["alice","bob","ruby"]
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"verified {current_user}")
    confirmed_users.append(current_user)
    