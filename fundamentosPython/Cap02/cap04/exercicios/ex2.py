
def summ(a, b):
    return a + b
def sub(a, b):
    return a -b
def mult(a, b):
    return a*b
def div(a, b):
    return a/b


def main():
    n1 = int(input("Please enter the first number: "))
    n2 = int(input("Please enter the second number: "))
    
    for func in (summ, sub, mult, div):
        print(f"The result of {func.__name__} is: {func(n1, n2)}")
        
        
main()