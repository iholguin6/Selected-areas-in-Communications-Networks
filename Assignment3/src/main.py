import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#creates panda dataframe
MyData = pd.read_csv('NetFlow_v2.csv')

#create Subset of TCP && Bytes>=100
New_frame = MyData[MyData.PROTOCOL =='tcp']
N = MyData[MyData.BYTES >=100]
print(New_frame)
print(N)
