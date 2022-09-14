lista = []
for i in range(0, 5):
    lista.append(int(input("informe um número: ")))
maior = lista[0]
menor = lista[0]
for i in range(1,5):
    if lista[i] > maior:
        maior = lista[i]
        aux_maior = i
    elif lista[i] < menor:
        menor = lista[i]
        aux_menor = i

print(f"Os valores são {lista} \n O maior valor é {max(lista)}, na posição {aux_maior+1}\n O menor valor é {min(lista)}, na posição {aux_menor+1}")
