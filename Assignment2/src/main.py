import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

MyData = pd.read_csv('NetFlow_v2.csv')

print(MyData['BYTES'].min(),MyData['BYTES'].max(), MyData['BYTES'].mean())

min_val = MyData['BYTES'].min()
max_val = MyData['BYTES'].max()
avg_val = MyData['BYTES'].mean()

plt.ylim(0,1000)
plt.hist(MyData['BYTES'],bins = 500, range=[min_val,max_val])
plt.savefig('NetFlow2')
