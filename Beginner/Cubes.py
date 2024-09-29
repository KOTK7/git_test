cubes = [value for value in range(1,11)]
for value in cubes:
    print(value**3)
#** as a list comprehension
cubess = [value**3 for value in range(1,11)]
print(cubess)