favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'rust',
'phil': 'python',
'john': 'c++'
}
#** adding another name to the dictionary
favorite_languages['jack'] = 'java'
#** checking if key is in the dictionary
for name in favorite_languages:
    if name in favorite_languages:
        print(f"Thank you {name} for responding")
    else:
        print(f"{name} would you please take the poll")