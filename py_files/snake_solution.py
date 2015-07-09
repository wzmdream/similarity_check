# -*- coding: utf-8 -*-
import simpleguitk as simplegui
import random

## 定义常量
# 画布的尺寸
WIDTH = 600
HEIGHT = 600
STEP = 20
COLS = WIDTH / STEP
ROWS = HEIGHT / STEP
UP, DOWN, LEFT, RIGHT = range(4)

snake = None
bean = None
direction = LEFT   # 初始方向向右
score = 0
gameover = False
time_interval = 200 # 定时器定时值：200毫秒
timer = None        # timer 将在 play 函数里创建
        
def create_snake():
    return [[COLS/2, ROWS/2], [COLS/2 + 1, ROWS/2], [COLS/2 + 2, ROWS/2], [COLS/2 + 3, ROWS/2]]
    

def build_body(body_pos):
    return [[body_pos[0]*STEP, body_pos[1]*STEP], 
             [body_pos[0]*STEP+STEP, body_pos[1]*STEP], 
             [body_pos[0]*STEP+STEP, body_pos[1]*STEP+STEP],
             [body_pos[0]*STEP, body_pos[1]*STEP+STEP]]
             

def create_bean():   
    while True:
        x = random.randrange(COLS)
        y = random.randrange(ROWS)
        if [x, y] not in snake:
            return [x, y]


# 绘制画布
def draw(canvas):
    if snake is not None and bean is not None:
        bean_body = build_body(bean)
        canvas.draw_polygon(bean_body, 1, 'Yellow', 'Yellow')
        
        for body_pos in snake:
            body = build_body(body_pos)
            canvas.draw_polygon(body, 1, 'Green', 'Green')
            
    canvas.draw_text('得分：'+str(score), [20, 40], 20, 'White')
    
def play():
    global snake, bean, direction, gameover, score, time_interval, timer
    # 如果有正在运行的定时器，需要先把它停下
    if timer is not None and timer.is_running():
        timer.stop() 
    # 创建定时器
    timer = simplegui.create_timer(time_interval, move)
    timer.start()
    
    snake = create_snake()
    bean = create_bean()
    direction = LEFT
    score = 0
    gameover = False
    time_interval = 200  


def keydown(key):
    global direction
    if key == simplegui.KEY_MAP['up']:
        if direction == DOWN:
            return
        direction = UP
    if key == simplegui.KEY_MAP['left']:
        if direction == RIGHT:
            return
        direction = LEFT
    if key == simplegui.KEY_MAP['right']:
        if direction == LEFT:
            return
        direction = RIGHT
    if key == simplegui.KEY_MAP['down']:
        if direction == UP:
            return
        direction = DOWN  
        
        
def move():
    global snake, bean, direction, gameover, score, time_interval, timer
    if not gameover:
        if direction == RIGHT:
            head = [snake[0][0]+1, snake[0][1]]
        elif direction == UP:
            head = [snake[0][0], snake[0][1]-1]
        elif direction == LEFT:
            head = [snake[0][0]-1, snake[0][1]]
        elif direction == DOWN:
            head = [snake[0][0], snake[0][1]+1]
        # 检查游戏结束条件    
        if head[0] >= COLS or head[0] < 0 or head[1] >= ROWS or head[1] < 0 or (head in snake):
            gameover = True
            return
        
        snake.insert(0, head)   
        tail = snake.pop()
        if bean in snake: # 如果吃到豆子
            bean = create_bean()
            snake.append(tail)
            score += 1    
            if score > 0 and score % 5 == 0 and time_interval > 50:
                simplegui.timers.destroy() # 先销毁原有 timer，再创建新的 timer
                time_interval /= 1.2
                timer = simplegui.create_timer(time_interval, move)    
                timer.start()
       
    
# 创建用户界面
frame = simplegui.create_frame("贪吃蛇", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)

# 创建按钮
frame.add_button("开始游戏", play, 80)

# 启动游戏
play()
frame.start()
