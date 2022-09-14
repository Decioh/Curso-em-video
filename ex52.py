x = int(input("Insira um número para descobrir se ele é primo: "))
count = 0
for i in range(1,x+1,1):
    if x % i == 0:
        count = count + 1
if count == 2:
    print("O número é primo!")
else:
    print("O número não é primo!")
