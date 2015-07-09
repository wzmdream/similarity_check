title = r"""
 ___________   ________    _____
/_   \   _  \  \_____  \  /  |  |
 |   /  /_\  \  /  ____/ /   |  |_
 |   \  \_/   \/       \/    ^   /
 |___|\_____  /\_______ \____   |
            \/         \/    |__|

"""

instruction = """
游戏说明：
1. 按上、下、左、右方向键，数字沿该方向移动到棋盘一侧。
2. 在该方向上如果有相同的一对数字，这对数字就会相加合并为新的数字。
3. 产生数字1024就算胜利，当棋盘满了并且没有数字可以合并时游戏失败。
"""

c2 = r"""
 ___  
|_  ) 
 / /  
/___| 
"""

c4 = r"""
 _ _  
| | | 
|_  _|
  |_| 
"""

c8 = r"""
 ___ 
( _ )
/ _ \
\___/
 """

c16 = r"""
 _  __ 
/ |/ / 
| / _ \
|_\___/
"""

c32 = r"""
 _______ 
|__ /_  )
 |_ \/ / 
|___/___|
"""

c64 = r"""
  __ _ _ 
 / /| | | 
/ _ \_  _|
\___/ |_| 
 """

c128 = r"""
 _ ___ ___ 
/ |_  | _ )
| |/ // _ \
|_/___\___/
"""

c256 = r"""
 ___ ___   __ 
|_  ) __| / / 
 / /|__ \/ _ \
/___|___/\___/
"""

c512 = r"""
 ___ _ ___ 
| __/ |_  )
|__ \ |/ / 
|___/_/___|
"""

c1024 = r"""
 _  __ ___ _ _  
/ |/  \_  ) | | 
| | () / /|_  _|
|_|\__/___| |_| 
"""

number_pic = {2:c2.split(sep='\n'), 4:c4.split(sep='\n'), 8:c8.split(sep='\n'),
              16:c16.split(sep='\n'), 32:c32.split(sep='\n'), 64:c64.split(sep='\n'),
              128:c128.split(sep='\n'), 256:c256.split(sep='\n'), 512:c512.split(sep='\n'),
              1024:c1024.split(sep='\n')}
              
def show_board(board):
    # 根据最大的数字调整棋盘尺寸
    max_num = max(max(board))
    size = 10 # 默认值
    if max_num in (2, 8):
        size = 10
    elif max_num == 4:
        size = 11
    elif max_num == 16:
        size = 12
    elif max_num == 32:
        size = 14
    elif max_num == 64:
        size = 15
    elif max_num in (128, 512):
        size = 16
    elif max_num == 256:
        size = 19
    elif max_num == 1024:
        size = 21
        
    for i in range(4):
        print('_'*(size*4+5))
        for j in range(4):
            print('|', end='')
            for k in range(4):
                if board[i][k] == 0:
                    print(' '*size, end='')
                else:
                    line = number_pic[board[i][k]][j+1]
                    print("{0:^{1}}".format(line, size), end='')
                print('|', end='')
            print()
    print('_'*(size*4+5))
        
def check_board(board):
    # 返回值的含义———— -1:游戏失败, 0:棋盘未满或者有可合并的数字, 1:游戏胜利
    # 注意下面三组循环的顺序
    
    for i in range(4):  # 检查胜利条件
        for j in range(4):
            if board[i][j] == 1024:
                return 1
            
    for i in range(4): # 检查棋盘有无空位
        for j in range(4):
            if board[i][j] == 0:
                return 0

    for i in range(4): # 检查棋盘有没有可以合并的数字
        for j in range(4):
            if i-1 >= 0 and board[i-1][j] == board[i][j]: # 和上边比（注意检查列表边界）
                return 0
            elif i+1 < 4 and board[i+1][j] == board[i][j]: # 和下边比
                return 0
            elif j-1 >= 0 and board[i][j-1] == board[i][j]: # 和左边比
                return 0
            elif j+1 < 4 and board[i][j+1] == board[i][j]: # 和右边比
                return 0
    # 能够执行到这里说明没有达到1024，并且棋盘已满
    return -1

