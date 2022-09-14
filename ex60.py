print("--- Claculando o fatorial ---")
n = int(input("Insira um número para calcular seu valor em fatorial! "))
fat = 1
i = n
while i < 0:
    fat = fat * i
    i -= 1
print("{}! =".format(n), end="")
for i in range (n, 1, -1):
    print(" {}x".format(i), end="")
print(" 1 => {}".format(fat))
