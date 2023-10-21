def send_messages():
    msgs =["Hi","Hello","Awesome"]
    new_msgs =[]
    while msgs:
        dele = msgs.pop()
        print(dele)
        new_msgs.append(dele)
send_messages()