altura = 9  # Filas de ceros

# Imprimir la estrella
print(' ' * altura + '*')

# Imprimir las filas de ceros
for i in range(altura):
    espacios = ' ' * (altura - i - 1)
    ceros = '0' * (2 * i + 1)
    print(espacios + ceros)