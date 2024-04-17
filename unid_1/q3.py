import matplotlib.pyplot as plt
import numpy as np
from scipy.linalg import null_space

# Construa a matriz dos coeficientes
A = np.array([
    [2,3,5,-5],
    [-7,7,0,0],
    [-3,4,1,3],
    [-9,3,-6,-4]
])

solucao1 = np.round(null_space(A),decimals=2)

## Montando o gráfico com Cores

# Definindo as dimensões
x = A[:,0]
y = A[:,1]
z = A[:,2]
w = A[:,3]

# Criando a figura
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Criando o gráfico
scatter = ax.scatter(solucao1[0],solucao1[1],solucao1[2],s=100, c=solucao1[3], cmap='viridis')
ax.scatter(0,0,0,s=100,c=0)

# Legenda
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

# Título
plt.title(f"Pontos: [x1={solucao1[0]},x2={solucao1[1]},x3={solucao1[2]},x4={solucao1[3]}]")

# Colocando valores dos vetores
for i, txt, in enumerate(w):
    ax.text(x[i],y[i],z[i],f'[{x[i]},{y[i]},{z[i]},{w[i]}]',fontsize=10,ha='left',va='bottom')
ax.text(0,0,0,f'[0,0,0,0]',fontsize=10,ha='left',va='bottom')

#Mostrar hiperplano
ax.scatter(x, y, z,s=100,c=w)
plt.plot(x,y,z,color='blue',linestyle='--')

# Barra de cores
cbar = fig.colorbar(scatter, orientation='horizontal')
cbar.set_label('Quarta Dimensão')

# Mostrar o Gráfico
plt.show()

A = np.array([
    [3,4,-7,0],
    [5,-8,7,4],
    [6,-8,6,4],
    [9,-7,-2,0]
])

solucao2 = null_space(A)

## Montando o gráfico com Cores

# Definindo as dimensões
x = A[:,0]
y = A[:,1]
z = A[:,2]
w = A[:,3]

# Criando a figura
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Criando o gráfico
scatter = ax.scatter(solucao2[0],solucao2[1],solucao2[2],s=100, c=solucao2[3], cmap='viridis')
ax.scatter(0,0,0,s=100,c=0)

# Legenda
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

# Título
plt.title(f"Pontos: [x1={solucao2[0]},x2={solucao2[1]},x3={solucao2[2]},x4={solucao2[3]}]")

# Colocando valores dos vetores
for i, txt, in enumerate(w):
    ax.text(x[i],y[i],z[i],f'{w[i]:.2f}',fontsize=10,ha='left',va='bottom')
ax.text(0,0,0,f'[0,0,0,0]',fontsize=10,ha='left',va='bottom')

# Barra de cores
cbar = fig.colorbar(scatter, orientation='horizontal')
cbar.set_label('Quarta Dimensão')

#Mostrar hiperplano
ax.scatter(x, y, z,s=100,c=w)
plt.plot(x,y,z,color='blue',linestyle='--')

# Mostrar o Gráfico
plt.show()

