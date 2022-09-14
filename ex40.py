nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))

media = (nota2 + nota1)/2

if media < 5 :
    print("REPROVADO. Média {:.2}".format(media))
elif media >= 7 :
    print("Aprovado! Média {:.2}, parabéns!".format(media))
else:
    print("Recuperação final, sua média foi {:.2}".format(media))

