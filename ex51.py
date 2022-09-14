i = int(input("Insira o primeiro termo da PA: "))
x = int(input("Insira a razão da PA: "))
print(i)
for i in range(i, i+9*x, x): #apenas 9, pois o primeiro termo está fora do for.
    print(i+x)
