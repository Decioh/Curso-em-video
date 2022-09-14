nome = ['', '', '', '']
sexo = ['', '', '', '']
idade = ['0', '0', '0', '0']
count = 0
save = 0
i=0
nome[0] = input("Qual o nome da {}ª pessoa? ".format(i + 1))
idade[0] = int(input("Qual a idade da {}ª pessoa?".format(i + 1)))
sexo[0] = input("Qual o sexo da {}ª pessoa [M] ou [F]? ".format(i + 1)).strip().upper()
for i in range(1,4,1):
    nome[i] = input("Qual o nome da {}ª pessoa? ".format(i+1))
    sexo[i] = input("Qual o sexo da {}ª pessoa [M] ou [F]? ".format(i+1)).strip().upper()
    idade[i] = int(input("Qual a idade da {}ª pessoa?".format(i+1)))
    if sexo == 'M' and idade[i] > idade[i-1] == 'M':
        save = i
    if sexo[i] == "F" and idade[i] < 20:
        count = count + 1
media_idade = (idade[0]+idade[1]+idade[2]+idade[3])/4

print("A média de idade é {}".format(media_idade))
print("O homem mais velho é o {} e ele tem {} anos".format(nome[save], idade[save]))
print("{} Mulheres tem menos de 20 anos".format(count))

