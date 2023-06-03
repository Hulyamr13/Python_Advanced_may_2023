import time
from PIL import Image


def teleportation():
    print("Initiating teleportation sequence...")
    time.sleep(2)

    destination = input("Enter the destination address (country): ")
    year = input("Enter the year of teleportation: ")

    print("Teleportation in progress...")
    time.sleep(3)

    print(f"Teleportation successful. Welcome to {destination} in the year {year}!")

    image_path = input("Enter the path to the image file: ")
    image = Image.open(image_path)
    image.show()


teleportation()
