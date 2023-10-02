from project.computer_types.computer import Computer

class DesktopComputer(Computer):
    def __init__(self, manufacturer: str, model: str):
        super().__init__(manufacturer, model)

    def configure_computer(self, processor: str, ram: int):
        available_processors = {
            "AMD Ryzen 7 5700G": 500,
            "Intel Core i5-12600K": 600,
            "Apple M1 Max": 1800
        }

        if processor not in available_processors:
            raise ValueError(f"{processor} is not compatible with desktop computer {self.manufacturer} {self.model}!")

        if ram not in [2 ** i for i in range(1, 8)] or ram > 128:
            raise ValueError(f"{ram}GB RAM is not compatible with desktop computer {self.manufacturer} {self.model}!")

        self._processor = processor
        self._ram = ram
        self._price = available_processors[processor] + (ram.bit_length() - 1) * 100

        return f"Created {self.manufacturer} {self.model} with {processor} and {ram}GB RAM for {self.price}$."
