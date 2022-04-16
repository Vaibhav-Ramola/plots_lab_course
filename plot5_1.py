import numpy as np
import matplotlib.pyplot as plt

fig, axs = plt.subplots(2, 1)

timeAxis = np.arange(0, 10, 0.01)

plt.title("Inverting Amplifier", fontsize = 18)

ax1 =  axs[0]# plt.subplot(2, 1, 1)
Vin = 0.27*np.sin(timeAxis*np.pi)
ax1.set(xlim = (0, 10), ylim = (-5, 5), xticks = np.arange(0, 10), yticks = np.arange(-5, 5))
ax1.set_title("Vin = 0.27V", fontsize = 16)
ax1.set_xlabel("Time (pi units)", fontsize = 12)
ax1.set_ylabel("Vin (Volts)", fontsize = 12)
ax1.plot(timeAxis, Vin)
ax1.grid(True)

ax2 = axs[1] #plt.subplot(2, 1, 2)
Vout = -2.7*np.sin(timeAxis*np.pi)
ax2.set(xlim = (0, 10), ylim = (-5, 5), xticks = np.arange(0, 10), yticks = np.arange(-5, 5))
ax2.set_title("Vout = 2.7V", fontsize = 16)
ax2.set_xlabel("Time (pi units)", fontsize = 12)
ax2.set_ylabel("Vout (Volts)", fontsize = 12)
ax2.plot(timeAxis, Vout)
ax2.grid(True)

# print(axs)
# plt.setp(axs[0], ylabel = "Vin (Volts)")
# plt.setp(axs[1], ylabel = "Vout (Volts)")
# plt.setp(axs[:], xlabel = "Time (pi units)")

plt.tight_layout()
plt.show()