# lançam- se 2 dados, seja X a soma das faces, determiar a distribuição de probabilidade de X.
import matplotlib.pyplot as plt
import numpy as np


def printacoisas():
    #print hello world
    print("Hello")
    print("World")
    
def calcular_distribuicao_probabilidade(quantidade):
    X = {i: 0 for i in range(2, 13)} #dictionary comprehension to map each number in the range to the value 0.
    
    for dado1 in range(1,7):
        for dado2 in range(1,7):
            X[dado1+dado2]+=1
    return X
                
    
    
    
    
def plotar_distribuicao(dados_dict):
    somas = list(dados_dict.keys())
    # Converte contagem em probabilidade (divide por 36)
    probabilidades = [valor / 36 for valor in dados_dict.values()]
    
    # CORREÇÃO AQUI: Use bar em vez de hist
    plt.bar(somas, probabilidades, edgecolor='black')
    
    plt.title("Distribuição de Probabilidade (Soma 2 Dados)")
    plt.xlabel("Soma")
    plt.ylabel("Probabilidade")
    plt.xticks(range(2, 13)) # Força mostrar todos os números no eixo X
    plt.show()
    
    
def main():
    probabilidades = calcular_distribuicao_probabilidade(36)
    plotar_distribuicao(probabilidades)
if __name__ == "__main__":
    main()
    
    
    # DIFERENÇA:
    # plt.hist(dados_brutos): Usa quando você tem uma lista crua (ex: [2, 2, 3, 7...]) e quer que o Python conte a frequência.
    # plt.bar(x, y): Usa quando você JÁ calculou a frequência/probabilidade (seu dicionário) e só quer desenhar as alturas.