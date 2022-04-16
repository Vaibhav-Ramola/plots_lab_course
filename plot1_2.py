from turtle import color
import numpy as np
import matplotlib.pyplot as plt

Vds35 = np.array([0, 0.01, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
Ids35 = np.array([0, 2.1, 5, 6.2, 7.1, 7.8, 8.6, 9.3, 10.2, 10.7, 10.9, 11.0, 11.1, 11.2, 11.3, 11.4, 11.5, 11.6, 11.7])

Vds4 = np.array([0, 0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.10, 0.2, 0.24, 0.27, 0.3, 0.32, 0.35, 0.38, 0.42, 0.45, 0.7, 0.8, 0.9, 1.0])
Ids4 = np.array([0, 7.6, 15, 23, 32, 41, 50, 58, 67, 80, 95, 114, 120, 127, 136, 139, 141, 142, 143, 144, 144.2, 144.3, 144.4, 144.5])


fig, ax = plt.subplots()

plt.scatter(Vds4, Ids4)
plt.plot(Vds4, Ids4)
plt.scatter(Vds35, Ids35)
plt.plot(Vds35, Ids35)

ax.annotate("Vgs = 4V", xy = (1.0, 145.0), xytext = (1.0, 145.0), fontsize = 13, color = "blue")
ax.annotate("Vgs = 3.5V", xy = (1.0, 12.0), xytext = (1.0, 12.0), fontsize = 13, color = "brown")

ax.set(xlim=(0, 1.1), ylim=(0, 150), xticks = np.arange(0, 1.1, 0.05), yticks=np.arange(0, 150, 10))

plt.title("Drain Characteristics", fontsize=30)
plt.xlabel("Vds(V)", fontsize = 15)
plt.ylabel("Ids(mA)", fontsize = 15)
plt.grid(True)

fig.tight_layout()

plt.show()