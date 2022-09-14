s = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        s += i
print("A soma de todos os números impares \n múltiplos de 3 entre 1 e 500 é: {}".format(s))