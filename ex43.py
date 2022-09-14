print("=-=-"*10)
m = float(input("Informe seu peso: "))
h = float(input("Informe sua altura: "))
IMC = m/(h**2)

print("{:.2f}".format(IMC))

if IMC <= 18.5:
    print("Abaixo do peso")
elif IMC > 18.5 and IMC <= 25:
    print("Peso ideal")
elif IMC > 25 and IMC <= 30:
    print("Sobrepeso")
elif IMC > 30 and IMC <=40:
    print("Obesidade")
else:
    print("Obesidade mórbida")