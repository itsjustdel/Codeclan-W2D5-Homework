from classes.room import Room
from classes.bar import Bar

class Venue:
    def __init__(self, entry_fee, room_amount, money):
        self.entry_fee = entry_fee                
        self.money = money
        self.rooms = []
        self.bar = Bar()

        # populate room list
        self.create_room_list(room_amount)

    def create_room_list(self, room_amount):                
        for i in range(room_amount):
            # create rooms with max guests equal to 6 for all rooms
            room = Room(i, 6)
            self.rooms.append(room)

