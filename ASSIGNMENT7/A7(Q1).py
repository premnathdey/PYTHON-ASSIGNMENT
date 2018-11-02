import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
labels=['Ist Year','IInd Year','IIIrd Year','IVth Year']
ypos=np.arange(len(labels))
sizes=[103,97,77,66]
plt.bar(ypos, sizes, align='center', alpha=0.5)
plt.xticks(ypos, labels)
plt.ylabel('STRENGTH OF STUDENTS')
plt.title('IIIT KALYANI STUDENTS')
plt.show()
import matplotlib.pyplot as mo
colors = ['gold','yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0, 0, 0, 0)
mo.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=False, startangle=140)
mo.axis('equal')
mo.show()

from matplotlib import pyplot as po
import numpy as npi
a = npi.array([66,77,97,103])
po.hist(a, bins=[0, 20, 40, 60, 80, 100])
po.title("histogram")
po.show()