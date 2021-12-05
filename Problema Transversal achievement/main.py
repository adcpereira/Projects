import pandas as pd

LISTA = [[".", "."], [3, 5, 6, 7, 8], [], []]

def creat_board(n):
    list = []
    for i in range(n):
        list.append(["."] * n)
    return list

def choose_n():
    while True:
        n = input("----> ")
        try:
            n = int(n)
            if n > 0:
                return n
            else:
                print("Please type a natural number!")
        except:
            print("Please type a number")

def board_print(board):
    print("\n")
    n = len(board)
    data = board
    df = pd.DataFrame(data, index = range(1, n + 1) ,columns=range(1, n + 1))
    print(df)

def player_move(m, bd, n):
    while True:
        move = input(f"Player {m} choose your play: ")
        move = move.split()
        try:
            move = list(map(int, move))
        except:
            print("Please insert numbers")
        if len(move) == 2:
            if type(move[0]) == type(1):
                if max(move) >= 1 or min(move) <= n:
                    if check_move_in_bd(bd, move[0], move[1]) == ".":
                        return move
                    else:
                        print("Position already occupied.")
                else:
                    print(f"Please insert numbers beetween {1} and {n}.")
        else:
            print("Choose a x and y coordinates")


def check_move_in_bd(board, i, j):
    return board[i - 1][j - 1]

def insert_move_in_bd(board, i, j, m):
    board[i - 1][j - 1] = m
    return board

def check_if_winner(bd, c):
    list = []
    for i in range(len(bd)):
        for line in bd:
            if line.count(c) != 1:
                return False
            list.append(line[i])
        if list.count(c) != 1:
            return False
        list = []
    return True
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#Algorithm

def minimax(bd, n):
    pass


def score(bd, n, c):
    if check_if_winner(c):
        pass

def avaiable_spots(bd):
    result = []
    for i, line in enumerate(bd):
        for j ,j_position in enumerate(line):
            if j_position == ".":
                result.append([i, j])
    return result


def main():
    print("Bem vindo ao jogo Transversal achievement!!!")
    print(f"Escolha um n")
    n = choose_n()
    bd = creat_board(n)
    p = 0
    while True:
        p = p + 1
        board_print(bd)
        if p % 2 == 1:
            move = player_move("O", bd, n)
            insert_move_in_bd(bd, move[0], move[1], "O")
            lp = "O"
        elif p % 2 == 0:
            move = player_move("X", bd, n)
            insert_move_in_bd(bd, move[0], move[1], "X")
            lp = "X"
        if p > 2 * (n - 1):
            if check_if_winner(bd, lp):
                board_print(bd)
                print(f"The winner is {lp}!!")
                break
            if p == 2 * n:
                board_print(bd)
                print("Draw")
                break

main()