def aprovar(valor,sal,anos):
    meses = anos*12
    parcela = valor/meses
    if parcela >= sal*30/100:
        return False
    else:
        return True

nome=input("Qual o seu nome? ")
valor = float(input("Qual o valor do imóvel? "))
anos = int(input("Em quantos anos deseja pagar? "))
sal=int(input("Qual o seu salário? "))

if(aprovar(valor,sal,anos) == True):
    print("Olá {}, Seu emprestimo foi APROVADO!".format(nome))
else:
    print("Olá {}. Infelizmente, não pudemos aprovar seu crédito.".format(nome))
print("Obrigado pela consulta!")

