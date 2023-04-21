import matplotlib.pyplot as drawing
import os
# Step 1: prepare data
# Step 2: Annotate - title, label, legends, axis
# Step 3: plot

a, b, c = input("Enter coefficients: ").split(',')
a, b, c = int(a), int(b), int(c)
x_values = list(range(-10, 11))

# Line chart 1: linear equation
y_values = [a * x + b for x in x_values]
drawing.plot(x_values, y_values, color="g", label=f"{a}x + {b}")

# Line chart 2: quadratic equation
y_values = [a * x ** 2 + b * x + c for x in x_values]
drawing.plot(x_values, y_values, color="r", label=f"{a}x^2 + {b}x + {c}")

drawing.xlabel("x values")
drawing.ylabel("y values")
drawing.yscale('linear')
drawing.legend()
drawing.grid()
drawing.title(f"Linear and quadratic equations")

path = 'equations'
if not os.path.isdir(path):
    os.mkdir(path)  # Make a directory
os.chdir(path)  # Change directory
drawing.savefig('graph.png')

drawing.show()
