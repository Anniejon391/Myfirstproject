from cProfile import label
from turtle import title
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

t=np.arrange(0.0,2.0,0.01)
s=1+np.sin(2*np.pi*t)

fig, ax=plt.subplots()
ax.plot(t, s)

ax.set(xlabel='time (s)',ylabel='voltage',
       title='About as simple as it gets')

ax.grid()

plt.show()

fig.savefig('test.png')