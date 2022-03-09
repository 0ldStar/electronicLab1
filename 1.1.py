import matplotlib.pyplot as plt
import numpy as np


def derivative1(x):  # AO
    return 8 * x / 27 - 6274 / 27


def derivative2(x):  # CK
    return 1 * x / 22 - 721 / 22


def derivative3(x):  # OE
    return 10 * x / 23 - 8006 / 23


I1 = [0.0003, 0.000566, 0.5344, 2.452, 4.417, 6.394, 8.376, 10.36, 12.35, 14.34, 16.33, 18.32]  # мА
U1 = [299.9, 499.7, 732.8, 774.2, 791.4, 802.9, 811.9, 819.4, 825.9, 831.7, 837.1, 842]  # мВ

plt.plot(U1, I1, label='Straight Silicon', c='r')

X1 = np.arange(782, 818)
plt.plot(X1, derivative1(X1), 'k--')
X2 = np.arange(720, 743)
plt.plot(X2, derivative2(X2), 'k--')
X3 = np.arange(800, 842)
plt.plot(X3, derivative3(X3), 'k--')

plt.hlines(10, 0, 818, linestyles='--', colors='black')
plt.vlines(818, 0, 10, linestyles='--', colors='black')
plt.hlines(1, 0, 743, linestyles='--', colors='black')
plt.vlines(743, 0, 1, linestyles='--', colors='black')

plt.scatter(818, 10, label='O')
plt.scatter(818, 0, label='B')
plt.scatter(800, 0, label='E')
plt.scatter(782, 0, label='A')
plt.scatter(743, 1, label='K')
plt.scatter(743, 0, label='D')
plt.scatter(720, 0, label='C')

plt.ylabel('I, мА')
plt.xlabel('U, мВ')

plt.grid()
plt.legend()
plt.show()

print("R0 = %d Ом" % (818 / 10))
print("r0 = %d Ом" % ((818 - 782) / 10))
print("Rк = %d Ом" % (743 / 1))
print("rк = %d Ом" % ((743 - 720) / 1))
print("E = %d мВ" % 800)
