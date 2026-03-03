print("Operação de adição!\n\n")
loop = "s"
while loop == "s":
    n1 = float(input("Digite um número: "))
    n2 = float(input("Digite o segundo número: "))
    print(f"A soma de {n1} + {n2} é igual a {n1 + n2}")
    
    loop = input("Deseja fazer outra conta de adição?[S ou N]: ").lower()