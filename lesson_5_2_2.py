# Define a class Songs, it will show the lyrics of a song.
# Its __init__() method should have two arguments:self and lyrics.
# lyrics is a list.
# Inside your class create a method called sing_me_a_song() that prints each element of lyrics on its own line.

class Songs:
    """Class that shows the lyrics of a song"""

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        print("Lyrics of the stored song:")
        for line in self.lyrics:
            print(line)
        print()


Test_Song = Songs(["Start spreading the news",
                    "I'm leaving today",
                    "I want to be a part of it",
                    "New York, New York"])
Test_Song.sing_me_a_song()
