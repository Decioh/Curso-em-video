s = input("Insira uma frase para saber se ela é um palindromo: ")
s2 =s.replace(' ', '')
i_s = ''.join(reversed(s2))

if s2 == i_s:
    print("A frase '{}' é um palindromo".format(s))
else:
    print("A frase '{}' não é um palindromo".format(s))