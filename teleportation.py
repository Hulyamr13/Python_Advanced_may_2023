import time


def teleportation():
    print("Initiating teleportation sequence...")
    time.sleep(2)

    destination = input("Enter the destination address (country): ")
    year = input("Enter the year of teleportation: ")

    print("Teleportation in progress...")
    time.sleep(3)

    print(f"Teleportation successful. Welcome to {destination} in the year {year}!")


teleportation()
