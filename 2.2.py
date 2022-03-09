import matplotlib.pyplot as plt
import numpy as np

I4 = [0.01, 0.02, 0.051, 0.101, 0.2, 0.5, 0.7, 0.8, 1, 2, 4.998]  # мкА
U4 = [9.99, 19.99, 49.98, 100, 199.9, 499.8, 699.6, 799.6, 999, 2000, 4998]  # мкВ

plt.plot(U4, I4, label='Reverse Germanium', c='r')
plt.grid()
plt.legend()
plt.show()
