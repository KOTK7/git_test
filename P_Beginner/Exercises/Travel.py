active = True

responses = {}

dream_places = []

while active:
    # Ask the user to enter three dream travel destinations. Store them in a list.
    dream_place1 = input("what is one of your best dream places?: ")
    response1 = input("And how would you like to go there?: (Car/Plane/Train) ")
    responses['first_place'] = response1

    dream_places.append(dream_place1)
    dream_place2 = input("what is other place of your best dream places?: ")
    response2 = input("And how would you like to go there?: (Car/Plane/Train) ")
    responses['second_place'] = response2

    dream_places.append(dream_place2)

    dream_place3 = input("what is other place you would want to visit?: ")
    response3 = input("And how would you like to go there?: (Car/Plane/Train) ")
    dream_places.append(dream_place3)
    responses['third_place'] = response3
    break

"""def show_resutls():
    print(responses)
    print(dream_places)

show_resutls()
"""
visited_places = []

while dream_places:
    current_place = dream_places.pop()
    print(f"I visited {current_place}!")
    visited_places.append(current_place)

print(visited_places)
