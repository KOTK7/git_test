def make_album(artist_name, album_name, No_of_songs=None):
    if No_of_songs:
        album = {'artist':artist_name,'album':album_name, 'Songs': No_of_songs}
    else:
        album = {'artist':artist_name,'album':album_name}
    return album
while True:
    print("Please enter your artist and album name")
    print("enter 'q' at anytime to quit")
    artist = input("artist's name: ")
    if artist == 'q':
        break
    album = input("album's name: ")
    if album == 'q':
        break
    Artist = make_album(artist, album)
print(Artist)