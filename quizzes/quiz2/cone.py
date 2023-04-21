# Cone.py
import math

radius = float(input("Radius of the cone: "))
height = float(input("Height of the cone: "))
volume = 1 / 3 * math.pi * math.pow(radius, 2) * height
slant_height = math.sqrt(math.pow(radius, 2) + math.pow(height, 2))
surface = math.pi * math.pow(radius, 2) + math.pi * radius * slant_height

print(f"Volume: {round(volume,2)}")
print(f"Slant height: {round(slant_height, 2)}")
print(f"Surface: {round(surface, 2)}")
