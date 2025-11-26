print("Hello World");


numeros = list(range(1,21))

# Pares Divisores     ---> todo número composto é formado pela multiplicação de dois números

# ex : [24]

# 2 x 12 
# 3 x 8
# 4 x 6       <---- ponto de virada
# 6 x 4
# 8 x 3
# 12 x 2


for numero in numeros:



    if numero < 2:
        continue

    eh_primo = True

    for i in range(2,int(numero**0.5) + 1):
        if numero % i == 0:
            eh_primo = False
            break
    if eh_primo:
        print(numero)

