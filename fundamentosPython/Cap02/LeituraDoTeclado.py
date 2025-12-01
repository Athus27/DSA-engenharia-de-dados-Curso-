print("Hello, World!")
def average(g1,g2):
    avg = (float(g1)+float(g2))/2
    return avg
    
    
n1 = input("please enter your first grade:\n")
n2 = input("please enter your second grade:\n")
final_grade = average(n1,n2)
print("\nSua nota é ", final_grade)
print("\nSITUAÇÃO:")
if final_grade >= 6:
    print("APROVADO");
else:
    print("REPROVADO");


