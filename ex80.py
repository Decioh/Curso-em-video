lista = list()
n = 0
lista.append(int(input("Insira um valor: ")))
print("O primeiro valor foi inserido com sucesso!")
while True:
    aux = (int(input("Insira outro valor: ")))
    for i in range(0, len(lista)):
        if aux > lista[i]:
            n += 1
    lista.insert(n, aux)
    print(f"Valor inserido com sucesso na posição {n} da lista!")
    n = 0
    op = str(input("Quer continuar inserindo valores? [y] ou [n]"))
    if op == 'n':
        break
print(lista)
