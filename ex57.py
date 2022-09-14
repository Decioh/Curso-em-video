op = 'String'
while op != 'M' and op != 'F': #while sexo not in 'mMfF':
    op = input("Qual o seu sexo? \nHomem: [M]\n Mulher: [F]:").upper()
    print("Opção inválida, digite novamente!")
print("Obrigado por responder corretamente!")
