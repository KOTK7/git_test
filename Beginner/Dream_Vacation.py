program_active = True
poll_taker = {}
while program_active:

    prompt_name = input("What is your name?: ")
    prompt_place = input("What is your dream vacation?: ")
    poll_taker[prompt_name] = prompt_place
    prompt_program = input("is there someone else to poll?: (yes or no) ")
    if prompt_program == "no":
            program_active = False
print("poll has ended")
for name, place in poll_taker.items():
    print(f"{name}'s dream vacation is {place}")