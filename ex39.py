nome = input("Qual o seu nome? ")
n = int(input("informe seu ano de nascimento: "))
idade = 2022-n
if idade < 18:
    print("{}, seu momento ainda vai chegar, você ainda tem {} anos. =(".format(nome, idade))
elif idade > 18:
    print("{}, Já passou da hora de se alistar, você já tem {} anos. =)".format(nome, idade))
else:
    print("{}, está na hora de se alistar, se atente as datas!".format(nome))