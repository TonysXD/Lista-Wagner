turno = input("Digite em qual turno você estuda: ").lower()

if turno == "v" or turno == "vespertino":
    print("Boa tarde!")

if turno == "m" or turno == "matutino":
    print("Bom dia!")

if turno == "n" or turno == "noturno":
    print("Boa noite!")
else:
    print("Digite um valor válido!")