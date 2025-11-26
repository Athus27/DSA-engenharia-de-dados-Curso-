print("Hello World");


numeros = list(range(1,21))

# Pares Divisores     ---> todo número composto é formado pela multiplicação de dois números

# ex : [24]

# 2 x 12 
# 3 x 8
# 4 x 6       <---- ponto de virada, que é aproximadamente (24)^0.5
# 6 x 4
# 8 x 3
# 12 x 2


# Se a raiz for 4.9 -> int vira 4.
# range(2, 4) testaria só 2 e 3.
# range(2, 4 + 1) testa 2, 3 e 4.


for numero in numeros:



    if numero < 2:
        continue

    eh_primo = True

    # O '+ 1' é necessário porque o range do Python para ANTES do último número.
    for i in range(2,int(numero**0.5) + 1):
        if numero % i == 0:
            eh_primo = False
            break
    if eh_primo:
        print(numero)

