import numpy as np

filename = "H2_08_1600-WFN_00001_1-1_0.cube"


with open(filename) as file:
    lines = file.readlines()
    ngrid = int(lines[3].split()[0])
    step = float(lines[3].split()[1])

# print(ngrid, step)

mesh = np.loadtxt(filename, skiprows=8).reshape(ngrid, ngrid, ngrid)

# i = np.sum(np.square(mesh) * step**3)
# print(i)

L = ngrid * step

xgrid = np.arange(0, 30, 1) * step

wn = np.sum(np.square(mesh), axis=(1, 2))

xn = (
    -L
    / (2 * np.pi)
    * np.imag(np.log(np.sum((np.exp(-1.0j * 2 * np.pi / L * xgrid) * wn))))
) * 0.529177210903  # Convertion for a.u to A

print("Wannier center:")
print(f"x: {xn:.10f}")

wyn = np.sum(np.square(mesh), axis=(0, 2))

yn = (
    -L
    / (2 * np.pi)
    * np.imag(np.log(np.sum((np.exp(-1.0j * 2 * np.pi / L * xgrid) * wyn))))
) * 0.529177210903  # Convertion for a.u to A

print(f"y: {yn:.10f}")

wzn = np.sum(np.square(mesh), axis=(0, 1))

zn = (
    -L
    / (2 * np.pi)
    * np.imag(np.log(np.sum((np.exp(-1.0j * 2 * np.pi / L * xgrid) * wzn))))
)

print(f"z: {zn:.10f}")
