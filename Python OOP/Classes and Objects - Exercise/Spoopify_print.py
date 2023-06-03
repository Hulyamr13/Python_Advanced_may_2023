from project2.song import Song
from project2.album import Album
from project2.band import Band

song = Song("Running in the 90s", 3.45, False)
print(song.get_info())

album = Album("Initial D")
second_song = Song("Around the World", 2.34, False)
print(album.add_song(second_song))
print(album.details())
print(album.publish())

band = Band("Manuel")
print(band.add_album(album))
print(band.remove_album("Initial D"))
print(band.details())
