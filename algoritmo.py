import random

cores = ["branco", "azul", "vermelho", "amarelo", "verde"]

item_aleatorio = random.choice(cores)
palavra_escondida = '*' * len(item_aleatorio)
erros = 0
i = 0

while erros < 4 and palavra_escondida != item_aleatorio:

    print("Forca:", palavra_escondida, "\n\nTente adivinhar uma letra:")
    tentativa = input(str)

    indice = item_aleatorio.find(tentativa)

    if indice != -1:

        nova_palavra_escondida = ""

        for i in range(len(item_aleatorio)):

            if item_aleatorio[i] == tentativa:

                nova_palavra_escondida += tentativa

            else:

                nova_palavra_escondida += palavra_escondida[i]

        palavra_escondida = nova_palavra_escondida

        print("Você acertou!!!")

    else:

        erros += 1
        print("Errrrrrrouuuuuuu!!!!!!!!\nQuantidade de erros: ", erros)
