from cmath import sqrt
import matplotlib.pyplot as plt;
import numpy as np;


i = np.arange(0, np.pi/2.0, 0.0001)
del_i = i + np.arcsin(sqrt(3)/2 * np.sqrt(1.52*1.52 - np.power(np.sin(i), 2)) - 1/2 * np.sin(i)) - np.pi/3;

fig,ax = plt.subplots();

ax.set(xlim = (0, 2), ylim = (0, np.pi/2), xticks = np.arange(0, 2, 0.1), yticks = np.arange(0, np.pi/2, 0.1))
ax.plot(i, del_i)
ax.set_title("Total Deviation v/s Entrance angle", fontsize = 16)
ax.set_xlabel("Entrance Angle (Radians)", fontsize = 16)
ax.set_ylabel("Total deviation (Radians)", fontsize = 16)
ax.grid(True)

plt.tight_layout()
plt.show()


