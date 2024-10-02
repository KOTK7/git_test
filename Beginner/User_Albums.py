def make_album(artist_name, title):
    album = {"name":artist_name.title(),"album_name":title.title()}
    print(f"{album['name']} : {album['album_name']}")
    return album
while True:
    info = make_album(input("what is your favourite artist?: ").title(),
        input("what is your favourtie album for that artist?: ").title())
    prompt =  input("q to exit: ")
    if prompt == "q":
        break