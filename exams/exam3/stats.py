# importing package
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

col_list = ['date', 'state', 'male cases', 'female cases']
df = pd.read_csv("starter/covid.csv", usecols=col_list)

print(df['male cases'])
print(df['female cases'])

# a simple line plot
df.plot(kind='bar', x='date', y=['male cases','female cases'])

plt.savefig('cases.png')
plt.show()
