#compare two function
import matplotlib.pyplot as plt
import numpy as np
x=np.arange(0,2*(np.pi),0.1)
y=np.sin(x)
plt.plot(x,y)
x1,y1=[2,5],[0,4]
plt.plot(x1, y1, marker= 'o')
plt.show()
