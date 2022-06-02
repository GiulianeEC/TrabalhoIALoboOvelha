    #!/usr/bin/env python3
# -*- codificacao: utf-8 -*-
# !/usr/bin/env python3

from math import inf as infinity
from random import choice
import platform
import time
from os import system

HUMANO = -1 # HUMANO = Jogador humano
COMP = +1 # COMP = Maquina

from random import randint
lobo = ([7, 4]) 
#posção inicial

ovelha_1 = ([0, 1, 0])
ovelha_2 = ([0, 3, 0])
ovelha_3 = ([0, 5, 0])
ovelha_4 = ([0, 7, 0])

ovelhas = ([0,0,0,0])

# tabuleiro= dicionário com valores e posição(x,y), onde indica o movi/posição 
# Começa vazio, com zero em todas posições.
tabuleiro = [
    [0, 1, 0, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, -1, 0, 0, 0],
]

#avalia heuristica do estado
def avaliacaoHeuristica(estado):
    if ovelhaVence(estado, COMP):
        placar = +1
    elif loboVence(estado, HUMANO):
        placar = -1
    else:
        placar = 0

    return placar

#avalia o estado do jogador e retorna vitoria dentro das possibilidades:
def loboVence(estado, jogador):
    if lobo[0] <= ovelha_1[0] and lobo[0] <= ovelha_2[0] and lobo[0] <= ovelha_3[0] and lobo[0] <= ovelha_4[0] :
        return True
    else:
        return False

# Se um, dentre todos os alinhamentos pertence um mesmo jogador,então o jogador vence!
def ovelhaVence(estado, jogador):
    cell = jogadasPossiveis_lobo(estado)
    if cell == []:
        return True
    else:
        return False

#será fim de jogo caso ocorra vitória de um dos jogadores.
def fimDojogo(estado):
    return loboVence(estado, HUMANO) or ovelhaVence(estado, COMP)


# verifica celulas vazias e litsa posições ainda possiveis
def celulasVazias(estado):
    celulas = []
    for x, row in enumerate(estado):
        for y, cell in enumerate(row):
            if cell == 0: celulas.append([x, y])
    return celulas


def jogadasPossiveis_lobo(estado):
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


def jogadasPossiveis_Ovelha(estado):
    celulas = []
    for x, row in enumerate(estado):
        for y, cell in enumerate(row):
            if cell == 1:

                if (x + 1) < 8 and (y - 1) >= 0 and estado[x + 1][y - 1] == 0:
                    celulas.append([x + 1, y - 1])

                if x + 1 < 8 and y + 1 < 8 and estado[x + 1][y + 1] == 0:
                    celulas.append([x + 1, y + 1])

    return celulas

#Um movimento é valido se a célula escolhida está vazia.
def movimento_valido(x, y):
    if [x, y] in jogadasPossiveis_Ovelha(tabuleiro):
        return True #se o tabuleiro[x][y] está vazio
    else:
        return False

def movimento_validoLobo(x, y):
    if [x, y] in celulasVazias(tabuleiro):
        tabuleiro[lobo[0]][lobo[1]] = 0
        return True #se o tabuleiro[x][y] está vazio
    else:
        return False

#Executa o movimento no tabuleiro se as coordenadas são válidas
#(x,y) coordenadas e jogador da vez
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

#Função da IA que escolhe o melhor movimento
def minimax(estado, profundidade, jogador):
    # valor-minmax(estado)
    if jogador == COMP:
        melhor = [-1, -1, -infinity]
    else:
        melhor = [-1, -1, +infinity]

    # valor-minimax(estado) = avaliacao(estado)
    if profundidade == 0 or fimDojogo(estado):
        placar = avaliacaoHeuristica(estado)
        return [-1, -1, placar]
    if jogador == COMP:
        for cell in jogadasPossiveis_Ovelha(estado):
            x, y = cell[0], cell[1]

            estado[x][y] = jogador
            placar = minimax(estado, profundidade - 1, -jogador)
            estado[x][y] = 0
            placar[0], placar[1] = x, y

            if placar[2] > melhor[2]:
                    melhor = placar  # valor MAX
            
    elif jogador == HUMANO:
        for cell in celulasVazias(estado):
            x, y = cell[0], cell[1]

            estado[x][y] = jogador
            placar = minimax(estado, profundidade - 1, -jogador)
            estado[x][y] = 0
            placar[0], placar[1] = x, y

            if placar[2] < melhor[2]:
                melhor = placar  # valor MIN


    return melhor # uma lista com [melhor linha, melhor coluna, melhor placar]

def limpa_console():
    os_name = platform.system().lower()
    if 'windows' in os_name:
        system('cls')
    else:
        system('clear')


#Imprime o tabuleiro no console
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


#Chama a função minimax se a profundidade < 8,ou escolhe uma coordenada aleatória.
def IA_vez(comp_escolha, humano_escolha):
    # profundidade = len(celulas_vazias(tabuleiro))
    profundidade = 4
    if profundidade == 0 or fimDojogo(tabuleiro):
        return

    limpa_console()
    print('Vez do Computador [{}]'.format(comp_escolha))
    exibe_tabuleiro(tabuleiro, comp_escolha, humano_escolha)

    move = minimax(tabuleiro, profundidade, COMP)
    x, y = move[0], move[1]

    exec_movimento(x, y, COMP)
    time.sleep(1)

# O HUMANO joga escolhendo um movimento válido
def HUMANO_vez(comp_escolha, humano_escolha):
 
    profundidade = 4
    if profundidade == 0 or fimDojogo(tabuleiro):
        return

    # Dicionário de movimentos válidos
    movimento = -1
    movimentos = {
        3: [lobo[0] + 1, lobo[1] + 1], 1: [lobo[0] + 1, lobo[1] - 1], 7: [lobo[0] - 1, lobo[1] - 1],
        9: [lobo[0] - 1, lobo[1] + 1],
    }

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
            print('Fim de jogo!')
            exit()
        except:
            print('Escolha Inválida!Tente novamente e escolha 1,3,7 ou 9!')

#Funcao para testar as teclas de opções de movimento do teclado
def testa_movimento(movimento):
	if(movimento == 1 or movimento == 3 or movimento == 7 or movimento == 9):
		return 0
	else:
		return 1

#Funcao Principal que chama todas funcoes
def main():
    limpa_console()
    humano_escolha = 'L'  # Pode ser X ou O
    comp_escolha = 'O'  # Pode ser X ou O
    primeiro = 'S'  # se HUMANO e o primeiro

    limpa_console()
    # Laço do jogo
    while len(celulasVazias(tabuleiro)) > 0 and not fimDojogo(tabuleiro):
        if primeiro == 'N':
            IA_vez(comp_escolha, humano_escolha)
            primeiro = ''

        HUMANO_vez(comp_escolha, humano_escolha)
        IA_vez(comp_escolha, humano_escolha)

    # Final de jogo
    if loboVence(tabuleiro, HUMANO):
        limpa_console()
        print('Vez do HUMANO [{}]'.format(humano_escolha))
        exibe_tabuleiro(tabuleiro, comp_escolha, humano_escolha)
        print('Você Venceu!')
    elif ovelhaVence(tabuleiro, COMP):
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