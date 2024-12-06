import numpy as np
import matplotlib.pyplot as plt

def plot_electric_field(charges, x_range, y_range, app_title="Trabalho Guilherme Kadubitzki"):
    """
    Simula e visualiza o campo elétrico gerado por um conjunto de cargas pontuais.

    Parameters:
    - charges: lista de tuplas (x, y, q), onde x e y são as coordenadas da carga, e q é a magnitude.
    - x_range: intervalo em x como (x_min, x_max).
    - y_range: intervalo em y como (y_min, y_max).
    - app_title: título para o aplicativo e visualização.
    """
    x_min, x_max = x_range
    y_min, y_max = y_range

    x = np.linspace(x_min, x_max, 50)
    y = np.linspace(y_min, y_max, 50)
    X, Y = np.meshgrid(x, y)

    Ex, Ey = np.zeros(X.shape), np.zeros(Y.shape)

    for cx, cy, q in charges:
        dx = X - cx
        dy = Y - cy
        r = np.sqrt(dx**2 + dy**2)
        r3 = np.where(r != 0, r**3, np.inf)  # Evita divisão por zero
        Ex += q * dx / r3
        Ey += q * dy / r3

    plt.figure(figsize=(8, 6))
    plt.suptitle(app_title, fontsize=16)  # Adiciona o título principal
    plt.streamplot(X, Y, Ex, Ey, color=np.sqrt(Ex**2 + Ey**2), cmap='viridis', linewidth=1, density=1.5)

    for cx, cy, q in charges:
        color = 'red' if q > 0 else 'blue'
        plt.scatter(cx, cy, color=color, s=100 * abs(q), label=f'q = {q} C')

    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.xlabel('X (m)')
    plt.ylabel('Y (m)')
    plt.title('Campo Elétrico Gerado por Cargas Pontuais')
    plt.colorbar(label='Intensidade do Campo (N/C)')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.show()

def get_user_input():
    """
    Permite que o usuário insira as cargas manualmente.
    Retorna uma lista de cargas no formato [(x, y, q), ...].
    """
    charges = []
    print("Insira as cargas (digite 'fim' para encerrar):")
    while True:
        try:
            x = input("Insira a coordenada x da carga (ou 'fim' para encerrar): ")
            if x.lower() == 'fim':
                break
            x = float(x)

            y = float(input("Insira a coordenada y da carga: "))
            q = float(input("Insira a magnitude da carga (em Coulombs): "))

            charges.append((x, y, q))
        except ValueError:
            print("Entrada inválida. Certifique-se de inserir valores numéricos.")
    return charges

# Exemplo de uso:
print("Simulação de Campo Elétrico")
user_charges = get_user_input()
if not user_charges:
    print("Nenhuma carga inserida. Usando valores padrão.")
    user_charges = [
          (0, 0, 1e-9),   # Carga positiva em (0, 0)
        (1, 1, -1e-9),  # Carga negativa em (1, 1)
        (-1, -1, 2e-9)  # Carga positiva em (-1, -1)
    ]

plot_electric_field(user_charges, x_range=(-2, 2), y_range=(-2, 2), app_title="Trabalho Guilherme Kadubitzki")
