import numpy as np
import matplotlib.pyplot as plt

from plot6_3 import V_carrier_signal

time = np.arange(0, 5, 0.00001)
V_information_signal = 0.25 * np.sin(np.pi * time)
V_carrier_signal = 0.01 * np.sin(np.pi * 100 * time)
V_modulated_signal = V_carrier_signal + V_information_signal

fig, ax = plt.subplots()

ax.set(xlim = (0, 5), ylim = (-0.30, 0.30), xticks = np.arange(0, 5, 1), yticks = np.arange(-0.3, 0.3, 0.05))
ax.set_xlabel("Time (pi/300 Units)", fontsize = 16)
ax.set_ylabel("V_modulated_signal (Volts)", fontsize = 16)
ax.plot(time, V_modulated_signal)
ax.grid(True)

plt.tight_layout()
plt.show()