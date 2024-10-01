people ={
    "user1":{"first_name":"Jack","last_name":"Jones","age":"27","city":"NYC"},
    "user2":{"first_name":"John","last_name":"Barbosa","age":"24","city":"Pheonix city"},
    "user3":{"first_name":"Phil","last_name":"Mark","age":"31","city":"Washington"}
}

for key,value in people.items():
    full_name = f'{value["first_name"]} {value["last_name"]}'
    print(f"Hi my name is {full_name}, My age is {value['age']} and I live in {value['city']}")