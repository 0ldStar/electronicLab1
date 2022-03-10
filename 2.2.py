import matplotlib.pyplot as plt
import numpy as np

I4 = [0, 0, -0.001, -0.001, -0.001, -0.001, -0.001, -0.002, -0.002, -0.003, -0.006]  # мкА
U4 = [-10, -20, -50, -100, -200, -500, -700, -800, -1000, -2000, -5000]  # мкВ

plt.plot(U4, I4, label='Reverse Germanium', c='r')
x = np.arange(-5000, 0, 1)
y = -0.001 + x / 1000000
plt.plot(x, y, linestyle="--", c="k")
plt.hlines(-0.004, 0, -5000, color="black", linestyles="--")
plt.scatter(-3000, -0.004, label="O")
plt.scatter(0, -0.001, label="A")
plt.scatter(0, -0.004, label="B")
plt.grid()
plt.xlabel("U, мВ")
plt.ylabel("I, мкА")
plt.legend()
plt.show()