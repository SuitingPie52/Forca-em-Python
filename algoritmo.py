import randomimport random

cores = ["branco", "azul", "vermelho", "amarelo", "verde", "marrom", "bege", "roxo", "rosa", "cinza", "dourado",
         "preto"]

animais = ["macaco", "anta", "cavalo", "burro", "cachorro", "gato"]

item_aleatorio = random.choice(cores)
palavra_escondida = '*' * len(item_aleatorio)
erros = 0
i = 0

print("------ BEM VINDO AO JOGO DA FORCA !!! ------\n\n")
total_de_erros = int(input("Escolha a quantidade de erros que você pode cometer: "))

while erros < total_de_erros + 1 and palavra_escondida != item_aleatorio:

    print("\n\nForca:", palavra_escondida, "\n\n")
    tentativa = str(input("Tente adivinhar uma letra: "))

    indice = item_aleatorio.find(tentativa)

    if indice != -1:

        nova_palavra_escondida = ""

        for i in range(len(item_aleatorio)):

            if item_aleatorio[i] == tentativa:

                nova_palavra_escondida += tentativa

            else:

                nova_palavra_escondida += palavra_escondida[i]

        palavra_escondida = nova_palavra_escondida

        print("Tentativa correta !!!")

    else:

        erros += 1
        print("Errrrrrrouuuuuuu!!!!!!!!\nQuantidade de erros: ", erros)


if erros > total_de_erros:

    print("\nFim de jogo... Você ultrapassou o seu limite de erros.\nA palavra era:", item_aleatorio)

elif palavra_escondida == item_aleatorio:

    print("\nVocê venceu !!! Parabéns :D\nA palavra era:", palavra_escondida)

