import numpy as np
import matplotlib.pyplot as plt

time = np.arange(0, 5, 0.00001)
V_information_signal = np.sin(np.pi * time)
V_carrier_signal = 0.01 * np.sin(np.pi * 100 * time)
V_modulated_signal = V_carrier_signal + V_information_signal

fig, ax = plt.subplots()

ax.set(xlim = (0, 5), ylim = (-1.2, 1.2), xticks = np.arange(0, 5), yticks = np.arange(-1.2, 1.2, 0.2))
ax.set_xlabel("Time (pi/300 Units) ", fontsize = 16)
ax.set_ylabel("V_modulated_signal (Volts)", fontsize = 16)
ax.grid(True)
ax.plot(time, V_modulated_signal)

plt.tight_layout()
plt.show()