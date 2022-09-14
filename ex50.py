s = 0
for i in range(1, 7, 1):
    x = int(input("Insira um número: "))
    if x % 2 == 0:
        s += x
print("A soma dos números pares digitados é: {}".format(s))

