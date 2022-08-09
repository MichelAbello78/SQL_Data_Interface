from calendar import c
from re import L
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

x=[1, 2, 3, 4,5]
y=[2.2, 3.5, 3.9, 5.1, 6.3]
df=pd.DataFrame({'x': x, 'y': y})
m=np.polyfit(df['x'], df['y'], l)
f=np.polyld(m)
df.insert(2  ,'Fit', f(df['x']))
plt.scatter(df['x'], df['y'], c="blue")
plt.plot(df['x'], df['Fit'], c='orange')
plt.title('Linear Regression')
plt.xlim([0, 5])
plt.ylim([0, 7])
plt.xlabel('x')
plt.ylabel('y')
plt.show()

