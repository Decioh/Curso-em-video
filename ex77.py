palavras = ("Sou", "Alvinegro", "Da", "Vila", "Belmiro", "Santos", "Vive")
for i in palavras:
    print(f"\nNa palavra '{i}', temos", end=' ')
    for letra in i:
        if letra.lower() in 'AEIOUaeiou':
            print(f" {letra} ", end='')
