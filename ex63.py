print("-=-=- Sequencia de fibonacci -=-=-")
n = int(input("Quantos números da sequencia de fibonacci você deseja ver? "))
term = 0
a = int(0)
b = int(1)
c = int(0)
while term < n:

        a = c
        print("{} → ".format(a), end=" ")
        c = b
        b = a+b
        term += 1
print("FIM")