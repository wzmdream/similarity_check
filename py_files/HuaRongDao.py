# -*- coding: utf-8 -*-
"""
请在此处完善你个人的信息
学院：
班级：
学号：
姓名：
"""
# 华容道

import simpleguitk as simplegui

# 全局变量
canvas_height = 500  # 画布高度，单位为像素
canvas_width = 400  # 画布宽度，单位为像素
game_over = False  # 游戏是否结束
figure_moving = False # 是否有运动的人物
all_figure = {}  # 所有人物
steps = 0  # 移动步数
current_figure = None  # 鼠标点中的人物
current_center = []    # 鼠标点中人物的中心坐标
original_point = []    # 鼠标点击的初始位置坐标
speed = 4              # 人物移动的速度
machao_image = simplegui.load_image('images/马超.png')
zhangfei_image = simplegui.load_image('images/张飞.png')
zhaoyun_image = simplegui.load_image('images/赵云.png')
huangzhong_image = simplegui.load_image('images/黄忠.png')
guanyu_image = simplegui.load_image('images/关羽.png')
caocao_image = simplegui.load_image('images/曹操.png')
soldier_image = simplegui.load_image('images/士兵.png')

# 绘制全部人物
def draw_all_figure(all_figure, canvas):
    for figure in all_figure.values():
        figure.draw(canvas)

# 检查移动人物与其它人物及边界的碰撞
def check_collide():
    global game_over
    if current_figure.get_dest_center()[0] == 200 and current_figure.get_dest_center()[1] == 400: # 曹操到达逃出位置
        current_figure.set_move_direction("down")
    else:
        for figure in all_figure.values():
            if figure != current_figure:
                current_figure.collide(figure)
    if current_figure.get_dest_center()[1] > 600:  # 曹操已经消失
        game_over = True

# 绘制游戏结束信息
def draw_game_over_msg(canvas, msg):
    msgwidth = frame.get_canvas_textwidth(msg, 48, 'sans-serif')
    canvas.draw_text(msg, ((canvas_width - msgwidth) / 2, canvas_height / 2), 48, 'Red', 'sans-serif')


# Figure类（人物类）
class Figure:
    def __init__(self, image, src_center, src_size, dest_center, dest_size):
        self.image = image
        self.src_center = src_center
        self.src_size = src_size
        self.dest_center = dest_center
        self.dest_size = dest_size
        self.move_direction = None

    def get_dest_center(self):
        return self.dest_center
    def get_dest_size(self):
        return self.dest_size
    def set_move_direction(self, direction):
        self.move_direction = direction
    def collide(self, other):
        global figure_moving, steps
        if self.move_direction == 'left':
            self_left = self.dest_center[0] - self.dest_size[0] / 2
            other_right = other.get_dest_center()[0] + other.get_dest_size()[0] / 2
            self_top = self.dest_center[1] - self.dest_size[1] / 2
            self_bottom = self.dest_center[1] + self.dest_size[1] / 2
            other_top = other.get_dest_center()[1] - other.get_dest_size()[1] / 2
            other_bottom = other.get_dest_center()[1] + other.get_dest_size()[1] / 2
            if (self_left == other_right and self_bottom > other_top and self_top < other_bottom) or self_left == 0:
                steps += 1
                self.move_direction = None
                figure_moving = False
        elif self.move_direction == 'right':
            self_right = self.dest_center[0] + self.dest_size[0] / 2
            other_left = other.get_dest_center()[0] - other.get_dest_size()[0] / 2
            self_top = self.dest_center[1] - self.dest_size[1] / 2
            self_bottom = self.dest_center[1] + self.dest_size[1] / 2
            other_top = other.get_dest_center()[1] - other.get_dest_size()[1] / 2
            other_bottom = other.get_dest_center()[1] + other.get_dest_size()[1] / 2
            if (self_right == other_left and self_bottom > other_top and self_top < other_bottom) or self_right == canvas_width:
                steps += 1
                self.move_direction = None
                figure_moving = False
        elif self.move_direction == 'up':
            self_top = self.dest_center[1] - self.dest_size[1] / 2
            other_bottom = other.get_dest_center()[1] + other.get_dest_size()[1] / 2
            self_left = self.dest_center[0] - self.dest_size[0] / 2
            self_right = self.dest_center[0] + self.dest_size[0] / 2
            other_left = other.get_dest_center()[0] - other.get_dest_size()[0] / 2
            other_right = other.get_dest_center()[0] + other.get_dest_size()[0] / 2
            if (self_top == other_bottom and self_right > other_left and self_left < other_right) or self_top == 0:
                steps += 1
                self.move_direction = None
                figure_moving = False
        elif self.move_direction == 'down':
            self_bottom = self.dest_center[1] + self.dest_size[1] / 2
            other_top = other.get_dest_center()[1] - other.get_dest_size()[1] / 2
            self_left = self.dest_center[0] - self.dest_size[0] / 2
            self_right = self.dest_center[0] + self.dest_size[0] / 2
            other_left = other.get_dest_center()[0] - other.get_dest_size()[0] / 2
            other_right = other.get_dest_center()[0] + other.get_dest_size()[0] / 2
            if (self_bottom == other_top and self_right > other_left and self_left < other_right) or self_bottom == canvas_height:
                steps += 1
                self.move_direction = None
                figure_moving = False
        label_text = "移动次数 = " + str(steps) + " 步"
        label.set_text(label_text)
    def draw(self, canvas):
        canvas.draw_image(self.image, self.src_center, self.src_size, self.dest_center, self.dest_size)

    def update(self):
        if self.move_direction == 'left':
            self.dest_center[0] = self.dest_center[0] - speed
        elif self.move_direction == 'right':
            self.dest_center[0] = self.dest_center[0] + speed
        elif self.move_direction == 'up':
            self.dest_center[1] = self.dest_center[1] - speed
        elif self.move_direction == 'down':
            self.dest_center[1] = self.dest_center[1] + speed

# 鼠标点击事件的处理函数
def mouseclick(pos):
    global current_figure, current_center, original_point
    if not figure_moving:
        for key, figure in all_figure.items():
            center = figure.get_dest_center()
            size = figure.get_dest_size()
            if pos[0] >= center[0] - size[0] / 2 and pos[0] <= center[0] + size[0] / 2 and pos[1] >= center[1] - size[
                1] / 2 and pos[1] <= center[1] + size[1] / 2:
                current_figure = figure
                current_center = figure.get_dest_center()
                original_point = pos

# 鼠标拖动事件的处理函数
def mousedrag(pos):
    global current_figure, current_center, original_point, figure_moving
    if current_figure != None:
        horizontal_move = pos[0] - original_point[0]
        vertical_move = pos[1] - original_point[1]
        figure_moving = True
        if abs(horizontal_move) > abs(vertical_move):
            if horizontal_move > 0:
                current_figure.set_move_direction("right")
            else:
                current_figure.set_move_direction("left")
        else:
            if vertical_move > 0:
                current_figure.set_move_direction("down")
            else:
                current_figure.set_move_direction("up")

# 屏幕刷新事件处理函数
def draw(canvas):
    if game_over:
        draw_game_over_msg(canvas, '通关成功')
    else:
        check_collide()
        draw_all_figure(all_figure, canvas)
        current_figure.update()


# 为游戏开始或重新开始初始化全局变量，也是鼠标点击按钮的事件处理函数
def start_game():
    global steps, all_figure, game_over,current_figure, figure_moving
    figure_moving = False
    steps = 0
    all_figure = {}
    all_figure['马超'] = Figure(machao_image, [50, 100], [100, 200], [50, 100], [100, 200])
    all_figure['曹操'] = Figure(caocao_image, [100, 100], [200, 200], [200, 100], [200, 200])
    all_figure['张飞'] = Figure(zhangfei_image, [50, 100], [100, 200], [350, 100], [100, 200])
    all_figure['赵云'] = Figure(zhaoyun_image, [50, 100], [100, 200], [50, 300], [100, 200])
    all_figure['关羽'] = Figure(guanyu_image, [100, 50], [200, 100], [200, 250], [200, 100])
    all_figure['黄忠'] = Figure(huangzhong_image, [50, 100], [100, 200], [350, 300], [100, 200])
    all_figure['士兵1'] = Figure(soldier_image, [50, 50], [100, 100], [150, 350], [100, 100])
    all_figure['士兵2'] = Figure(soldier_image, [50, 50], [100, 100], [250, 350], [100, 100])
    current_figure = Figure(soldier_image, [50, 50], [100, 100], [50, 450], [100, 100])
    all_figure['士兵3'] = current_figure
    all_figure['士兵4'] = Figure(soldier_image, [50, 50], [100, 100], [350, 450], [100, 100])
    game_over = False
    label.set_text("移动次数 = 0 步")


# 创建窗口初始化画布
frame = simplegui.create_frame("华容道之横刀立马", canvas_width, canvas_height)
label = frame.add_label("移动次数 = 0 步")

# 注册事件处理函数
frame.set_draw_handler(draw)  # 显示处理，每秒调用draw函数60次
button = frame.add_button('重新开始游戏', start_game, 100)  # 鼠标每次点击“重新开始游戏”按钮，调用start_game函数1次
frame.set_mouseclick_handler(mouseclick)  #
frame.set_mousedrag_handler(mousedrag)

# 启动游戏
start_game()  # 为游戏开始或重新开始初始化全局变量
frame.start()  # 显示窗口