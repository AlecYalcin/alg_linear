import matplotlib.pyplot as plt
import numpy as np

# Defina os componentes do vetor
x = np.random.rand(10)  # coordenadas x
y = np.random.rand(10)  # coordenadas y
z = np.random.rand(10)  # coordenadas z
w = np.random.rand(10)  # quarta dimensão

# Crie a figura
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plote os pontos com a quarta dimensão como tamanho
ax.scatter(x, y, z, s=100*w, c=w, cmap='viridis')

# Adicione rótulos aos eixos
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Mostre o gráfico
plt.show()