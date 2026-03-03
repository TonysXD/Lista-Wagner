lista = []
i = 0
while i < 3:
    numero = float(input(f"Digite o número {i + 1}: "))
    lista.append(numero)

    i += 1
    lista.sort()
print(lista)
print(f"O maior número é {lista[2]}")