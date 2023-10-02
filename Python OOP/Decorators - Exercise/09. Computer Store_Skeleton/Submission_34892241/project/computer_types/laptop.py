from project.computer_types.computer import Computer

class Laptop(Computer):
    def __init__(self, manufacturer: str, model: str):
        super().__init__(manufacturer, model)

    def configure_computer(self, processor: str, ram: int):
        available_processors = {
            "AMD Ryzen 9 5950X": 900,
            "Intel Core i9-11900H": 1050,
            "Apple M1 Pro": 1200
        }

        if processor not in available_processors:
            raise ValueError(f"{processor} is not compatible with laptop {self.manufacturer} {self.model}!")

        if ram not in [2 ** i for i in range(1, 7)] or ram > 64:
            raise ValueError(f"{ram}GB RAM is not compatible with laptop {self.manufacturer} {self.model}!")

        self._processor = processor
        self._ram = ram
        self._price = available_processors[processor] + (ram.bit_length() - 1) * 100

        return f"Created {self.manufacturer} {self.model} with {processor} and {ram}GB RAM for {self.price}$."
