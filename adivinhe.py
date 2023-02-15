from random import randint
import time

# variaveis globais
choose_pc = randint(1, 10)
choose_human = cont = 1
player1 = player2 = choose_play = confir = ""
chance_player1 = cont_player1 = chance_player2 = cont_player2 = 1



print(f"{' ' * 5}JOGO ADIVINHE O NUMERO QUE ESTOU PENSANDO ENTRE 1 E 10")
time.sleep(2)
choose_play = input("Para marcar os jogadores digite s ou n para não marcar: ")

# escolher o nome dos jogadores
if choose_play == "s":
    player1 = input("informe o player 1: ")
    while True:
        confir = input(f"{player1}, se o nome estiver correto digite s ou n para corrigir: ")
        if confir == 'n':
            player1 = input("informe o player 1: ")
        if confir == 's':
            break
if choose_play == "s":
    player2 = input("informe o player 2: ")
    while True:
        confir = input(f"{player2}, se o nome estiver correto digite s ou n para corrigir: ")
        if confir == 'n':
            player2 = input("informe o player 2: ")
        if confir == 's':
            break

# jogo apenas com a máquina ou com dois jogadores
if choose_play == "n":
    print("Estou pensando.", end="")
    time.sleep(1)
    print(".", end="")
    time.sleep(1)
    print(".")
    choose_human = int(input("Adivinhe: "))

    while choose_pc != choose_human:

        if choose_pc == choose_human:
            break
        if choose_human < choose_pc:
            print("O numero fornecido é abaixo do numero escolhido por mim ")
        if choose_human > choose_pc:
            print("O numero fornecido é acima do numero escolhido por mim ")
        choose_human = int(input("Errou, tente novamente: "))
        cont += 1
    print("Parabens você acertou!")
    print(f"sua quantidade de tentativas foi: {cont}")
if choose_play == "s":
    print(f"Vez do {player1}!")
    time.sleep(2)
    print("Estou pensando em um numero.", end="")
    time.sleep(1)
    print(".", end="")
    time.sleep(1)
    print(".")

    chance_player1 = int(input("Adivinhe: "))

    while choose_pc != chance_player1:

        if choose_pc == chance_player1:
            break
        if chance_player1 < choose_pc:
            print("O numero fornecido é abaixo do numero escolhido por mim ")
        if chance_player1 > choose_pc:
            print("O numero fornecido é acima do numero escolhido por mim ")
        chance_player1 = int(input("Errou, tente novamente: "))
        cont_player1 += 1
    print(f"Você acertou!")
    time.sleep(2)

    choose_pc = randint(1, 10)

    print(f"Vez do {player2}!")
    time.sleep(2)
    print("Estou pensando em um numero.", end="")
    time.sleep(1)
    print(".", end="")
    time.sleep(1)
    print(".")

    chance_player2 = int(input("Adivinhe: "))

    while choose_pc != chance_player2:

        if choose_pc == chance_player2:
            break
        if chance_player2 < choose_pc:
            print("O numero fornecido é abaixo do numero escolhido por mim ")
        if chance_player2 > choose_pc:
            print("O numero fornecido é acima do numero escolhido por mim ")
        chance_player2 = int(input("Errou, tente novamente: "))
        cont_player2 += 1
    print(f"Você acertou!")
    time.sleep(2)

    print(f'''
           Player: Tentativas 
    
           {player1}:   {cont_player1}{" " * 4}
           {player2}:   {cont_player2}{" " * 4}
    ''')
    if cont_player1 > cont_player2:
        print(f"Parabéns {player2}, Você ganhou! ")
    elif cont_player1 < cont_player2:
        print(f"Parabéns {player1}, Você ganhou!")
    else:
        print("Incrível, houve um empate!")
