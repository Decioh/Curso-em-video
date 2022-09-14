count = 0
for i in range(0,7,1):
    ano = int(input("Qual o ano de nascimento da {}ª pessoa?".format(i+1)))
    if 2022 - ano >= 18:
        count += 1
print("{} pessoas são maiores de idade, e {} são menores ".format(count, 7-count))
