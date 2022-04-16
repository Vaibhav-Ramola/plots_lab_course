import numpy as np
import matplotlib.pyplot as plt
from shapely.geometry import LineString


fig, ax = plt.subplots()

x = [20, 30, 40, 50, 70, 80, 90, 100, 250, 500, 1000, 2000, 5000, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 100000, 200000, 500000, 600000, 800000, 1000000, 2000000, 3000000]
x = np.array(x)
x = np.log10(x)


y = [17.95, 21.48, 22.92, 24.26, 26.05, 27.02, 27.62, 28.07, 30.16, 30.84, 31.00, 31.00, 31.00, 31.00, 31.00, 31.00, 31.00, 31.00, 31.00, 31.00, 31.00, 30.97, 30.84, 30.23, 29.91, 29.26, 28.52, 24.24, 17.62]
y = np.array(y)

ax.scatter(x, y, marker="o", s=16, facecolor = 'black')

ax.set(xlim = (0, 9), ylim = (15, 32), xticks = np.arange(0, 9), yticks = np.arange(15, 32))
plt.ylabel("Gain in dB")
plt.xlabel("log(frequency)")
ax.grid(True)
plt.title("log(frequency) v/s Gain in dB")
fig.tight_layout()

plt.plot(x,y)

m = (y[7]-y[6])/(x[7]-x[6])
c = (y[7]+y[6])/2-m*((x[7]+x[6])/2)

X = np.arange(0,9)
y1 = m*X+c
y2 = np.array(len(X)*[28])

plt1 = LineString(np.column_stack((X, y1)))
plt2 = LineString(np.column_stack((X, y2)))

intersection = plt1.intersection(plt2)
plt.plot(*intersection.xy, 'x', markeredgecolor = "red", markerfacecolor = 'none', markersize = 10)
plt.plot(np.array(len(np.arange(15, 32))*([*intersection.xy[0]])), np.arange(15, 32), linestyle = 'dashed', color = 'black')
print(*intersection.xy[0])
a = [*intersection.xy[0]]


plt.plot(X, y2, linestyle = 'dashed', color = 'black')

m = (y[27]-y[26])/(x[27]-x[26])
c = (y[27]+y[26])/2-m*((x[27]+x[26])/2)

X = np.arange(0,9)
y1 = m*X+c
y2 = np.array(len(X)*[28])

plt1 = LineString(np.column_stack((X, y1)))
plt2 = LineString(np.column_stack((X, y2)))

intersection = plt1.intersection(plt2)

plt.plot(*intersection.xy, 'x',markeredgecolor = 'red', markerfacecolor = 'none', markersize = 10)
plt.plot(np.array(len(np.arange(15, 32))* ([*intersection.xy[0]])), np.arange(15, 32), linestyle = 'dashed', color = 'black')
print(*intersection.xy[0])
b = [*intersection.xy[0]]
ax.plot([a[0], b[0]], [18, 18], '.')
ax.annotate('', xy=(a[0], 18.), xytext=(3, 18), arrowprops=dict(arrowstyle="->"))
ax.annotate('', xy = (b[0], 18), xytext = (5.5, 18), arrowprops = dict(arrowstyle="->"))
ax.annotate("Frequency Bandwidth", xy = (3.3, 17.75), xytext = (3.3, 17.75), fontsize = 20)


plt.show()
