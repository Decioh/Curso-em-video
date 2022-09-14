tupla = ('Palmeiras', 'Flamengo', 'Corinthians', 'Fluminense', 'Athletico-PR', 'Internacional', 'Atlético-MG',
         'América-MG', 'Bragantino', 'Santos', 'Sao Paulo', 'Botafogo', 'Goias', 'Ceara', 'Fortaleza', 'Cuiaba',
         'Avaí', 'Coritiba', 'Atlético-GO', 'Juventude')

while True:
    print("##Menu do Brasileirão##")
    print(" 1 - Tabela completa \n 2 - Apenas G6 \n 3 - Apenas z4 \n 4 - Consultar por nome do time \n 5 - Sair")
    op = int(input("Escolha uma opção: "))
    if op == 1:
        print('=' * 18)
        print("Brasileirão 2022")
        print('_' * 18)
        for i in range(0, 20, 1):
            if i < 9:
                print(f"0{i + 1}°|{tupla[i]}")
            else:
                print(f"{i + 1}°|{tupla[i]}")
        print("=" * 18)
        input("Enter para voltar ao menu principal")
    elif op == 2:
        print('=' * 18)
        print("g6 - Brasileirão 2022")
        print('_' * 18)
        for i in range(0, 6, 1):
            if i < 9:
                print(f"0{i + 1}°|{tupla[i]}")
            else:
                print(f"{i + 1}°|{tupla[i]}")
        print("=" * 18)
        input("Enter para voltar ao menu principal")
    elif op == 3:
        print('=' * 18)
        print("z4 - Brasileirão 2022")
        print('_' * 18)
        for i in range(16, 20, 1):
            print(f"{i + 1}°|{tupla[i]}")
            print("=" * 18)
        input("Enter para voltar ao menu principal")
    elif op == 4:
        a = int(input("1- Consultar lista de times 2 - Digitar nome"))
        if a == 1:
            print(sorted(tupla))
        time = str(input("Qual time você deseja consultar a posição? "))
        n = tupla.index(time)
        print(f"{n+1}°| {tupla[n]}")
        input("Enter para voltar ao menu principal")
    elif op == 5:
        break
