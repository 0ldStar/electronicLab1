import matplotlib.pyplot as plt
import numpy as np

I2 = [-0.01, -0.02, -0.05, -0.1, -0.2, -0.5, -0.7, -0.8, -1, -2, -5]
U2 = [-9.99, -19.99, -49.98, -100, -199.9, -499.8, -699.6, -799.6, -1000, -2000, -5000]

plt.plot(U2, I2, label='Reverse Silicon', c='r')
plt.grid()
plt.legend()
plt.show()


