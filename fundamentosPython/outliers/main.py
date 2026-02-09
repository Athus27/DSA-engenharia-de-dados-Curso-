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
    
    
def rehect_outliers(data):
    # Função para remover outliers usando o método do desvio interquartil (IQR).
    quartile_1, quartile_3 = np.percentile(data, [25, 75])
    iqr = quartile_3 - quartile_1
    lower_bound = quartile_1 - (1.5 * iqr)
    upper_bound = quartile_3 + (1.5 * iqr)
    filtered_data = [x for x in data if lower_bound <= x <= upper_bound]
    return filtered_data


if __name__ == "__main__":
    main()
    
    