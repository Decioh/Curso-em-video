from random import randint
from time import sleep
v = 0
while True:
    op = input("Escolha: [par][impar] ").strip().lower()
    player = int(input("Escolha um número de 0 a 10 para sua jogada!"))
    npc = randint(0, 10)
    if op == 'par':
        if (player + npc) % 2 == 0:
            print(f"Você escolheu {op}\nO npc jogou {npc} e você {player}\nA soma é {player + npc}\nVocê ganhou!!!")
            print("Vamos continuar...")
            v += 1
            sleep(2)
        else:
            print(f"Você escolheu {op}\nO npc jogou {npc} e você {player}\nA soma é {player + npc}\nVocê Perdeu!!!")
            print("O npc ganhou! Encerrando programa...")
            sleep(2)
            break
    elif op == 'impar':
        if (player + npc) % 2 == 0:
            print(f"Você escolheu {op}\nO npc jogou {npc} e você {player}\nA soma é {player + npc}\nVocê Perdeu!!!")
            print("O npc ganhou! Encerrando programa...")
            sleep(2)
            break
        else:
            print(f"Você escolheu {op}\nO npc jogou {npc} e você {player}\nA soma é {player + npc}\nVocê ganhou!!!")
            v += 1
            print("Vamos continuar...")
            sleep(2)
    else:
        print("Escolha [par] ou [impar]")
print(f"Você ganhou {v} vezes seguidas!")

