from random import randrange

print("Adivinho o número que o computador 'pensou'")
op = -1
npc = int(randrange(0, 10))
cont = 0
while op != npc:
        op = int(input("Tente acertar, é um número entre 0 e 10: "))
        cont += 1
        if (op != npc):
            print("Errou a sua {}ª tentativa. Continue tentando!".format(cont))
print("Acertou!! O npc 'pensou' '{}' e você acertou em sua {}ª tentativa".format(npc, cont))


