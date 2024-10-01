pets = {
    "spark":{"kind":"cat","owner name":"lara"},
    "goldy":{"kind":"fish","owner name":"william"},
    "max":{"kind":"dog","owner name":"jake"}
}
pets["lolo"] = {"kind":"dog","owner name":"sasha"}
for name, info in pets.items():
    print(f"{name} is a {info['kind']} and its owner's name is {info['owner name']}")