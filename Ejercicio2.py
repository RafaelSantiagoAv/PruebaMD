altura = 9 
print(' ' * altura + '*')
for i in range(altura):
    espacios = ' ' * (altura - i - 1)
    ceros = '0' * (2 * i + 1)
    print(espacios + ceros)