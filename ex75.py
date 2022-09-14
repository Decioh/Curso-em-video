tupla = (int(input("digite o 1° número ")),
         int(input("Digite o 2° número ")),
         int(input("Digite o 3° número ")),
         int(input("digite o último número ")))

print(f" O número 9 apareceu {tupla.count(9)} vezes. \n O número três aparece na {tupla.index(3)}° posição")

for n in tupla:
    if n % 2 == 0:
        print(n, end='')
