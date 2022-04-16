import numpy as np
import matplotlib.pyplot as plt

I_neg = np.array([0, 0, 0, 0, 0, -12.1, -13.2, -14.3, -15.2, -16.6, -17.4, -18.5, -19.8, -21.2, -23.1, -24.3, -25.3])
I_pos = np.array([0, 0, 0, 0, 0, 11.1, 12.3, 13.5, 14.3, 15.3, 16.8, 18.1, 19.4, 20.6, 21.5, 22.8, 24.6])

V_neg = np.array([0, -10, -20, -30, -32, -20, -20, -20, -20, -20, -20, -20, -20, -20, -20, -20, -20])
V_pos = np.array([0, 10, 20, 30, 32, 20.5, 20.5, 20.5, 20.5, 20.5, 20.5, 20.5, 20.5, 20.5, 20.5, 20.5, 20.5])

fig, ax = plt.subplots()

ax.set(xlim = (-25, 25), ylim = (-30, 30), xticks = np.arange(-25, 25, 5), yticks = np.arange(-26, 25, 5))

plt.title("Characteristics of DIAC", fontsize = 20)
plt.ylabel("Current, I (mA)", fontsize = 16)
plt.xlabel("Voltage, V (Volts)", fontsize = 16)
plt.scatter(V_neg, I_neg)
plt.scatter(V_pos, I_pos)
plt.plot(V_neg, I_neg)
plt.plot(V_pos, I_pos)
plt.grid(True)

plt.show()
