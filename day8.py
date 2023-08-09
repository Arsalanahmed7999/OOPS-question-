#1. Create a class called "MusicPlayer" with attributes playlist and current_song. The "playlist" attribute should be a list that stores the names of songs in the playlist. Implement methods to add a song to the playlist, remove a song from the playlist, and play the next song in the playlist. Create an instance of the class and add some songs to the playlist. Test the methods by adding, removing, and playing songs from the playlist.


class MusicPlayer:
    def __init__(self, playlist, current_song) -> None:
        self.playlist = playlist
        self.current_song = current_song
    
    def add_song(self, song):
        self.playlist.append(song)

    def remove_song(self, song):
        if song in self.playlist:
            self.playlist.remove(song)
        else:
            print('The song in not in the playlist')

    def play_next_song(self):
        if(len(self.playlist) > 0):
            self.current_song = self.playlist.pop(0)
            return ('The current song', self.current_song)
        else:
            return ('The playlist is empty')






a = MusicPlayer(['song1', 'song2'], 'songx')
# print(a.playlist)
# (a.add_song('anysongadded'))
# print(a.playlist)
a.remove_song('song1')
a.remove_song('song2')
# (a.playlist)
print(a.play_next_song())

# playlist = ['song1', 'song2']
# print(playlist)
# playlist.append('song3')
# print(playlist)


# playlist = ['song1', 'song2']
# print(playlist)
# playlist.remove('song3')
# print(playlist)

# playlist = []
# print(playlist.pop(0))