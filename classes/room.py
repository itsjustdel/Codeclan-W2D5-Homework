class Room:
    def __init__(self, number, max_guests):
        self.number = number        
        self.max_guests = max_guests
        self.guests = []
        self.songs = []

    def check_in_guest(self, guest):
        self.guests.append(guest)

    def check_out_guest(self, guest):
        self.guests.remove(guest)

    def add_song_to_room(self, song):
        self.songs.append(song)

    def is_room_full(self):
        if len (self.guests) < self.max_guests:
            # room is not full
            return False
        else:
            # no more space at the inn
            return True

    def has_song(self, song):
        return song in self.songs
