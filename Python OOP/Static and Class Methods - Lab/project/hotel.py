from project.room import Room

class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        for room in self.rooms:
            if room.number == room_number:
                return room.take_room(people)
        return f"Room number {room_number} not found"

    def free_room(self, room_number):
        for room in self.rooms:
            if room.number == room_number:
                return room.free_room()
        return f"Room number {room_number} not found"

    def status(self):
        free_rooms = [str(room.number) for room in self.rooms if not room.is_taken]
        taken_rooms = [str(room.number) for room in self.rooms if room.is_taken]
        total_guests = sum(room.guests for room in self.rooms if room.is_taken)
        return f"Hotel {self.name} has {total_guests} total guests\nFree rooms: {', '.join(free_rooms)}\nTaken rooms: {', '.join(taken_rooms)}"