from abc import ABC, abstractmethod

class Computer(ABC):
    def __init__(self, manufacturer: str, model: str):
        if not manufacturer.strip():
            raise ValueError("Manufacturer name cannot be empty.")
        if not model.strip():
            raise ValueError("Model name cannot be empty.")

        self._manufacturer = manufacturer
        self._model = model
        self._processor = None
        self._ram = None
        self._price = 0

    @abstractmethod
    def configure_computer(self, processor: str, ram: int):
        pass

    @property
    def manufacturer(self):
        return self._manufacturer

    @property
    def model(self):
        return self._model

    @property
    def processor(self):
        return self._processor

    @property
    def ram(self):
        return self._ram

    @property
    def price(self):
        return self._price

    def __repr__(self):
        return f"{self._manufacturer} {self._model} with {self._processor} and {self._ram}GB RAM"
