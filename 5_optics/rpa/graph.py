import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from lxml import etree


fig = plt.figure(figsize=(10, 6))
plt.tight_layout()

data = np.loadtxt("chi.dat")
plt.plot(data[:, 0], data[:, 2], "r-", label="Im(RPA)", lw=1)
plt.plot(data[:, 0], data[:, 1], "r:", label="Re(RPA)", lw=1)


data = np.loadtxt("../nolocal/imag.dat", max_rows=2000)
plt.plot(data[:, 0], data[:, 1], "b-", label="Im(IPA)", lw=1)

data = np.loadtxt("../nolocal/real.dat", max_rows=2000)
plt.plot(data[:, 0], data[:, 1], "b:", label="Re(IPA)", lw=1)


plt.ylabel(r"$\epsilon$")
plt.xlabel("E, eV")
plt.xlim(0, 40.0)
plt.legend()
# plt.yscale("log")
# plt.ylim(bottom=0.005)
# plt.axes().xaxis.set_minor_locator(MultipleLocator(5))
plt.savefig("graph.png")
plt.show()


fig = plt.figure(figsize=(10, 6))
plt.tight_layout()
data = np.loadtxt("chi.dat")
re = data[:, 1]
im = data[:, 2]
m = np.sqrt(re**2 + im**2)
n = np.sqrt((m + re) / 2)
y = ((np.sqrt(m) - 1) / (np.sqrt(m) + 1)) ** 2
plt.plot(data[:, 0], y, "r-", label="R(w)", lw=1)
plt.xlim(0, 40.0)
plt.savefig("r.png")
plt.show()
