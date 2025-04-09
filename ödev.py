from pylab import *
import matplotlib.pyplot as plt

x = [2, -3, -1.5, 3]
y = [3, 1, -2.5, -2]
color = ['m', 'g', 'r', 'b']

fig = plt.figure()
ax = fig.add_subplot(111)

# Noktaları çiz
scatter(x, y, s=100, marker='o', c=color)

# Tüm noktaları sırayla birleştir
for i in range(len(x)-1):
    plt.plot(x[i:i+2], y[i:i+2], 'ro-')

# X ve Y eksenlerini çiz
left, right = ax.get_xlim()
low, high = ax.get_ylim()
arrow(left, 0, right - left, 0, length_includes_head=True, head_width=0.15)
arrow(0, low, 0, high - low, length_includes_head=True, head_width=0.15)

# x = y doğrusunu çiz
xpoints = ypoints = ax.get_xlim()
ax.plot(xpoints, ypoints, linestyle='-', color='k', lw=3, scalex=False, scaley=False)

# === 1. ve 4. bölgeyi birleştir ===
# x > 0 olan noktaları seç
x_pos = []
y_pos = []
for i in range(len(x)):
    if x[i] > 0:
        x_pos.append(x[i])
        y_pos.append(y[i])

# Bu noktaları birleştir
if len(x_pos) >= 2:
    plt.plot(x_pos, y_pos, 'bo--', linewidth=2, label='1. ve 4. bölge')

# Grid ve göster
grid()
legend()
show()
