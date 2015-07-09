# -*- coding: utf-8 -*-
import random
import helper

board = [[0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0]]
         
UP, DOWN, LEFT, RIGHT = ('w', 's', 'a', 'd')

inplay = True

def create_number(board):
    has_gap = False
    for i in range(4): # 检查棋盘有无空位
        for j in range(4):
            if board[i][j] == 0:
                has_gap = True
                break
    while has_gap:
        row = random.randrange(0, 4)
        col = random.randrange(0, 4)
        if board[row][col] == 0:
            board[row][col] = 2
            return

def init():
    global board
    for i in range(3):
        create_number(board)


def move_left(board):
    for i in range(4): # 行
        combined = False
        for j in range(1, 4): # 列
            if board[i][j] != 0:
                for k in range(j, 0, -1): # 列
                    if board[i][k-1] == 0:
                        board[i][k-1] = board[i][k]
                        board[i][k] = 0
                    elif board[i][k-1] == board[i][k] and not combined:
                        board[i][k-1] *= 2
                        board[i][k] = 0
                        combined = True
    create_number(board)


def move_right(board):
    for i in range(4): # 行
        combined = False
        for j in range(2, -1, -1): # 列
            if board[i][j] != 0:
                for k in range(j, 3): # 列
                    if board[i][k+1] == 0:
                        board[i][k+1] = board[i][k]
                        board[i][k] = 0
                    elif board[i][k+1] == board[i][k] and not combined:
                        board[i][k+1] *= 2
                        board[i][k] = 0
                        combined = True
    create_number(board)
    

def move_up(board):
    for i in range(4): # 列
        combined = False
        for j in range(1, 4): # 行
            if board[j][i] != 0:
                for k in range(j, 0, -1): # 行
                    if board[k-1][i] == 0:
                        board[k-1][i] = board[k][i]
                        board[k][i] = 0
                    elif board[k-1][i] == board[k][i] and not combined:
                        board[k-1][i] *= 2
                        board[k][i] = 0
                        combined = True
    create_number(board)


def move_down(board):
    for i in range(4): # 列
        combined = False
        for j in range(2, -1,  -1): # 行
            if board[j][i] != 0:
                for k in range(j, 3): # 行
                    if board[k+1][i] == 0:
                        board[k+1][i] = board[k][i]
                        board[k][i] = 0
                    elif board[k+1][i] == board[k][i] and not combined:
                        board[k+1][i] *= 2
                        board[k][i] = 0
                        combined = True
    create_number(board)


def check_status(board):
    global inplay
    result = helper.check_board(board)
    if result == -1:
        inplay = False
        print("没有数字可以移动了:(")
    elif result == 1:
        inplay = False
        print("你成功了！")
        

def play():
    global board, inplay
    print(helper.title)
    print(helper.instruction)
    helper.show_board(board)
    while inplay:
        direction = input("按方向键移动数字：")
        if direction == UP:
            move_up(board)
        elif direction == DOWN:
            move_down(board)
        elif direction == LEFT:
            move_left(board)
        elif direction == RIGHT:
            move_right(board)
        helper.show_board(board)
        check_status(board)
        
# 当模块单独运行时，它的 __name__ 属性是 '__main__'
# 因此在模块内写测试代码时均按照下面 if 语句块的方法编写。
if __name__ == '__main__':
    init()
    play()
