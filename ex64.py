soma = x = int(0)
while True:
    if x == 999:
        break
    soma += x
    x = int(input("Digite um número para colocar na soma, ou 999 para sair: "))


print("A soma final é: {}".format(soma))
