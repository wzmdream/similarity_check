# -*- coding: utf-8 -*-
import random
import helper

# 棋盘用二维列表表示。空白用 0 表示
board = [[0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0]]
         
UP, DOWN, LEFT, RIGHT = ('w', 's', 'a', 'd')

inplay = True

# 随机在棋盘空白位置产生新的数字
def create_number(board):
    has_gap = False
    # 检查棋盘有无空位
    for i in range(4): 
        for j in range(4):
            if board[i][j] == 0:
                has_gap = True
                break
    # 有空位才创建新的数字
    while has_gap:
        row = random.randrange(0, 4)
        col = random.randrange(0, 4)
        if board[row][col] == 0:
            board[row][col] = 2 # 初始数字是 2
            return


# 向左移动数字。读懂这个函数，写出其它移动数字的函数就容易多了。
def move_left(board):
    for i in range(4): # 遍历每一行
        combined = False
        for j in range(1, 4): # 从第二列开始
            if board[i][j] != 0:
                for k in range(j, 0, -1): # 从第j列往前依次判断
                    if board[i][k-1] == 0: # 如果是空白，就移动数字
                        board[i][k-1] = board[i][k]
                        board[i][k] = 0
                    # 如果是相同的数字就合并。只能合并一次用 combined 标志来控制
                    elif board[i][k-1] == board[i][k] and not combined:
                        board[i][k-1] *= 2
                        board[i][k] = 0
                        combined = True
    create_number(board) # 数字移动后要创建新的数字


# 向右移动数字
def move_right(board):
    pass
    

# 向上移动数字
def move_up(board):
    pass


# 向下移动数字
def move_down(board):
    pass


# 检查棋盘，判断输赢
def check_status(board):
    global inplay
    # 利用 helper.check_board
    pass

        
# 初始化棋盘
def init():
    # 在棋盘上产生三个数字
    pass


# 控制游戏的进程
def play():
    global board, inplay
    print(helper.title)
    print(helper.instruction)
    helper.show_board(board)
    while inplay:
        # 根据玩家输入的方向移动棋盘。移动后要用 check_board 检查棋盘。
        pass
        
        
# 当模块单独运行时，它的 __name__ 属性是 '__main__'
# 因此在模块内写测试代码时均按照下面 if 语句块的方法编写。
if __name__ == '__main__':
    # 程序从这里开始
    init()
    play()
