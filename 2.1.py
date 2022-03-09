import matplotlib.pyplot as plt
import numpy as np


def derivative1(x):  # AO
    return 0.25 * x - 98.5


def derivative2(x):  # CK
    return 1 * x / 27 - 338 / 27


def derivative3(x):  # OE
    return 10 * x / 29 - 4069 / 29


I3 = [0.03731, 0.3245, 1.253, 3.2, 5.172, 7.151, 9.134, 11.12, 13.11, 15.1, 17.09, 19.08] # мА
U3 = [281.3, 337.7, 373.6, 399.8, 414.2, 424.6, 432.9, 440, 446.2, 451.9, 457, 461.9] # мВ
plt.plot(U3, I3, label='Straight Germanium', c='r')

X1 = np.arange(392, 434)
plt.plot(X1, derivative1(X1), 'k--')
X2 = np.arange(336, 365)
plt.plot(X2, derivative2(X2), 'k--')
X3 = np.arange(406, 461)
plt.plot(X3, derivative3(X3), 'k--')

plt.hlines(10, 0, 434, linestyles='--', colors='black')
plt.vlines(434, 0, 10, linestyles='--', colors='black')
plt.hlines(1, 0, 365, linestyles='--', colors='black')
plt.vlines(365, 0, 1, linestyles='--', colors='black')

plt.scatter(434, 10, label='O')
plt.scatter(434, 0, label='B')
plt.scatter(392, 0, label='A')
plt.scatter(406, 0, label='E')
plt.scatter(365, 1, label='K')
plt.scatter(365, 0, label='D')
plt.scatter(336, 0, label='C')

plt.ylabel('I, мА')
plt.xlabel('U, мВ')

plt.grid()
plt.legend()
plt.show()

print("R0 = %d Ом" % (434 / 10))
print("r0 = %d Ом" % ((434 - 392) / 10))
print("Rк = %d Ом" % (365 / 1))
print("rк = %d Ом" % ((365 - 336) / 1))
print("E = %d мВ" % 406)
