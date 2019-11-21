import matplotlib.pyplot as plt

from random_walk import RandomWalk

rw = RandomWalk(50000)

rw.fill_walk()
plt.scatter(rw.x_values,rw.y_values,edgecolors='none',s=1)
plt.show()

