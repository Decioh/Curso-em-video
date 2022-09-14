from time import sleep

op = int(0)
x = 0
x = int(input("Informe o 1° número: "))
y = int(input("Informe o 2° número: "))
while op != 5:
    op = int(input("[1] - Somar [2] - Multiplicar\n[3]Maior [4] - Novos números\n\t[5] - sair "))
    if op == 1:
        print("Você escolheu somar!")
        result = x+y
        print("O resultado foi {}".format(result))
        print("retornando pro menu...")
        sleep(2)
    elif op == 2:
        print("Você escolheu multiplicar!")
        result = x * y
        print("O resultado foi {}".format(result))
        print("retornando pro menu...")
        sleep(2)
    elif op == 3:
        maior = x
        if y > maior:
            maior = y
        print("O maior é {}".format(maior))
        print("Retornando pro menu...")
        sleep(2)
    elif op == 4:
        x = int(input("Informe o 1° número: "))
        y = int(input("Informe o 2° número: "))
        print("Atualizando variáveis...")
        sleep(2)
    elif op == 5:
        print("Saindo...")
        sleep(2)
    else:
        print("Opção invalida")

