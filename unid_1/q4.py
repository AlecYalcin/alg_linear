import matplotlib.pyplot as plt
import numpy as np
from func import solution_verify

A = np.array([
    [2,3,5,-5],
    [-7,7,0,0],
    [-3,4,1,3],
    [-9,3,-6,-4]
])

b = np.array([8,7,5,-3])

# Resolva o sistema linear
solucao = solution_verify(A,b)

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
scatter = ax.scatter(solucao[0],solucao[1],solucao[2],s=100, c=solucao[3], cmap='viridis')
ax.scatter(b[0],b[1],b[2],s=100,c=b[3])

# Legenda
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

# Título
plt.title(f"Pontos: [x1={solucao[0]:.0f},x2={solucao[1]:.0f},x3={solucao[2]:.0f},x4={solucao[3]:.0f}]")

# Colocando valores dos vetores
for i, txt, in enumerate(w):
    ax.text(x[i],y[i],z[i],f'[{x[i]},{y[i]},{z[i]},{w[i]}]',fontsize=10,ha='center',va='bottom')
ax.text(b[0],b[1],b[2],f'[{b[0]},{b[1]},{b[2]},{b[3]}]',fontsize=10,ha='center',va='bottom')
ax.text(solucao[0],solucao[1],solucao[2],f'[{solucao[0]:.0f},{solucao[1]:.0f},{solucao[2]:.0f},{solucao[3]:.0f}]',fontsize=10,ha='center',va='bottom')

# Barra de cores
cbar = fig.colorbar(scatter, orientation='horizontal')
cbar.set_label('Quarta Dimensão')

#Mostrar hiperplano
ax.scatter(x, y, z,s=100,c=w)
plt.plot(x,y,z,color='blue',linestyle='--')

# Mostrar o Gráfico
plt.show()

A = np.array([
    [3,4,-7,0],
    [5,-8,7,4],
    [6,-8,6,4],
    [9,-7,-2,0]
])

b = np.array([4,-4,-4,-7])

# Resolva o sistema linear
solucao = solution_verify(A,b)

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
scatter = ax.scatter(solucao[0],solucao[1],solucao[2],s=100, c=solucao[3], cmap='viridis')
ax.scatter(b[0],b[1],b[2],s=100,c=b[3])

# Legenda
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

# Título
plt.title(f"Pontos: [x1={solucao[0]:.0f},x2={solucao[1]:.0f},x3={solucao[2]:.0f},x4={solucao[3]:.0f}]")

# Colocando valores dos vetores
for i, txt, in enumerate(w):
    ax.text(x[i],y[i],z[i],f'[{x[i]},{y[i]},{z[i]},{w[i]}]',fontsize=10,ha='center',va='bottom')
ax.text(b[0],b[1],b[2],f'[{b[0]},{b[1]},{b[2]},{b[3]}]',fontsize=10,ha='center',va='bottom')
ax.text(solucao[0],solucao[1],solucao[2],f'[{solucao[0]:.0f},{solucao[1]:.0f},{solucao[2]:.0f},{solucao[3]:.0f}]',fontsize=10,ha='center',va='bottom')

# Barra de cores
cbar = fig.colorbar(scatter, orientation='horizontal')
cbar.set_label('Quarta Dimensão')

#Mostrar hiperplano
ax.scatter(x, y, z,s=100,c=w)
plt.plot(x,y,z,color='blue',linestyle='--')

# Mostrar o Gráfico
plt.show()
