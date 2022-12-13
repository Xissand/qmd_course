import numpy as np

data = np.loadtxt("imag.dat", max_rows=2000)
y = data[:, 0] * (data[:, 1] + data[:, 2] + data[:, 3]) / 3
integral = np.trapz(y=y, x=data[:, 0])

ww = (
    np.pi
    / 2
    * (5.6 * 10**4)
    ** 2  # Constant https://ru.wikipedia.org/wiki/%D0%9F%D0%BB%D0%B0%D0%B7%D0%BC%D0%B5%D0%BD%D0%BD%D0%B0%D1%8F_%D1%87%D0%B0%D1%81%D1%82%D0%BE%D1%82%D0%B0
    * (
        4 / (3.3809420000000001 * 3.3809420000000001 * 4.1205400000000001) * 10 ** (24)
    )  # Electron density
    ** 1  # square root squared
    / ((1.602 * 10 ** (-12)) ** 2)  # convert from ergs to eV
    * (1.055 * 10 ** (-27)) ** 2  # convert frequency to energy by multiplying by hbar
)
print(integral, ww)
