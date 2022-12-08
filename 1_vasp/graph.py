import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from lxml import etree

rs = np.arange(0.3, 3.05, 0.05)
es = []

for r in rs:
    file = f"data/{r:.2f}/vasprun.xml"
    tree = etree.parse(file)
    energy = float(tree.xpath("//calculation/energy/i")[0].text)  # get e_fr_energy
    es.append(energy)

mini = np.argmin(es)
minr = rs[mini]
mine = es[mini]

fig = plt.figure(figsize=(10, 6))
plt.tight_layout()
plt.plot(rs, es, "bo")
plt.plot(rs, es, "b-")
plt.vlines(minr, -7, 8, "red", "dashed")
plt.ylabel("U")
plt.xlabel("R")
plt.text(minr + 0.2, 6, f"min of {mine:.2f} eV at {minr:.2f} A")
plt.xlim(left=0.0)
plt.ylim((-7, 8))
# plt.axes().xaxis.set_minor_locator(MultipleLocator(5))
plt.savefig("graph.png")
plt.show()
