def IMC(peso, tamanho):
    imc = peso  / (tamanho ** 2)
    return imc
peso = float(input("Peso: "))
tamanho = float(input("Tamanho (em metros): "))

# Calculate BMI using the function
resultado = IMC(peso, tamanho)
print("Seu IMC é:", resultado)

if resultado < 18.5:
    print("Você é magro.")
elif 18.5 <= resultado <= 24.9:
    print("Nice, Peso normal!")
elif 25 <= resultado <= 29.9:
    print("Sobrepeso.")
else:
    print("Obeso.")