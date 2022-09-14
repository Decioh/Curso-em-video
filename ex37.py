import codecs

op = int(input("1- Converter para binario.\n2- Converter para octal.\n3- Converter para hexadecimal. "))

if op == 1:
    n = int(input("Informe um número inteiro: "))
    print("O número {} em binario é {}.".format(n, bin(n)[2:]))
elif op == 2:
    n = int(input("Informe um número inteiro: "))
    print("O número {} em octal é {}.".format(n, oct(n)[2:]))
elif op == 3:
    n = int(input("Informe um número inteiro: "))
    print("o número {} em hexadecimal é {}.".format(n, hex(n)[2:]))
else:
    print("Opção inválida.")
