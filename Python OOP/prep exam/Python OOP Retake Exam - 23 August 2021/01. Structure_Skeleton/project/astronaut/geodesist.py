from project.astronaut.astronaut import Astronaut


class Geodesist(Astronaut):
    OXYGEN_UNITS = 50

    def __init__(self, name):
        super().__init__(name, self.OXYGEN_UNITS)