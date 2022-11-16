from hotel_rooms.room import Room


class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars):
        return cls(f"{stars} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        for room in self.rooms:
            if room_number == room.number:
                self.guests = people
                return room.take_room(people)

    def free_room(self, room_number):
        for room in self.rooms:
            if room_number == room.number:
                self.guests = 0
                return room.free_room()

    def status(self):
        free_rooms = [room.number for room in self.rooms if not room.is_taken]
        taken_rooms = [room.number for room in self.rooms if room.is_taken]
        total_guests = sum([room.guests for room in self.rooms])

        return f"Hotel {self.name} has {total_guests} total guests\n" \
               f"Free rooms: {', '.join(str(x) for x in free_rooms)}\n" \
               f"Taken rooms: {', '.join(str(x) for x in taken_rooms)}"
