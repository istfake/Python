import random

# palavras para o jogo
palavras = ["pedra", "chuva", "goteira", "chão", "lua", "macaco", "mar", "sol"]

# escolher uma palavra aleatória


def escolher_palavra(palavras):
    return random.choice(palavras)

# Função para inicializar a palavra oculta com underscores


def inicializar_forca(palavra):
    return "_" * len(palavra)

# Função para substituir underscore pela letra correta


def atualizar_forca(palavra, forca, letra):
    nova_forca = ""
    for i in range(len(palavra)):
        if palavra[i] == letra:
            nova_forca += letra
        else:
            nova_forca += forca[i]
    return nova_forca

# Função para imprimir a palavra oculta com espaços entre as letras


def exibir_forca(forca):
    return " ".join(forca)

# Função principal do jogo


def jogar_forca():
    palavra = escolher_palavra(palavras)
    forca = inicializar_forca(palavra)
    tentativas = 6

    print("Bem-vindo ao jogo da forca!")
    print("Adivinhe a palavra oculta em no máximo 6 tentativas.")
    print(exibir_forca(forca))

    while True:
        letra = input("Digite uma letra: ").lower()

        if letra in palavra:
            forca = atualizar_forca(
                palavra, forca, letra)
            print(exibir_forca(forca))
        else:
            tentativas -= 1
            print(
                "Letra incorreta! Você tem {0} tentativas restantes.".format(tentativas))

        if forca == palavra:
            print(
                "Parabéns! Você adivinhou a palavra correta: '{0}'".format(palavra))
            break

        if tentativas == 0:
            print("Você perdeu! A palavra correta era: '{}'".format(palavra))
            break


# Chamar a função para iniciar o jogo
jogar_forca()
