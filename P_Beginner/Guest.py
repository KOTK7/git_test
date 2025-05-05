from pathlib import Path

name = input('Please enter your name: ')

path = Path('Guest.txt')

path.write_text(name)