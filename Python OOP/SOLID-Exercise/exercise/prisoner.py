class Person:
    def __init__(self, position):
        self.position = position

    def walk_north(self, dist):
        self.position[1] += dist

    def walk_east(self, dist):
        self.position[0] += dist


class FreePerson(Person):
    def __init__(self, position):
        super().__init__(position)

    def walk(self, distance_north, distance_east):
        self.walk_north(distance_north)
        self.walk_east(distance_east)


class Prisoner(FreePerson):
    PRISON_LOCATION = (3, 3)

    def __init__(self):
        super().__init__(list(self.PRISON_LOCATION))
        self.is_free = False

    def walk_north(self, dist):
        raise ValueError("A prisoner cannot move freely.")

    def walk_east(self, dist):
        raise ValueError("A prisoner cannot move freely.")


prisoner = Prisoner()
print("The prisoner trying to walk to north by 10 and east by -3.")

try:
    prisoner.walk_north(10)
    prisoner.walk_east(-3)
except ValueError as e:
    pass

print(f"The location of the prison: {prisoner.PRISON_LOCATION}")
print(f"The current position of the prisoner: {tuple(prisoner.position)}")
