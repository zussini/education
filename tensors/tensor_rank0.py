import matplotlib.pyplot as plt
import numpy as np

# Scalar field visualization
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.exp(-0.1 * (X**2 + Y**2))

plt.contourf(X, Y, Z, cmap='viridis')
plt.colorbar(label='Scalar Field')
plt.title('Scalar Field (Rank 0 Tensor)')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

