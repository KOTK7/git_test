program_active = True
poll_taker = {}
#** the program will work as long as it equalls true
while program_active:
#** storing user input : their name and their dream vacation
    prompt_name = input("What is your name?: ")
    prompt_place = input("What is your dream vacation?: ")
    poll_taker[prompt_name] = prompt_place
#** testing if there is someone else
    prompt_program = input("is there someone else to poll?: (yes or no) ")
    if prompt_program == "no":
#** if it equalls no the program ends
            program_active = False
print("poll has ended")
#** printing each answer
for name, place in poll_taker.items():
    print(f"{name}'s dream vacation is {place}")