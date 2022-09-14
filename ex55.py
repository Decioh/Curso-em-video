maior = 0.00
menor = 1000.00

for i in range(0,5,1):
    peso = float(input("Informe o peso da {}ª pessoa: ".format(i+1)))
    if peso > maior:
        maior = peso
    elif menor>peso:
        menor = peso
print("O menor peso foi: {}\nO maior peso foi: {}".format(menor, maior))
