expenses = ['food','rent','entertainment']

expen_val = {'food': 200, 'rent' : 300, 'entertainment' : 80}

def add_expen():
    expen_val['clothes'] = 350

add_expen()


class Budget:
    def __init__(self):
        self.electricity = 0
    
    def add_elec():
        electricity = 'electricity'
        expen_val[electricity] = 250
add_once = Budget.add_elec()


val = 0
for value in expen_val.values():
    val += value

if val >= 1100:
    print("We can't afford that")
else:
    print('well that is affordable')
# print(val)