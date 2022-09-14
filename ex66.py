soma = 0
count = 0

while True:
    n = int(input(f"Insira um número: "))
    if n == 999:
        break
    soma += n
    count += 1
print(f"Foram digitados {count} números \nA soma de todos foi {soma} ")