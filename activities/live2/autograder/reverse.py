"""
Live activity 3
Write a Python program reverse.py that asks for a license plate number and reverses only the numeric part.
The license plate format is a two-letter state name abbreviation followed by digits.
You must match the sample output as shown below.
"""

license_number = input("enter plate number: ")
reversed_license_number = license_number[:2]+license_number[:1:-1]
print(f"reversed plate number: {reversed_license_number}")