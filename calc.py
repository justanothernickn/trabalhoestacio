
def adi(x, y):
    return x + y

def sub(x, y):
    return x - y

def mult(x, y):
    return x * y

def div(x, y):
    return x / y


print("Operação.")
print("1.Adição")
print("2.Subtração")
print("3.Multicação")
print("4.Divisão")
print("5.Sair")

while True:

    escolha = input("Escolha entre(1/2/3/4/5): ")


    if escolha in ('1', '2', '3', '4', '5'):
        try:
            num1 = float(input("Num1: "))
            num2 = float(input("Num2: "))
        except ValueError:
            print("Inválido. coloque números")
            continue

        if escolha == '1':
            print(num1, "+", num2, "=", adi(num1, num2))

        elif escolha == '2':
            print(num1, "-", num2, "=", sub(num1, num2))

        elif escolha == '3':
            print(num1, "*", num2, "=", mult(num1, num2))

        elif escolha == '4':
            print(num1, "/", num2, "=", div(num1, num2))
        
        elif escolha == '5':
            break
        dnv = input("De novo (s/n): ")
        if dnv == "n":
          break
    else:
        print("Inválido")