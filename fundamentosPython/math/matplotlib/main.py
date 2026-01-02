
import numpy as np
import matplotlib.pyplot as plt


def main():
    x = np.linspace(0, 10, 200) 
    y = np.sin(x)
    plt.plot(x, y, 'b-', linewidth=2) # Plota a linha azul
    plt.title('Exemplo de Grafico com NumPy e Matplotlib')
    plt.xlabel('Eixo X')
    plt.ylabel('Eixo Y')
    plt.show() # Mostra o gráfico

if __name__=="__main__":
    main()
    


