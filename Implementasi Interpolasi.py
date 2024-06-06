import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange, BarycentricInterpolator

# Data
tegangan = np.array([5, 10, 15, 20, 25, 30, 35, 40])
waktu_patah = np.array([40, 30, 25, 40, 18, 20, 22, 15])

# Interpolasi Lagrange
poly_lagrange = lagrange(tegangan, waktu_patah)
x_range = np.linspace(5, 40, 400)
y_lagrange = poly_lagrange(x_range)

# Plot untuk Interpolasi Lagrange
plt.figure(figsize=(10, 6))
plt.plot(tegangan, waktu_patah, 'o', label='Data', markersize=8)
plt.plot(x_range, y_lagrange, color='blue', label='Interpolasi Lagrange')
plt.xlabel('Tegangan')
plt.ylabel('Waktu Patah')
plt.title('Interpolasi Polinomial Lagrange')
plt.legend()
plt.grid(True)
plt.show()

# Interpolasi Newton
poly_newton = BarycentricInterpolator(tegangan, waktu_patah)
y_newton = poly_newton(x_range)

# Plot untuk Interpolasi Newton
plt.figure(figsize=(10, 6))
plt.plot(tegangan, waktu_patah, 'o', label='Data', markersize=8)
plt.plot(x_range, y_newton, color='orange', linestyle='--', label='Interpolasi Newton')
plt.xlabel('Tegangan')
plt.ylabel('Waktu Patah')
plt.title('Interpolasi Polinomial Newton')
plt.legend()
plt.grid(True)
plt.show()
