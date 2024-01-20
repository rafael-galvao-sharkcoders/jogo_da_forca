from random import choice

def winner(letras_certas):
    for i in letras_certas:
        if i != "_":
            return True
        return False

estado_forca = [" _____\n|     |\n|\n|\n|"," _____\n|     |\n|     0\n|\n|"," _____\n|     |\n|     0\n|     |\n|"," _____\n|     |\n|     0\n|    /|\n|"," _____\n|     |\n|     0\n|    /|\ \n|"," _____\n|     |\n|     0\n|    /|\ \n|    /"," _____\n|     |\n|     0\n|    /|\ \n|    / \ "]

palavras = ["Neve", "Orvalho", "AgnÃ³stico", "Ardiloso", "Pato", "AssombraÃ§Ã£o", "Computador", "Problema", "Basket", "Baseball", "Qualquer", "Atraso", "Capivara", "Ave", "Carvalho", "AvÃ´", "Saber", "Rei", "Enforcado", "Azul", "Golfinho", "Xadrez", "Jogo", "Dar"]
palavra_aleatoria = choice(palavras)

tentativa = 7
contador = 0

# verificar tamanho da palavra
for letra in palavra_aleatoria:
    contador = contador + 1

#print(palavra_aleatoria)

letras_certas = ["_" for _ in range(contador)]

# loop principal
while tentativa > 0:

    if tentativa == 7:

        print(estado_forca[0])

        for letra in range(contador):
            print(letras_certas[letra], end="")
        letra_utilizador = input("\nletra: ")
        if letra_utilizador in palavra_aleatoria:
            for i in range(contador):

                if palavra_aleatoria[i] == letra_utilizador:
                    letras_certas[i] = letra_utilizador
            print("letra correta")

        else:
            print("letra incorreta.")
            tentativa = tentativa - 1

    elif tentativa == 6:

        print(estado_forca[1])

        for letra in range(contador):
            print(letras_certas[letra], end="")
        letra_utilizador = input("\nletra: ")
        if letra_utilizador in palavra_aleatoria:

            for i in range(contador):

                if palavra_aleatoria[i] == letra_utilizador:
                    letras_certas[i] = letra_utilizador
            print("letra correta!")

        else:

            print("letra incorreta.")

            tentativa = tentativa - 1
    elif tentativa == 5:

        print(estado_forca[2])

        for letra in range(contador):
            print(letras_certas[letra], end="")
        letra_utilizador = input("\nletra: ")
        if letra_utilizador in palavra_aleatoria:

            for i in range(contador):

                if palavra_aleatoria[i] == letra_utilizador:
                    letras_certas[i] = letra_utilizador
            print("letra correta!")
        else:

            print("letra incorreta.")

            tentativa = tentativa - 1

    elif tentativa == 4:

        print(estado_forca[3])

        for letra in range(contador):
            print(letras_certas[letra], end="")
        letra_utilizador = input("\nletra: ")

        if letra_utilizador in palavra_aleatoria:

            for i in range(contador):

                if palavra_aleatoria[i] == letra_utilizador:
                    letras_certas[i] = letra_utilizador
            print("letra correta!")
        else:

            print("letra incorreta.")

            tentativa = tentativa - 1

    elif tentativa == 3:

        print(estado_forca[4])

        for letra in range(contador):
            print(letras_certas[letra], end="")

        letra_utilizador = input("\nletra: ")
        if letra_utilizador in palavra_aleatoria:

            for i in range(contador):

                if palavra_aleatoria[i] == letra_utilizador:
                    letras_certas[i] = letra_utilizador
            print("letra correta!")
        else:

            print("letra incorreta.")

            tentativa = tentativa - 1

    elif tentativa == 2:

        print(estado_forca[5])

        for letra in range(contador):
            print(letras_certas[letra], end="")

        letra_utilizador = input("\nletra: ")
        if letra_utilizador in palavra_aleatoria:

            for i in range(contador):

                if palavra_aleatoria[i] == letra_utilizador:
                    letras_certas[i] = letra_utilizador
            print("letra correta!")
        else:

            print("letra incorreta.")

            tentativa = tentativa - 1

    elif tentativa == 1:

        print(estado_forca[6])

        for letra in range(contador):
            print(letras_certas[letra], end="")

        letra_utilizador = input("\nletra: ")
        if letra_utilizador in palavra_aleatoria:
            for i in range(contador):

                if palavra_aleatoria[i] == letra_utilizador:
                    letras_certas[i] = letra_utilizador
            print("letra correta!")
        else:

            print("letra incorreta.")

            tentativa = tentativa - 1

    if "_" in letras_certas:
        continue
    else:
        print("ganhou")




