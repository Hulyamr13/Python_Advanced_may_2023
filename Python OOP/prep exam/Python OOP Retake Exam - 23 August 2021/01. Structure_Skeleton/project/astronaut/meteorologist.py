from project.astronaut.astronaut import Astronaut


class Meteorologist(Astronaut):
    OXYGEN_FOR_BREATH = 15
    OXYGEN_UNITS = 90

    def __init__(self, name):
        super().__init__(name, self.OXYGEN_UNITS)