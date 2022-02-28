import numpy as np
import matplotlib.pyplot as plt
x = []
y = []
u = 2
for i in np.arange(.1, 1.91, .01):
    x.append(i)
    y.append(i/(2*(u**2) * (1 - i/u)))
print(x[-1])
plt.plot(x, y, color='red')
plt.xlabel('Average Arrival Rate (s)')
plt.ylabel('Queueing Delay(Mbps)')
plt.title('Queueing Delay vs Average Arrival')
plt.show()