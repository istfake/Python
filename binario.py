binario = input("Digite um número em binário: ")
decimal = 0
expoente = len(binario) - 1

for i in binario:
    decimal += int(i) * 2 ** expoente
    expoente -= 1

print(decimal)
