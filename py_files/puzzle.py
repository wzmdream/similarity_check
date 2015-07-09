'''
Created on 2014年7月15日

@author: Administrator
说明：智力拼图
    主要练习：1.random模块生成随机数方法
        2.if-elif-else语句
        3.list创建遍历方法
        4.创建frame的方法
        5.添加按钮
        6.函数调用方法
        7、鼠标单击事件驱动
        8. 画布添加文字、画多边形方法
        
'''

import simpleguitk as simplegui
import  random

# 定义全局变量
board_col = 4 #游戏面板的列数
board_row = 4 #游戏面板的行数

#空白块
BLANK = None
#顺序打乱的游戏面板数组
puzzle_board = []
#顺序正确的
starting_board = []
#玩家游戏所用的步数
step = 0

#初始化游戏面板
def getStartingBoard():
    global starting_board  
    counter = 1
    starting_board = []
    for x in range(board_col):
        column = []
        for y in range(board_row):
            column.append(counter)
            counter += board_col
        starting_board.append(column)
        counter -= board_col * (board_row - 1) + board_col - 1

    starting_board[board_col-1][board_row-1] = BLANK

#生成随机打乱的游戏面板
def getPuzzleBoard():
    global puzzle_board       
    random.seed()
   
    counter = 1
    puzzle_board = []
    for x in range(board_col):
        column = []
        for y in range(board_row):
            column.append(counter)
            counter += board_col
            random.shuffle(column)
        puzzle_board.append(column)
        counter -= board_col * (board_row - 1) + board_col - 1

    x = random.randint(0,3)
    y = random.randint(0,3)
    
    for i in range(board_col):
        for j in range(board_row):         
            if puzzle_board[i][j] == 16:
                puzzle_board[i][j] = puzzle_board[x][y]
                puzzle_board[x][y] = BLANK

    random.shuffle(puzzle_board)
#画图句柄事件    
def draw(canvas):
    global puzzle_board , step 

    for i in range(board_col):
        for j in range(board_row):  
            canvas.draw_polygon([[80+80*i, 80 + 80*j],[80 + 80*(i+1), 80 + (j)*80], [80 + 80*(i+1), 80 + (j+1)*80], [80 + 80*(i), 80 + (j+1)*80]], 2, "black", "Green")
            if puzzle_board[i][j] != BLANK:
                
                canvas.draw_text(str(puzzle_board[i][j]),[100 + 80 * i,140 + 80 * j],30,"White")
            else:
                canvas.draw_polygon([[80+80*i, 80 + 80*j],[80 + 80*(i+1), 80 + (j)*80], [80 + 80*(i+1), 80 + (j+1)*80], [80 + 80*(i), 80 + (j+1)*80]], 2, "black", "black")

    canvas.draw_text("step:"+str(step),[50, 60],20,"white") 
    
    if puzzle_board == starting_board :
        canvas.draw_text("恭喜你！",[230, 60],20,"red") 
# 开始游戏
def new_game():
    global step 
    step = 0
    getPuzzleBoard()
    getStartingBoard()
    
# 鼠标点击事件
def mouseclick(pos):
    global puzzle_board,step
    #数字位置
    spot_x = ( pos[0] - 80 ) // 80
    spot_y = ( pos[1] - 80 ) // 80
    #鼠标点击在面板范围内有效
    if  spot_x >=0  and spot_x < 4 and spot_y >=0 and spot_y < 4 :      
        tmp = puzzle_board[spot_x][spot_y]
        #判断该点的哪个方向是black
        if (spot_y - 1) >= 0 and puzzle_board[spot_x][spot_y - 1] == BLANK :
            puzzle_board[spot_x][spot_y] = puzzle_board[spot_x][spot_y - 1]
            puzzle_board[spot_x ][spot_y- 1] = tmp 
            step = step + 1     
        elif (spot_y + 1) < 4 and puzzle_board[spot_x][spot_y + 1] == BLANK :
            puzzle_board[spot_x][spot_y] = puzzle_board[spot_x][spot_y + 1] 
            puzzle_board[spot_x][spot_y + 1]  = tmp 
            step = step + 1
        elif (spot_x - 1) >= 0 and puzzle_board[spot_x-1][spot_y] == BLANK :
            puzzle_board[spot_x][spot_y] = puzzle_board[spot_x-1][spot_y]
            puzzle_board[spot_x -1][spot_y]  = tmp 
            step = step + 1
        elif (spot_x + 1) < 4 and puzzle_board[spot_x + 1][spot_y] == BLANK :
            puzzle_board[spot_x][spot_y] = puzzle_board[spot_x + 1][spot_y]
            puzzle_board[spot_x +1][spot_y]  = tmp 
            step = step + 1

# 创建frame
frame = simplegui.create_frame("智力拼图", 500, 500)
#设置背景画布颜色
frame.set_canvas_background("gray")
#添加按钮
frame.add_button("重新开始", new_game, 100)

# 注册鼠标事件和画图事件
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

#开始
new_game()
#启动frame
frame.start()

