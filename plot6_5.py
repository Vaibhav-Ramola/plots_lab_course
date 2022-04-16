import numpy as np
import matplotlib.pyplot as plt

time = np.arange(0, 10, 0.00001)
V_information_signal = np.sin(np.pi * time)
V_carrier_signal = 0.01 * np.sin(np.pi * 100 * time)

fig, axs = plt.subplots(2, 1)

ax1 = axs[0]
ax1.set(xlim = (0, 10), ylim = (-1.2, 1.2), xticks = np.arange(0, 10), yticks = np.arange(-1.2, 1.2, 0.2))
ax1.set_xlabel("Time (pi/300 Units)", fontsize = 16)
ax1.set_ylabel("V_information_signal (Volts)", fontsize = 16)
ax1.grid(True)
ax1.plot(time, V_information_signal)

ax2 = axs[1]
ax2.set(xlim = (0, 1), ylim = (-0.1, 0.1), xticks = np.arange(0, 1, 0.05), yticks = np.arange(-0.1, 0.1, 0.05))
ax2.set_xlabel("Time (pi/300 Units)", fontsize = 16)
ax2.set_ylabel("V_carrier_signal (Volts)", fontsize = 16)
ax2.grid(True)
ax2.plot(time, V_carrier_signal)

plt.tight_layout()
plt.show()
