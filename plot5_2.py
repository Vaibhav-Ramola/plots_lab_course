import numpy as np
import matplotlib.pyplot as plt

fig, axs = plt.subplots(2, 1)

timeStamp = np.arange(0, 10, 0.01)

ax1 = axs[0]
Vin = 0.54 * np.sin(np.pi * timeStamp)
ax1.set(xlim = (0, 10), ylim = (-5, 5), xticks = np.arange(0, 10), yticks = np.arange(-5, 5))
ax1.plot(timeStamp, Vin)
ax1.set_title("Vin = 0.54V", fontsize = 16)
ax1.set_xlabel("Time (pi units)", fontsize = 12)
ax1.set_ylabel("Vin (Volts)", fontsize = 12)
ax1.grid(True)

ax2 = axs[1]
Vout = 5.9 * np.sin(timeStamp * np.pi)
ax2.set(xlim = (0, 10), ylim = (-7, 7), xticks = np.arange(0, 10), yticks = np.arange(-7, 7))
ax2.plot(timeStamp, Vout)
ax2.set_title("Vout = 5.9V", fontsize = 16)
ax2.set_xlabel("Time (pi units)", fontsize = 12)
ax2.set_ylabel("Vout (Volts)", fontsize = 12)
ax2.grid(True)

plt.tight_layout()
plt.show()
