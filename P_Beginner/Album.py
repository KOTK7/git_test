def make_album(artist_name, album_name, No_of_songs=None):
    if No_of_songs:
        album = {'artist':artist_name,'album':album_name, 'Songs': No_of_songs}
    else:
        album = {'artist':artist_name,'album':album_name}
    return album
musician1 = make_album('Justin Bieber', 'Journals')
musician2 = make_album('Charlie xcx', 'brat')
musician3 = make_album('Ed Sheeran', 'Example', 12)

print(musician1)
print(musician2)
print(musician3)
