def main():
    super_function(f, 2)

    # 2. Usando Lambda (Anônima) para elevar ao cubo
    # lambda x: x * x * x  ->  função inline que recebe x e retorna x³
    print("\n--- Função Lambda (Cubo) ---")
    resultado = do_something(lambda x: x * x * x, 3)
    print(f"Resultado: {resultado}")

def f():
    print("Function f is called")

def super_function(func, n):
    """Executa uma função n vezes."""
    for _ in range(n):
        func()

def do_something(func, val):
    """Aplica uma função a um valor e retorna o resultado."""
    return func(val)

if __name__ == "__main__":
    main()
    
    
""" - Sobre Calculo Lambda
1.  um sistema formal criado por Alonzo Church na década de 1930. É a base de toda a programação funcional.Tudo é função: No cálculo lambda purista, não existem números ou booleanos nativos;
tudo é construído através de funções.
Regras Básicas:
    Abstração: Criar uma função.
    Aplicação: Aplicar uma função a um argumento 
    Importância: Ele provou que qualquer cálculo matemático pode ser resolvido apenas com funções (equivalente à Máquina de Turing).
    2. Função Lambda (Programação)É a implementação prática do conceito acima nas linguagens modernas (como Python).
    Anônima: Não precisa de um nome (def).
    Efémera: Criada e usada no momento (inline).
    Sintaxe em Python: lambda argumentos: expressão

"""