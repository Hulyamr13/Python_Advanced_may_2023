from project3.vehicle import Vehicle
from project3.car import Car
from project3.sports_car import SportsCar

vehicle = Vehicle()
print(vehicle.move())

car = Car()
print(car.move())
print(car.drive())

sports_car = SportsCar()
print(sports_car.move())
print(sports_car.drive())
print(sports_car.race())
