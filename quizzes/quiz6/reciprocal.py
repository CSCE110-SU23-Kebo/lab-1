import math

numbers = [1, 5 / 2, -6, 0, 0.4, -0.17, 'pi', 3.14, 2-6j, math.pi]
for n in numbers:
    try:
        reciprocal = 1 / n
        print(f"The reciprocal of {n} is {round(reciprocal, 2)}")
    except Exception as e:
        print(f"{e}")
