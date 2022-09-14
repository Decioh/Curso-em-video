while True:
    n = int(input("De qual número você quer ver a tabuada? "))
    if n < 0:
        break
    for i in range (1, 10, 1):
        print(f"{n} x {i} = {n*i}|")

