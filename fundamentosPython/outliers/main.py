import numpy as np
import matplotlib.pyplot as plt

def main():
    # Esse código gera uma distribuição normal de rendas e adiciona um valor extremo (outlier)
    # para demonstrar o impacto nos histogramas.
    
    
    # Cria 10 mil valores aleatórios com média 27k e dispersão de 15k (curva de Gauss).
    # Amostra 10.000 pontos de uma curva gaussiana: centralizados em 27.000 (média) com espalhamento de 15.000 (sigma).

    incomes=np.random.normal(27000,15000,10000)
    incomes= np.append(incomes,[1000000000])
    
    plt.hist(incomes,50)
    plt.xlabel("Income")
    plt.ylabel("Number of People")
    plt.title("Histogram of Incomes")
    plt.show()
if __name__ == "__main__":
    main()
    
    