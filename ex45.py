from random import randint
from time import sleep

empate = 0
vitoria = 0
derrota = 0

print("=-"*10)
print("------Jokenpô!------")

itens = ('Pedra', 'Papel', 'Tesoura', 'Sair')
op = input(" 1 - Iniciar o jogo!\n 3 - Sair")
while op != 3:
    npc = randint(0, 2)
    npc = itens[npc]
    print("=-" * 10)
    print("Placar atual:\nv: {} d: {} e:{}".format(vitoria, derrota, empate))
    print("=-" * 10)
    print(" 0 - Pedra 1 - Papel\n 2 - Tesoura 3 - Sair")

    op = int(input("Escolha: "))
    jogador = itens[op]
    if op == 3:
        print("=-"*10)
        print("\nPlacar final do jogo \n")
        print("Vitórias: {} Derrotas: {} Empates:{}".format(vitoria, derrota, empate))
        if vitoria > derrota:
            print("Parabéns você ganhou!")
        elif vitoria == derrota:
            print("Empate!")
        else:
            print("Você perdeu =(")
        sleep(10)
    else:
        if jogador == npc:
            print("\n Você escolheu {}\n O computador {}.\n Empatou!".format(jogador, npc))
            empate += 1
            sleep(2)
        elif jogador == 'Pedra' and npc == 'Papel':
            print("\n Você escolheu {}\n O computador {}.\n O computador ganhou!".format(jogador, npc))
            derrota += 1
            sleep(2)
        elif jogador == 'Pedra' and npc == 'Tesoura':
            print("\n Você escolheu {}\n O computador {}.\n Você ganhou!".format(jogador, npc))
            vitoria += 1
            sleep(2)
        elif jogador == 'Papel' and npc == 'Pedra':
            print("\n Você escolheu {}\n O computador {}.\n Você ganhou!".format(jogador, npc))
            vitoria += 1
            sleep(2)
        elif jogador == 'Papel' and npc == 'Tesoura':
            print("\n Você escolheu {}\n O computador {}.\n O computador ganhou!".format(jogador, npc))
            derrota += 1
            sleep(2)
        elif jogador == 'Tesoura' and npc == 'Pedra':
            print("\n Você escolheu {}\n O computador {}.\n O computador ganhou!".format(jogador, npc))
            derrota += 1
            sleep(2)
        elif jogador == 'Tesoura' and npc == 'Papel':
            print("\n Você escolheu {}\n O computador {}.\n Você ganhou!".format(jogador, npc))
            vitoria += 1
            sleep(2)

