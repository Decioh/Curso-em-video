from time import sleep
print("---Mostrando PA---")
n = int(input("Informe o primeiro termo da PA: "))
razao = int(input("Informe a razão da PA: "))
termos = 0
op = 1
while op != 0:
    termos = 0
    op = int(input("\nDigite o número de elementos que deseja ver, ou 0 para sair: "))
    while termos < op:
            print(" {} ".format(n), end="")
            n = n + razao
            termos += 1


print("Finalizando...")
sleep(2)
