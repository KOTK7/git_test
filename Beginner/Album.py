def make_album(artist_name, title, num_songs=""):
    album = {"name":artist_name.title(),"album_name":title.title()}
    if num_songs:
        album["songs"] = num_songs
    return album
info = make_album("justin bieber","journals",num_songs=15)
info1 = make_album("Eminem","curtains",)
info2 = make_album("Rihanna","Diamond",)
print(info)
print(info1)
print(info2)