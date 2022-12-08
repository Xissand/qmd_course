import numpy as np
import matplotlib.pyplot as plt

rs = np.arange(0.3, 3.05, 0.05)
es = []

for r in rs:
    file = f"data/{r:.2f}/log.lammps"
    with open(file) as data:
        line = ""
        while "Step" not in line:  # Minimization steps
            line = data.readline()
        line = data.readline()
        while "Step" not in line:  # run 0 step
            line = data.readline()
        line = data.readline()
        # line = s[84]
        energy = float(line.split()[1]) * 0.043  # convertion from kcal/mol to eV
        es.append(energy)

mini = np.argmin(es)
minr = rs[mini]
mine = es[mini]

fig = plt.figure(figsize=(10, 6))
plt.tight_layout()
plt.plot(rs, es, "bo")
plt.plot(rs, es, "b-")
plt.vlines(minr, -27, -8, "red", "dashed")
plt.ylabel("U")
plt.xlabel("R")
plt.text(minr + 0.2, -11, f"min of {mine:.2f} eV at {minr:.2f} A")
plt.xlim(left=0.0)
plt.ylim((-27, -8))
# plt.axes().xaxis.set_minor_locator(MultipleLocator(5))
plt.savefig("graph.png")
plt.show()
