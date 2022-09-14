produtos = ('Leite', 7.98, 'Ovos', 12.00, 'Baunilha', 3.00, 'Banana', 2.50, 'Coca-Cola', 7.00)

print("="*24)
print(f'{"PRODUTOS":^24}')
print("="*24)
for i in range(0, 9, 2):
    print(f"{produtos[i]:-<13}", end='')
    i += 1
    print(f"R$ {produtos[i]:5.2f} |")
print("="*24)
