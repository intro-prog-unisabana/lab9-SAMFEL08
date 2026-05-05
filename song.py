class Song:
    def __init__(self, name, artist, length):
        self.name = name
        self.artist = artist
        self.length = length
    def get_length_in_seconds(self):
        ensegundos = self.length * 60
        return ensegundos
    def __str__(self):
        return f"'{self.name}' by {self.artist} ({self.length})"