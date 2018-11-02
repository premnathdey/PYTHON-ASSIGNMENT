import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
labels=['y1','y2','y3','y4']
ypos=np.arange(len(labels))
size1=[500,700,1500,890]
size2=[485,730,1600,950]
plt.bar(ypos, size1, align='center', alpha=0.5)
plt.xticks(ypos, labels)
plt.ylabel('POPULATION')
plt.title('CITY 1')
plt.show()
plt.bar(ypos, size1, align='center', alpha=0.5)
plt.xticks(ypos, labels)
plt.ylabel('POPULATION')
plt.title('CITY 2')
plt.show()