import numpy as np
import matplotlib.pyplot as plt

rs = np.arange(0.3, 3.05, 0.05)
es0 = []
es1 = []
et1 = []

for r in rs:
    file = f"./S0/log.{r:.2f}.out"
    with open(file) as data:
        line = ""
        while "ENERGY| Total FORCE_EVAL ( QS ) energy [a.u.]:" not in line:  # Minimization steps
            line = data.readline()
        energy = float(line.split()[-1]) * 27.211386245988  # convertion from kcal/mol to eV
        es0.append(energy)
    file = f"./S1/log.{r:.2f}.out"
    with open(file) as data:
        line = ""
        while "ENERGY| Total FORCE_EVAL ( QS ) energy [a.u.]:" not in line:  # Minimization steps
            line = data.readline()
        energy = float(line.split()[-1]) * 27.211386245988  # convertion from kcal/mol to eV
        es1.append(energy)
    file = f"./T1/log.{r:.2f}.out"
    with open(file) as data:
        line = ""
        while "ENERGY| Total FORCE_EVAL ( QS ) energy [a.u.]:" not in line:  # Minimization steps
            line = data.readline()
        energy = float(line.split()[-1]) * 27.211386245988  # convertion from kcal/mol to eV
        et1.append(energy)



es0 = np.array(es0)
es0 -= es0[-1]
es1 = np.array(es1)
es1 -= es1[-1]
et1 = np.array(et1)
et1 -= et1[-1]


fig = plt.figure(figsize=(10, 6))
plt.tight_layout()
plt.plot(rs, es0, "bo")
plt.plot(rs, es0, "b-", label="S0")

plt.plot(rs, es1, "ro")
plt.plot(rs, es1, "r-", label="S1")

plt.plot(rs, et1, "go")
plt.plot(rs, et1, "g-", label="T1")


plt.ylabel("U")
plt.xlabel("R")
plt.legend()
#plt.xlim(left=0.0)
#plt.ylim((-4,15))
# plt.axes().xaxis.set_minor_locator(MultipleLocator(5))
plt.savefig("graph.png")
plt.show()
