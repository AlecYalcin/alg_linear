import numpy as np
import matplotlib.pyplot as plt
from func import solution_verify

## Descobrindo os X que satisfazem o A e Montando a Função

# Pontos dados pela questão
data = np.array([[0,0],[2, 2.90],[4,14.8],[6,39.6],[8,74.3],[10,119]])
# Matriz base
A = np.vstack([np.ones(6), data[:, 0], data[:, 0]**2, data[:,0]**3, data[:,0]**4, data[:,0]**5]).T
# Vetor resultante
b = data[:, 1]
# Encontrando os valores de T(u) que satisfazem Au = b
u = solution_verify(A,b)
# Função descoberta que calcula a força resultante em lb (pounds) baseada na velocidade (ft/sec)
p = lambda t: u[0] + u[1]*t + u[2]*t**2 + u[3]*t**3 + u[4]*t**4 + u[5]*t**5
print(f"A força de 750ft/s em 100lb é de {p(750)}")

## Com a função descoberta, montar o gráfico

# Montando a base do gráfico
x_values = np.linspace(0, 10, 200)
y_values = p(x_values)

plt.plot(x_values, y_values, label=f'p(x) = {round(u[0])}+{round(u[1])}*x{round(u[2])}*(x^2)+{round(u[3])}*(x^3)+{round(u[4])}*(x^4)+{round(u[5])}*(x^5)')

# Montando pontos destacados
highlight_x = data[:,0]
highlight_y = [p(x) for x in highlight_x]

plt.scatter(highlight_x, highlight_y, color='red', label='Pontos destacados')
# Adicionando y destacado
plt.axvline(0, color='black',linestyle='-',linewidth=1)
# Adicionando linhas verticais
for i in range(len(highlight_x)):
    plt.plot([highlight_x[i],highlight_x[i]],[0,highlight_y[i]],'r--')
    plt.plot([0,highlight_x[i]],[highlight_y[i],highlight_y[i]],'r--')

# Detalhes do gráfico
plt.xlabel('velocity(100ft/sec)')
plt.ylabel('Force(100lb)')
plt.title('Gráfico de p(x)')
plt.legend()

# Exibição do gráfico
plt.grid(True)
plt.show()

