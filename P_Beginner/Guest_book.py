from pathlib import Path

path  = Path('Guest_book.txt')

add_name = ""


while True:
    names = input('Please enter your name: ')
    add_name += names + '\n'
    done = input("If done enter q: ")
    if done == 'q':
        break

path.write_text(add_name)