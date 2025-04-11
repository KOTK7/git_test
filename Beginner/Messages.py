def show_messages(messages):
    for msg in messages:
        return messages

short_messages = ['Hello world!', 'Great Book!', 'I really recommend']
The_messages = show_messages(short_messages)

# for msg in The_messages:
#     print(msg)
# print(The_messages)

def send_messages():
    sent_messages = []

    while The_messages:
        currently_sending = The_messages.pop()
        print(f'We are currently sending "{currently_sending}"')
        sent_messages.append(currently_sending)
    print(f'We succesfully sent: {len(sent_messages)} Messages')

send_messages()
print(The_messages)
