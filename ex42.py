a = float(input("Qual o primeiro lado do triangulo?: "))
b = float(input("Qual o segundo lado do triangulo?: "))
c = float(input("Qual o terceiro lado do triangulo?: "))

if abs(b-c) < a and a < b+c and abs(a-c) < b and b< a+c and abs(a-b) < c and c < a+b:
    t = 1
else:
    print("O triangulo não existe")
    t = 0

if t == 1:
    if a == b and b == c:
        print("O triangulo existe e é equilátero!")
    elif a == b or a == c:
        print("O triangulo existe e é isóceles")
    else:
        print("O triângulo existe e é escaleno")
else:
    print("Impossível calcular, o triangulo não existe!")