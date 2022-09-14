n = int(1)
soma = float(0.00)
cont = int(0.00)
maior = int(-10000)
menor = int(10000)
while True:
    n = int(input("Digite um número para entrar na média: "))
    soma += n
    cont += 1
    if n > maior:
        maior = n
        if cont == 1:
            menor = n
    elif n < menor:
        menor = n
    op = input("Quer continuar inserindo números? [Y][N]").upper()
    if op == 'N':
        break


print("""Foram digitados {} números.
O maior número digitado foi: {}
O menor número digitado foi: {}
A média dos valores digitados foi: {:.3}""".format(cont, maior, menor, soma/cont))