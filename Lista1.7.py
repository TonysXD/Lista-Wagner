suspeita = 0
p1 = input("A pessoa telefonou para a vítima?: ")

if p1 == "sim" or p1 == "s":
    suspeita += 1

p2 = input("A pessoa esteve no local do crime?: ")
if p2 == "sim" or p2 == "s":
    suspeita += 1

p3 = input("A pessoa mora perto da vítima?: ")
if p3 == "sim" or p3 == "s":
    suspeita += 1

p4 = input("A pessoa devia para a vítima?: ")
if p4 == "sim" or p4 == "s":
    suspeita += 1

p5 = input("A pessoa já trabalhou com a vítima?: ")
if p5 == "sim" or p5 == "s":
    suspeita += 1

if suspeita >= 5:
    print("Assassino encontrado!")
elif suspeita > 2:
    print("Cúmplice!")
elif suspeita == 2:
    print("Suspeita!")
else:
    print("Inocente!")