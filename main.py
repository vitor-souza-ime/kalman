import numpy as np
import matplotlib.pyplot as plt

# Simulação: movimento retilíneo uniforme
np.random.seed(42)
n = 50  # número de medições
true_position = np.linspace(0, 10, n)  # posição real (0 a 10 metros)
velocity = 0.2  # velocidade constante (m/s)

# Simulação de medições ruidosas
measurement_noise = np.random.normal(0, 0.5, size=n)
measurements = true_position + measurement_noise

# Inicialização do Filtro de Kalman
estimated_positions = []
x = 0  # estimativa inicial da posição
P = 1  # incerteza inicial
Q = 1e-5  # variância do processo (modelo)
R = 0.25  # variância da medição (sensor)

for z in measurements:
    # PREDIÇÃO
    x_pred = x + velocity  # prediz nova posição
    P_pred = P + Q         # incerteza da predição

    # CORREÇÃO
    K = P_pred / (P_pred + R)         # ganho de Kalman
    x = x_pred + K * (z - x_pred)     # atualização com medição
    P = (1 - K) * P_pred              # nova incerteza

    estimated_positions.append(x)

# Plotando os resultados
plt.figure(figsize=(10, 5))
plt.plot(true_position, label='Posição real')
plt.plot(measurements, label='Medições com ruído', linestyle='dotted')
plt.plot(estimated_positions, label='Filtro de Kalman', linewidth=2)
plt.xlabel('Tempo (s)')
plt.ylabel('Posição (m)')
plt.legend()
plt.title('Filtro de Kalman 1D')
plt.grid(True)
plt.tight_layout()
plt.show()
