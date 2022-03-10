import matplotlib.pyplot as plt
import numpy as np

I2 = [0, 0, 0, 0, 0, -0.001, -0.001, -0.001, -0.001, -0.002, -0.005]  # мкА
U2 = [-10, -20, -50, -100, -200, -500, -700, -800, -1000, -2000, -5000]  # мВ

plt.plot(U2, I2, label='Reverse Silicon', c='r')

x = np.arange(-5000, 0, 1)
y = x / 1000000
plt.plot(x, y, linestyle="--", c="k")
plt.vlines(-3000, 0, -0.005, color="black", linestyles="--")
plt.scatter(-3000, -0.003, label="O")
plt.scatter(0, 0, label="A")
plt.scatter(-3000, 0, label="B")
plt.grid()
plt.xlabel("U, мВ")
plt.ylabel("I, мкА")
plt.legend()
plt.show()
