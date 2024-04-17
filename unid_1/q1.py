import numpy as np
import matplotlib.pyplot as plt
from func import solution_verify

## Descobrindo os X que satisfazem o A e Montando a Função

# Pontos dados pela questão
data = np.array([[1, 6], [2, 15], [3, 28]])
# Matriz base
A = np.vstack([np.ones(3), data[:, 0], data[:, 0]**2]).T
# Vetor resultante
b = data[:, 1]
# Encontrando os valores de T(u) que satisfazem Au = b
u = solution_verify(A,b)
# Com os pontos encontrados, montar a função
f = lambda x: u[0] + u[1]*x + u[2]*x**2

## Com a função descoberta, montar o gráfico

# Montando a base do gráfico
x_values = np.linspace(-3, 3, 50)
y_values = f(x_values)

plt.plot(x_values, y_values, label=f'f(x) = {u[0]}+{u[1]}*x+{u[2]}*(x^2)')

# Montando pontos destacados
highlight_x = data[:,0]
highlight_y = [f(x) for x in highlight_x]

plt.scatter(highlight_x, highlight_y, color='red', label='Pontos destacados')
# Adicionando y destacado
plt.axvline(0, color='black',linestyle='-',linewidth=1)
# Adicionando linhas verticais
for i in range(len(highlight_x)):
    plt.plot([highlight_x[i],highlight_x[i]],[0,highlight_y[i]],'r--')
    plt.plot([0,highlight_x[i]],[highlight_y[i],highlight_y[i]],'r--')



# Detalhes do gráfico
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Gráfico de f(x)')
plt.legend()

# Exibição do gráfico
plt.grid(True)
plt.show()

