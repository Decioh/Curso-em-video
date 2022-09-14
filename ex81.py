lista = list()
n = 0
i = 0
x = 0
cinco = False
while True:
    aux = (int(input("Insira um valor: ")))
    x += 1
    if aux == 5:
        cinco = True
    for i in range(0, len(lista)):
        if aux < lista[i]:
            n += 1
    lista.insert(n, aux)
    print(f"Valor inserido e ordenado com sucesso")
    n = 0
    op = str(input("Quer continuar inserindo valores? [y] ou [n]"))
    if op == 'n':
        break
                                        #lista.sort(reverse=True)
print(f"a) Foram digitados {x} números | b)Ordem decrescente: {lista} | c) Cinco está na lista? {cinco}")
