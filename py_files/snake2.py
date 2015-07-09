__author__ = 'Administrator'
# -*- coding: utf-8 -*-
import simpleguitk as simplegui
import random

WINDOW_WIDTH = 480
WINDOW_HEIGHT = 400
CELL_SIZE = 20
assert WINDOW_WIDTH % CELL_SIZE == 0, "Window width must be a multiple of cell size."
assert WINDOW_HEIGHT % CELL_SIZE == 0, "Window height must be a multiple of cell size."
CELL_WIDTH = int(WINDOW_WIDTH / CELL_SIZE) #横向方块个数
CELL_HEIGHT = int(WINDOW_HEIGHT / CELL_SIZE)#纵向方块个数

started = False
snake_coords =[]
apple_coord = {}
score = 0
#direction 变量为贪吃蛇 头的方向，默认向右
direction = 'right '
                          # r g b
back_ground = '#A8C39A' #(168,195,154)
def new_game():
    # 游戏开始，贪吃蛇长为3个cell
    global snake_coords, apple_coord,direction,started
    # 贪吃蛇出现的三个初始点
    random.seed()
    start_x = random.randint(5, CELL_WIDTH - 6)
    start_y = random.randint(5, CELL_HEIGHT - 6)
    snake_coords = [{'x': start_x,     'y': start_y},
                  {'x': start_x - 1, 'y': start_y},
                  {'x': start_x - 2, 'y': start_y}]

    # 苹果随机出现的坐标点
    apple_coord = get_apple_location()
    #初始方向朝右
    direction = 'right'

    started = True
    #启动定时器
    timer.start()

def get_apple_location():
    random.seed()
    start_x = random.randint(0, CELL_WIDTH - 1)
    start_y = random.randint(0, CELL_HEIGHT - 1)
    return {'x': start_x, 'y': start_y}

def draw_grid(canvas):
    for x in range(0, WINDOW_WIDTH, CELL_SIZE): # 画方格纵线 0-620
        canvas.draw_line([x, 0],[x, WINDOW_HEIGHT], 1, "White")
    for y in range(0, WINDOW_HEIGHT, CELL_SIZE): # 画方格水平线
       canvas.draw_line([0, y], [WINDOW_WIDTH, y], 1, "White")

def draw_apple(canvas):
    global apple_coord
    x = apple_coord['x'] * CELL_SIZE
    y = apple_coord['y'] * CELL_SIZE
    canvas.draw_polygon([[x, y], [x + CELL_SIZE, y],  [x + CELL_SIZE, y + CELL_SIZE],[x, y + CELL_SIZE]],1, 'red', 'red')

#按键按下事件,改变贪吃蛇的方向
def key_down(key):
    global direction
    #当贪吃蛇方向向右时，点左键无效，只能选择up或者down
    if key == simplegui.KEY_MAP['left'] and direction != 'right':
        direction = 'left'
    elif key == simplegui.KEY_MAP['right'] and direction != 'left':
        direction = 'right'
    elif key == simplegui.KEY_MAP['up'] and direction != 'down':
        direction = 'up'
    elif key == simplegui.KEY_MAP['down'] and direction != 'up':
         direction = 'down'

# 绘制贪吃蛇
def draw_snake(canvas):
    global snake_coords
    # 画蛇，先从头部方块画起，根据一个随机的（x,y）点和cell大小确定其余三个点坐标
    for coord in snake_coords:
        x = coord['x'] * CELL_SIZE
        y = coord['y'] * CELL_SIZE
        #内侧方块
        canvas.draw_polygon([[x, y], [x + CELL_SIZE, y],  [x + CELL_SIZE, y + CELL_SIZE],[x, y + CELL_SIZE]],
                         1, 'teal', 'teal')
        #外侧方块
        canvas.draw_polygon([[x, y+6], [x + CELL_SIZE, y + 6],  [x + CELL_SIZE, y + CELL_SIZE-6],[x, y + CELL_SIZE-6]],
                         1, 'gray', 'gray')
def check_over():
    global snake_coords
     # 判断蛇是否碰到了四周
    if snake_coords[0]['x'] == 0 or snake_coords[0]['x'] == CELL_WIDTH or snake_coords[0]['y'] == 0 or snake_coords[0]['y'] == CELL_HEIGHT:
        return True
    #蛇是否咬到自己
    for snake_body in snake_coords[1:]:
        if snake_body['x'] == snake_coords[0]['x'] and snake_body['y'] == snake_coords[0]['y']:
            return True

    return False
#按钮事件
def click():
    #先结束游戏再重新开始，防止当游戏没有结束时就点击重新开始，定时器没有停止
    game_over()
    new_game()

#按钮事件
def click2():
    global snake_coords
    #先结束游戏再重新开始，防止当游戏没有结束时就点击重新开始，定时器没有停止
    game_over()
    new_game()
    if len(snake_coords) > 5:
        timer._interval = 150
    elif len(snake_coords) > 7:
        timer._interval = 100
    elif len(snake_coords) > 9:
        timer._interval = 70

#按钮事件
def click3():
    #先结束游戏再重新开始，防止当游戏没有结束时就点击重新开始，定时器没有停止
    game_over()
    new_game()
#游戏结束
def game_over():
    global started
    started = False
    timer.stop()

def change_speed():
    global snake_coords
    if len(snake_coords) > 5:
        timer._interval = 150
    elif len(snake_coords) > 7:
        timer._interval = 100
    elif len(snake_coords) > 9:
        timer._interval = 70
#贪吃蛇在屏幕内前进
def move():
    global direction,snake_coords,apple_coord, score

    if direction == 'up':
        new_head = {'x': snake_coords[0]['x'], 'y': snake_coords[0]['y'] - 1}
    elif direction == 'down':
        new_head = {'x': snake_coords[0]['x'], 'y': snake_coords[0]['y'] + 1}
    elif direction == 'left':
       new_head = {'x': snake_coords[0]['x'] - 1, 'y': snake_coords[0]['y']}
    elif direction == 'right':
       new_head = {'x': snake_coords[0]['x'] + 1, 'y': snake_coords[0]['y']}

    #新点插入
    snake_coords.insert(0, new_head)

    if snake_coords[0]['x'] == apple_coord['x'] and snake_coords[0]['y'] == apple_coord['y']:
        # 如果蛇吃了苹果，重新生成一个苹果
        #吃掉一个，加10分
        score = score + 10
        apple_coord = get_apple_location()
    else:
        #否则，删除贪吃蛇最后一节
        #del snake_coords[-1]
        snake_coords.pop()

    change_speed()
    #判断游戏是否结束
    if check_over():
        game_over()

def draw(canvas):
    global snake_coords,apple_coord, score, started
    # 绘制方格，蛇和苹果
    draw_grid(canvas)
    draw_snake(canvas)
    draw_apple(canvas)

    label.set_text("得分:"+str(score))
    if not started:
        canvas.draw_text("游戏结束",[100, 200], 60,"blue")

# 创建frame，设置背景色
frame = simplegui.create_frame("贪吃蛇", WINDOW_WIDTH, WINDOW_HEIGHT)
frame.set_canvas_background(back_ground)

#添加按钮和label
label = frame.add_label("得分:" + str(score))
frame.add_button("难度一",click,50)
frame.add_button("难度二",click2,50)
frame.add_button("难度三",click3,50)
#添加句柄事件
frame.set_draw_handler(draw)
frame.set_keydown_handler(key_down)

#创建定时器
timer = simplegui.create_timer(200,move)

# 开始游戏
new_game()
frame.start()
