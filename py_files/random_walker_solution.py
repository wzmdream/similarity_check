# -*- coding: utf-8 -*-

import simpleguitk as simplegui
import random

## 定义常量
# 画布的尺寸
WIDTH = 400
HEIGHT = 400

# 我们的主角：随机游走圆点的有关常量
CIRCLE_RADIUS = 10
STEP_SIZE = 10
UP, RIGHT, DOWN, LEFT = range(4)
circle_x = WIDTH / 2
circle_y = HEIGHT / 2

# 计数器常量
STEP_COUNTER_POS = [WIDTH - 80, HEIGHT - 360]
step_counter = 0  

# 其它常量
TIME_INTERVAL = 200
point_list = []


def draw(canvas):   
    global step_counter, point_list 
    # 绘制圆点
    canvas.draw_circle([circle_x, circle_y], CIRCLE_RADIUS, 1, "White", "White")
     
    # 绘制计数器
    canvas.draw_text(step_counter, STEP_COUNTER_POS, 20, "White")
            
    # 绘制轨迹
    canvas.draw_polyline(point_list, 2, "Pink")
     

def move():
    # 在这里更新步数和圆点的位置
    global circle_x, circle_y, step_counter
    
    direction = random.randrange(0, 4)
    if direction == UP:
        circle_y -= STEP_SIZE
    elif direction == RIGHT:
        circle_x += STEP_SIZE
    elif direction == DOWN:
        circle_y += STEP_SIZE
    else:
        circle_x -= STEP_SIZE
        
    step_counter += 1
        
    point_list.append([circle_x, circle_y])
    

def reset_program():
    # 恢复常量的初值
    global circle_x, circle_y, step_counter, point_list
    circle_x = WIDTH / 2
    circle_y = HEIGHT / 2
    step_counter = 0
    point_list = []
    point_list.append([circle_x, circle_y])
        

# 创建用户界面
frame = simplegui.create_frame("Random Walker", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.add_button("重新开始", reset_program, 40)

# 创建定时器
timer = simplegui.create_timer(TIME_INTERVAL, move)

# 启动定时器
timer.start()

# 启动用户界面
reset_program()
frame.start()


