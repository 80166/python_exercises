# Study drills


class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)


La_La = [
    "In a field of green, under the moon so bright",
    " Lala, lala, dance beneath the starlight",
    "With the wind's soft hum and the crickets'",
    "Lala, lala, we'll sing our cares along.",
]
bulls_on_parade = ["They rally around the family", "With pockets full of shells"]
la_la_song = Song(La_La)
bulls_song = Song(bulls_on_parade)

la_la_song.sing_me_a_song()
bulls_song.sing_me_a_song()
