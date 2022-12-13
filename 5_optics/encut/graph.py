import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from lxml import etree

rs = [150, 200, 250, 300, 350]

fig = plt.figure(figsize=(10, 6))
plt.tight_layout()

for r in rs:
    data = np.loadtxt(f"data/{r}/imag.dat", max_rows=2000)
    plt.plot(data[:, 0], data[:, 1], label=f"{r}", lw=1)

plt.ylabel(r"$\epsilon$")
plt.xlabel("E, eV")
plt.xlim(0, 50.0)
plt.legend()
# plt.yscale("log")
# plt.ylim(bottom=0.005)
# plt.axes().xaxis.set_minor_locator(MultipleLocator(5))
plt.savefig("graph.png")
plt.show()

rsn = [250, 350]

fig = plt.figure(figsize=(10, 6))
plt.tight_layout()

for r in rsn:
    data = np.loadtxt(f"data/{r}/imag.dat", max_rows=2000)
    plt.plot(data[:, 0], data[:, 1], label=f"{r}", lw=1)

plt.ylabel(r"$\epsilon$")
plt.xlabel("E, eV")
plt.xlim(0, 50.0)
plt.legend()
# plt.yscale("log")
# plt.ylim(bottom=0.005)
# plt.axes().xaxis.set_minor_locator(MultipleLocator(5))
plt.savefig("graph_mod.png")
plt.show()
