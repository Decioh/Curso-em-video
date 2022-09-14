print("---Mostrando PA---")
n = int(input("Informe o primeiro termo da PA: "))
razao = int(input("Informe a razão da PA: "))
termos = 0
while termos < 10:
    print(" {} ->".format(n), end="")
    n = n + razao
    termos += 1
