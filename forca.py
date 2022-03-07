
def jogar():

    print("*********************************")
    print("***Bem vindo no jogo de Forca!***")
    print("*********************************")

    palavra_secreta = "maça".upper()
    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while(not enforcou and not acertou):

        chute = input("Qual letra? ")
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
            print(f"Ops, você errou! Faltam {(6-erros)} tentativas")

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

        letras_faltando = str(letras_acertadas.count('_'))
        print(f'Ainda faltam acertar {letras_faltando} letras')

    if(acertou):
        print("Você ganhou!!")
    else:
        print("Você perdeu!!")
    print ("Fim do jogo")


if(__name__ == "__main__"):
    jogar()