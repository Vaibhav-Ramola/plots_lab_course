import numpy as np
import matplotlib.pyplot as plt

Vgs = np.array([0, 2.9, 3, 3.1, 3.24, 3.4, 3.45, 3.66, 3.73, 4, 4.5])
Ids = np.array([0, 0, 0.2, 0.3, 1.4, 5.8, 8, 33.1, 46, 76, 150])

fig, ax = plt.subplots();

ax.scatter(Vgs, Ids)
plt.plot(Vgs, Ids)
ax.set(xlim=(0, 5), ylim = (0, 160), xticks=np.arange(0, 5, 0.5), yticks=np.arange(0, 160, 5))

plt.grid(True)
plt.title("Transfer Characteristics", fontsize = 30)
plt.xlabel("Vgs(V)",fontsize = 15)
plt.ylabel("Ids(mA)", fontsize = 15)

plt.show()

