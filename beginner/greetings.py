def show_messages():
    msgs =["Hi","Hello","Awesome"]
    new_msgs =[]
    while msgs:
        dele = msgs.pop()
        print(dele)
        new_msgs.append(dele)
show_messages()