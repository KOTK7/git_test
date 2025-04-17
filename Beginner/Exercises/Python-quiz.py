quiz = {'current_version':'3.13','book_name':'Python crash course','how_to_print':'print()'}

answered = {}
def start_quiz():
    for key in quiz.keys():
        answer = input(f'what is {key}?: ')
        answered[key] = answer

def compare():
    for key in quiz.keys():
        if answered[key] == quiz[key]:
            print(f"{key}: Correct ✅")
        else:
            print(f"{key}: Incorrect ❌")
start_quiz()
compare()