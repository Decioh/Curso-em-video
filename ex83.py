string = str(input("Insira uma fórmula para saber sua viabilidade: \n"))
count = 0

for i, char in enumerate(string):
    if char == '(':
        count += 1
    elif char == ')':
        count -= 1
    elif count < 0:
        break
if count == 0:
    print("É possível")
else:
    print("Impossível")
