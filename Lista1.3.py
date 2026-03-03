palavra = input("Digite uma palavra: ").lower()

for letra in palavra:
    if letra in 'aeiouáéíóúâêîôûãõ':
        print(f"A letra '{letra}' é uma VOGAL.")
    else:
        print(f"A letra '{letra}' é uma CONSOANTE.")