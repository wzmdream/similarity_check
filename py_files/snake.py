# -*- coding: utf-8 -*-
import simpleguitk as simplegui
import random

## 定义常量
WIDTH = 600     # 画布的尺寸
HEIGHT = 600
STEP = 20       # 移动步长
COLS = WIDTH / STEP     # 方阵的列数
ROWS = HEIGHT / STEP    # 方阵的行数
UP, DOWN, LEFT, RIGHT = range(4)

snake = None
bean = None
direction = LEFT   # 初始方向向左
score = 0
gameover = False
time_interval = 200 # 定时器定时值：200毫秒
timer = None        # timer 将在 play 函数里创建


# 贪吃蛇在程序里用一个列表表示
# 该列表的操作规则遵循队列的操作规则
def create_snake():
    return [[COLS/2, ROWS/2], [COLS/2 + 1, ROWS/2], [COLS/2 + 2, ROWS/2], [COLS/2 + 3, ROWS/2]]
    

# 根据身体在方阵上的坐标计算正方形四个顶点的坐标
def build_body(body_pos):
    return [[body_pos[0]*STEP, body_pos[1]*STEP], 
             [body_pos[0]*STEP+STEP, body_pos[1]*STEP], 
             [body_pos[0]*STEP+STEP, body_pos[1]*STEP+STEP],
             [body_pos[0]*STEP, body_pos[1]*STEP+STEP]]
             

# 在一个随机位置生成一个豆子
# 理解 in 运算符。
# 你在编写其它函数时，需要用它检验一个元素是否在一个列表里
def create_bean():   
    while True:
        x = random.randrange(COLS)
        y = random.randrange(ROWS)
        if [x, y] not in snake:
            return [x, y]


# 绘制贪吃蛇、豆子和得分
def draw(canvas):
    pass
    

# 初始化全局变量
def play():
    global snake, bean, direction, gameover, score, time_interval, timer
    # 如果有正在运行的定时器，需要先把它停下
    if timer is not None and timer.is_running():
        timer.stop() 
    # 创建定时器
    timer = simplegui.create_timer(time_interval, move)
    timer.start()
    
    # 代码写在下面
    pass  


# 根据按键调整蛇头的朝向
def keydown(key):
    global direction
    pass  
        

# 移动贪吃蛇：即操作snake这个列表
# 还需要检验是否吃到豆子和游戏的结束条件        
def move():
    global snake, bean, direction, gameover, score, time_interval, timer
    pass
       
    
# 创建用户界面
frame = simplegui.create_frame("贪吃蛇", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)

# 创建按钮
frame.add_button("开始游戏", play, 80)

# 启动游戏
play()
frame.start()
