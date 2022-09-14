from time import sleep

pessoas = list()
dados = list()
count = 0
while True:
    dados.append(str(input("Informe o nome: ")))
    dados.append(float(input("Informe o peso: ")))
    pessoas.append(dados[:])
    dados.clear()
    count += 1
    op = str(input("Você deseja inserir mais pessoas?[y/n]".strip()))
    if op in 'nN':
        break
    elif op in 'yY':
        print(f"{count} pessoas inseridas até agora...")
        sleep(2)
        print("Vamos inserir mais uma.")
print(f"{pessoas}")
for i in range(0,len(pessoas)):
    if i == 0:
        M_peso = m_peso = pessoas[i][1]
    else:
        if pessoas[i][1] > M_peso:
            M_peso = pessoas[i][1]
        elif pessoas[i][1 < m_peso]:
            m_peso = pessoas[i][1]
print(f"Maior peso = {M_peso} | Menor peso = {m_peso}")
