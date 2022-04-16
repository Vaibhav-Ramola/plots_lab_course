import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

Ia = np.array([0, 0.7, 1.6, 2.6, 3.8, 4.8, 5.8, 7, 7.9, 8.9, 10.3, 11.8, 13.5])
Vak = np.array([10, 9, 8, 7, 6, 5, 4, 3, 1.1, 1.1, 1.1, 1.1, 1.1])

plt.plot(Vak, Ia)
plt.scatter(Vak, Ia, facecolor = "blue", marker = "o")
ax.set(xlim = (0, 11), ylim = (0, 14), xticks = np.arange(0, 11), yticks = np.arange(0, 14))
plt.grid(True)

plt.title("SCR Characteristics (Ig = 2mA)", color = "black", fontsize = 16)
plt.xlabel("Vak (Volts)", color = "black", fontsize = 16)
plt.ylabel("Ia (mA)", color = "black", fontsize = 16)

plt.show()