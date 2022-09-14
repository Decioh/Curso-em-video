lista = []
while True:
    aux = int(input("Qual valor você quer adicionar?"))
    if aux not in lista:
        lista.append(aux)
    else:
        print("Valor ja adicionado, tente outro!")
    op = str(input("Quer continuar adicionando valores? [y] ou [n]: "))
    if op == 'n':
        break
print(f'Os valores adicionados, na ordem crescente foram: {sorted(lista)}')
