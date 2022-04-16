import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator


fig, ax= plt.subplots()

x = np.array([10, 9.5, 9, 8.5, 8, 7.5, 6, 5, 4, 3, 2, 1, 0])
y = np.array([0, 0.4, 0.8, 1.2, 1.7, 2.2, 3.6, 4.6, 5.6, 6.6, 7.6, 8.6, 9.6])
x_minor_locator = AutoMinorLocator(0.5)

ax.xaxis.set_minor_locator(x_minor_locator)
ax.scatter(x, y, s=30, marker="o")
ax.set(xlim=(0, 11), ylim = (0, 11), xticks = np.arange(0, 11), yticks = np.arange(0, 11))

plt.grid(which="minor")
plt.title("Graph : Voltage across Collector and Emitter, Vce v/s Collector Current, Ic")
plt.xlabel("Collector-Emitter Voltage, Vce(Volts)")
plt.ylabel("Collector Current, Ic(mA)")
plt.plot(x,y)
ax.grid(True)

plt.show()