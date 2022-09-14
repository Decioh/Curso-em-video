lista = list()
pares = list()
impares = list()

while True:
    op = str(input("Quer inserir números? [y][n] "))
    if op in 'nN':
        break
    elif op in 'yY':
        lista.append(int(input("Insira seu número: ")))
    else:
        print("Opção invalida, escolha [y]ou[n] ")

for i in range(0, len(lista)):
    if lista[i] % 2 == 0:
        pares.append(lista[i])
    else:
        impares.append(lista[i])

print(f"lista toda: {lista} | Pares: {pares} | Impares: {impares}")
