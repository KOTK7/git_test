from pathlib import Path

filenames = ['Cats.txt', 'Dogs.txt']

for filename in filenames:
    try:
        path = Path(filename)
        content = path.read_text()
        print(content)
    except FileNotFoundError:
        pass
        # print(f"sorry the {filename} is not found")
        # print("we won't show the files until they are in the right path")
        # break

