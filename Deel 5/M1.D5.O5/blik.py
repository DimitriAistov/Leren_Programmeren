import math

diameter = int(input("Wat is de diameter van het blik? "))
hoogte = int(input("Wat is de hoogte van het blik? "))

def calculate_cilinder_content():
    return round((diameter/2)*(diameter/2) * math.pi * hoogte, 1)

print(calculate_cilinder_content())
