from math import inf as infinity
from random import choice
import platform
import time
from os import system

HUMANO = -1
COMP = +1
from random import randint
lobo = ([0, 4])

ovelha_1 = ([7, 1, 0])
ovelha_2 = ([7, 3, 0])
ovelha_3 = ([7, 5, 0])
ovelha_4 = ([7, 7, 0])

ovelhas = ([0,0,0,0])

tabuleiro = [
    [0, 0, 0, 0, -1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 1, 0, 1],

]

def avaliacao(estado):
    if vitoria_ovelha(estado, COMP):
        placar = +1
    elif vitoria_lobo(estado, HUMANO):
        placar = -1
    else:
        placar = 0

    return placar

def vitoria_lobo(estado, jogador):
    win_estado = [
        [estado[7][1]], [estado[7][3]], [estado[7][5]], [estado[7][7]]      ]
    if [jogador] in win_estado:
        return True
    else:
        return False


def vitoria_ovelha(estado, jogador):
    cell = celulas_vazias_lobo(estado)

    if cell == []:
        return True
    else:
        return False


def fim_jogo(estado):
    return vitoria_lobo(estado, HUMANO) or vitoria_ovelha(estado, COMP)

def celulas_vazias(estado):
    celulas = []
    for x, row in enumerate(estado):
        for y, cell in enumerate(row):
            if cell == 0: celulas.append([x, y])
    return celulas


def celulas_vazias_lobo(estado):
    celulas = []
    for x, row in enumerate(estado):
        for y, cell in enumerate(row):
            if cell == -1:
                if x + 1 < 8 and y + 1 < 8 and estado[x + 1][y + 1] == 0:
                    celulas.append([x + 1, y + 1])
                if x + 1 < 8 and y - 1 >= 0 and estado[x + 1][y - 1] == 0:
                    celulas.append([x + 1, y - 1])
                if x - 1 >= 0 and y - 1 >= 0 and estado[x - 1][y - 1] == 0:
                    celulas.append([x - 1, y - 1])
                if x - 1 >= 0 and y + 1 < 8 and estado[x - 1][y + 1] == 0:
                    celulas.append([x - 1, y - 1])

    return celulas


def celulas_vaziasOvelha(estado):
    celulas = []
    for x, row in enumerate(estado):
        for y, cell in enumerate(row):
            if cell == 1:

                if (x + 1) < 8 and (y - 1) >= 0 and estado[x + 1][y - 1] == 0:
                    celulas.append([x + 1, y - 1])

                if x + 1 < 8 and y + 1 < 8 and estado[x + 1][y + 1] == 0:
                    celulas.append([x + 1, y + 1])

    return celulas


def movimento_valido(x, y):
    if [x, y] in celulas_vaziasOvelha(tabuleiro):
        return True
    else:
        return False


def movimento_validoLobo(x, y):
    if [x, y] in celulas_vazias(tabuleiro):
        tabuleiro[lobo[0]][lobo[1]] = 0
        return True
    else:
        return False


def exec_movimento(x, y, jogador):
    if movimento_valido(x, y):

        if (x == (ovelha_2[0] + 1) and y == (ovelha_2[1] + 1)) or (
                x == (ovelha_2[0] + 1) and y == (ovelha_2[1] - 1)):
            ovelhas[1] = 1

        if (x == (ovelha_1[0] + 1) and y == (ovelha_1[1] + 1)) or (
                x == (ovelha_1[0] + 1) and y == (ovelha_1[1] - 1)):
            ovelhas[0] = 1

        if (x == (ovelha_3[0] + 1) and y == (ovelha_3[1] + 1)) or (
                x == (ovelha_3[0] + 1) and y == (ovelha_3[1] - 1)):
           ovelhas[2] = 1

        if (x == (ovelha_4[0] + 1) and y == (ovelha_4[1] + 1)) or (
                x == (ovelha_4[0] + 1) and y == (ovelha_4[1] - 1)):
            ovelhas[3] = 1

        ov = False

        while ov == False:
            k = randint(0, 3)

            if (ovelhas[k] == 1):

                if (k == 0):
                    ovelha_1[2] = 1
                elif (k == 1):
                    ovelha_2[2] = 1
                elif (k == 2):
                    ovelha_3[2] = 1
                elif (k == 3):
                    ovelha_4[2] = 1
                for i in range(4):
                    ovelhas[i] = 0

                ov = True

        if ovelha_1[2] == 1:
            tabuleiro[ovelha_1[0]][ovelha_1[1]] = 0
            ovelha_1[0] = x
            ovelha_1[1] = y
            ovelha_1[2] = 0

        elif ovelha_2[2] == 1:
            tabuleiro[ovelha_2[0]][ovelha_2[1]] = 0
            ovelha_2[0] = x
            ovelha_2[1] = y
            ovelha_2[2] = 0

        elif ovelha_3[2] == 1:
            tabuleiro[ovelha_3[0]][ovelha_3[1]] = 0
            ovelha_3[0] = x
            ovelha_3[1] = y
            ovelha_3[2] = 0

        elif ovelha_4[2] == 1:
            tabuleiro[ovelha_4[0]][ovelha_4[1]] = 0
            ovelha_4[0] = x
            ovelha_4[1] = y
            ovelha_4[2] = 0

        tabuleiro[x][y] = jogador

        return True
    else:
        return False


def exec_movimentoLobo(x, y, jogador):
    if movimento_validoLobo(x, y):
        tabuleiro[x][y] = jogador
        lobo[0] = x
        lobo[1] = y

        return True
    else:
        return False


def minimax(estado, profundidade, jogador):
    if jogador == COMP:
        melhor = [-1, -1, -infinity]
    else:
        melhor = [-1, -1, +infinity]

    if profundidade == 0 or fim_jogo(estado):
        placar = avaliacao(estado)
        return [-1, -1, placar]
    if jogador == COMP:
        for cell in celulas_vaziasOvelha(estado):
            x, y = cell[0], cell[1]

            estado[x][y] = jogador
            placar = minimax(estado, profundidade - 1, -jogador)
            estado[x][y] = 0
            placar[0], placar[1] = x, y

            if jogador == COMP:
                if placar[2] > melhor[2]:
                    melhor = placar  # valor MAX
            else:
                if placar[2] < melhor[2]:
                    melhor = placar  # valor MIN
    elif jogador == HUMANO:
        for cell in celulas_vazias(estado):
            x, y = cell[0], cell[1]

            estado[x][y] = jogador
            placar = minimax(estado, profundidade - 1, -jogador)
            estado[x][y] = 0
            placar[0], placar[1] = x, y

            if jogador == COMP:
                if placar[2] > melhor[2]:
                    melhor = placar  # valor MAX
            else:
                if placar[2] < melhor[2]:
                    melhor = placar  # valor MIN

    return melhor


def limpa_console():
    os_name = platform.system().lower()
    if 'windows' in os_name:
        system('cls')
    else:
        system('clear')


def exibe_tabuleiro(estado, comp_escolha, humano_escolha):
    print('----------------------------------------')
    for row in estado:
        print('\n----------------------------------------')
        for cell in row:
            if cell == +1:
                print('|', comp_escolha, '|', end='')
            elif cell == -1:
                print('|', humano_escolha, '|', end='')
            else:
                print('|', ' ', '|', end='')
    print('\n----------------------------------------')

def IA_vez(comp_escolha, humano_escolha):
    # profundidade = len(celulas_vazias(tabuleiro))
    profundidade = 4
    if profundidade == 0 or fim_jogo(tabuleiro):
        return

    limpa_console()
    print('Vez do Computador [{}]'.format(comp_escolha))
    exibe_tabuleiro(tabuleiro, comp_escolha, humano_escolha)

    move = minimax(tabuleiro, profundidade, COMP)
    x, y = move[0], move[1]

    exec_movimento(x, y, COMP)
    time.sleep(1)


def HUMANO_vez(comp_escolha, humano_escolha):
    profundidade = 4
    if profundidade == 0 or fim_jogo(tabuleiro):
        return

    movimento = -1
    movimentos = {
        3: [lobo[0] + 1, lobo[1] + 1], 1: [lobo[0] + 1, lobo[1] - 1], 7: [lobo[0] - 1, lobo[1] - 1],
        9: [lobo[0] - 1, lobo[1] + 1],
    }
    # mudar movimentos
    limpa_console()
    print('Vez do HUMANO [{}]'.format(humano_escolha))
    exibe_tabuleiro(tabuleiro, comp_escolha, humano_escolha)

    while (testa_movimento(movimento)):
        try:
            movimento = int(input('Use numero (1, 3, 7 ou 9): '))
            coord = movimentos[movimento]
            tenta_movimento = exec_movimentoLobo(coord[0], coord[1], HUMANO)

            if tenta_movimento == False:
                print('Movimento Inválido')
                movimento = -1


        except KeyboardInterrupt:
            print('Tchau!')
            exit()
        except:
            print('Escolha Inválida!')
""" ---------------------------------------------------------- """
"""
Funcao para testar teclas de opções de movimento do teclado
"""
def testa_movimento(movimento):
	if(movimento == 1 or movimento == 3 or movimento == 7 or movimento == 9):
		return 0
	else:
		return 1

""" ---------------------------------------------------------- """


def main():
    limpa_console()
    humano_escolha = 'L'  
    comp_escolha = 'O'  

    primeiro = 'S'  # se HUMANO e o primeiro
    limpa_console()
    while primeiro != 'S' and primeiro != 'N':
        try:
            primeiro = input('Primeiro a Iniciar?[s/n]: ').upper()
        except KeyboardInterrupt:
            print('Tchau!')
            exit()
        except:
            print('Escolha Errada!')

    # Laço principal do jogo
    while len(celulas_vazias(tabuleiro)) > 0 and not fim_jogo(tabuleiro):
        if primeiro == 'N':
            IA_vez(comp_escolha, humano_escolha)
            primeiro = ''

        HUMANO_vez(comp_escolha, humano_escolha)
        IA_vez(comp_escolha, humano_escolha)

    # Mensagem de Final de jogo
    if vitoria_lobo(tabuleiro, HUMANO):
        limpa_console()
        print('Vez do HUMANO [{}]'.format(humano_escolha))
        exibe_tabuleiro(tabuleiro, comp_escolha, humano_escolha)
        print('Você Venceu!')
    elif vitoria_ovelha(tabuleiro, COMP):
        limpa_console()
        print('Vez do Computador [{}]'.format(comp_escolha))
        exibe_tabuleiro(tabuleiro, comp_escolha, humano_escolha)
        print('Você Perdeu!')
    else:
        limpa_console()
        exibe_tabuleiro(tabuleiro, comp_escolha, humano_escolha)
        print('Empate!')

    exit()


if __name__ == '__main__':
    main()
