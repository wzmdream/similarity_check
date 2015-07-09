# -*- coding: utf-8 -*-
"""
请在此处完善你个人的信息
学院：
班级：
学号：
姓名：
"""
# 决战三字经

import simpleguitk as simplegui
import random
import copy

# 全局变量
has_rising_box = True                 # 是否有文字块正在上升
canvas_height = 600                   # 画布高度，单位为像素
canvas_width = 480                    # 画布宽度，单位为像素
box_height = 30                       # 文字块高度，单位为像素
box_width = 120                       # 文字块宽度，单位为像素，包含3个汉字
rising_speed = -1                     # 上升速度，单位为像素
horizontal_move_distance = box_width  # 按左右箭头键时，水平移动的距离，单位为像素
game_over = False                     # 游戏是否结束
rising_box = None                     # 正在运动的文字块对象
stopped_box = set([])                 # 停止移动的文字块
prime_sentence_list = []              # 三字经全文列表，每句为一个列表元素
current_section_list = []             # 当前处理的段落文字列表，每句为一个列表元素，4句为一个段落
last_four_box = []                    # 最近的4个文字块对象列表
score = 0                             # 游戏得分

# 从文本文件读入三字经，存储在列表中，并返回该列表,三字经文件的格式如下
'''
rén zhī chū    xìng běn shàn    xìng xiāng jìn    xí xiāng yuǎn
人之初    性本善    性相近    习相远
gǒu bú jiào    xìng nǎi qiān    jiào zhī dào    guì yǐ zhuān
苟不教    性乃迁    教之道    贵以专
xī mèng mǔ    zé lín chǔ    zǐ bù xué    duàn jī zhù
昔孟母    择邻处    子不学    断机杼
dòu yān shān    yǒu yì fāng    jiāo wǔ zǐ    míng jù yáng
窦燕山    有义方    教五子    名俱扬
yǎng bú jiào    fù zhī guò     jiào bù yán    shī zhī duò
养不教    父之过    教不严    师之惰
......
'''
def read_from_file(filename):
    # 奇数行为诗句拼音，偶数行为诗句文本
    # 三字经每3个汉字为1句，每1句作为列表的1个元素，四句为一行（一段），句间隔为空格
    prime_list = []
    input_file = open(filename, encoding='utf-8')
    i = 1
    for line in input_file.readlines():
        if i % 2 == 0:
            line_list = line.split()
            for sentence in line_list:
                prime_list.append(sentence)
        i = i + 1
    input_file.close()
    return prime_list
print(read_from_file('三字经.txt'))
print(read_from_file ('三字经.txt')[0])
print(read_from_file ('三字经.txt')[491])
text = read_from_file ('三字经.txt')
for t in text:
    print(t)

def text_shuffle(text):
        tmp_list = list(text)
        random.shuffle(tmp_list)
        return ''.join(tmp_list)
print(text_shuffle ('人之初'))

def draw_all_stopped_box(stopped_box,canvas):
    for box in stopped_box:
        box.draw(canvas)

# 生成当前段落四句诗歌列表
def generate_current_section_list():
    tmp_list = []
    for i in range(4):
        tmpstr = str(i) + prime_sentence_list.pop(0)
        tmp_list.append(tmpstr)
        random.shuffle(tmp_list)
    return tmp_list
prime_sentence_list = read_from_file('三字经.txt')
print(generate_current_section_list())
print(generate_current_section_list())
print(generate_current_section_list())


def check_collision(group, moving_box):
    for box in group:
        if box.collide(moving_box):
            return True
    return False

def stop_box(group, moving_box):
    global has_rising_box, game_over,score, label, last_four_box
    if moving_box.get_processed():
        return
    if moving_box.get_pos()[1] == 0 or check_collision(group, moving_box):
        moving_box.set_rising(False)
        stopped_box = copy.deepcopy(moving_box)
        if stopped_box.get_sentence() == stopped_box.get_correct_sentence():
            score += 5
            label_text = "游戏得分 = " + str(score) + "分"
            label.set_text(label_text)
        if (int(stopped_box.get_pos()[0] / box_width)) != stopped_box.get_order():
            stopped_box.set_proper_order(False)
        group.add(stopped_box)

        moving_box.set_processed()
        box_size = len(group)
        last_section_fine = False
        if box_size % 4 ==1:
            last_four_box.clear()
        last_four_box.append(stopped_box)
        if box_size % 4 ==0:
            if (last_four_box[0].get_proper_order()
                 and last_four_box[0].get_sentence() == last_four_box[0].get_correct_sentence()
                 and last_four_box[1].get_proper_order()
                 and last_four_box[1].get_sentence() == last_four_box[1].get_correct_sentence()
                 and last_four_box[2].get_proper_order()
                 and last_four_box[2].get_sentence() == last_four_box[2].get_correct_sentence()
                 and last_four_box[3].get_proper_order()
                 and last_four_box[3].get_sentence() == last_four_box[3].get_correct_sentence()) :
                score += 20
                label_text = "游戏得分 = " + str(score) + "分"
                label.set_text(label_text)
                last_section_fine = True
        if last_section_fine:
            for box in last_four_box:
                group.discard(box)

        line_index = (stopped_box.get_pos()[1] + 15) // box_height
        if line_index >= 10:
            game_over = True
        else:
            has_rising_box = False

# 绘制游戏结束信息
def draw_game_over_msg(canvas, msg):
    msgwidth = frame.get_canvas_textwidth(msg, 48, 'sans-serif')
    canvas.draw_text(msg, ((canvas_width - msgwidth) / 2, canvas_height / 2), 48, 'Red', 'sans-serif')

# Box类
class Box:
    def __init__(self, pos, width, height, sentence, correct_sentence, order):
        self.pos = [pos[0],pos[1]]
        self.width = width
        self.height = height
        self.sentence = sentence
        self.correct_sentence = correct_sentence
        self.rising = True
        self.processed = False
        self.order = order
        self.proper_order = True

    def set_processed(self):
        self.processed = True
    def get_processed(self):
        return self.processed
    def set_proper_order(self, is_proper_order):
        self.proper_order = is_proper_order
    def get_proper_order(self):
        return self.proper_order
    def get_order(self):
        return self.order
    def set_rising(self, is_rising):
        self.rising = is_rising
    def get_sentence(self):
        return self.sentence
    def get_correct_sentence(self):
        return self.correct_sentence
    def get_pos(self):
        return self.pos
    def set_pos(self, new_pos):
        self.pos = new_pos

    def shuffle_sentence(self):
        self.sentence = text_shuffle(self.sentence)

    def collide(self,moving_object):
        if (self.pos[1]) + self.height == moving_object.get_pos()[1] and self.pos[0] == moving_object.get_pos()[0]:
            return True
        else:
            return False

    def draw(self, canvas):
        text_width = frame.get_canvas_textwidth(self.sentence, 24, 'sans-serif')
        if self.sentence == self.correct_sentence and self.proper_order:
            canvas.draw_polygon([self.pos, [self.pos[0] + self.width, self.pos[1]], [self.pos[0] + self.width, self.pos[1] + self.height], [self.pos[0], self.pos[1] + self.height]], 2, 'Green', 'Green')
            canvas.draw_text(self.sentence, (self.pos[0] + (self.width - text_width) / 2, self.pos[1] + self.height - 2), 24, 'White', 'sans-serif')
        else:
            canvas.draw_polygon([self.pos, [self.pos[0] + self.width, self.pos[1]], [self.pos[0] + self.width, self.pos[1] + self.height], [self.pos[0], self.pos[1] + self.height]], 2, 'Red', 'Red')
            canvas.draw_text(self.sentence, (self.pos[0] + (self.width - text_width) / 2, self.pos[1] + self.height - 2), 24, 'Yellow', 'sans-serif')
    def update(self):
        if self.rising == True:
            self.pos[1] += rising_speed

test_box = Box([120,100], box_width, box_height, '人之初', '之人初', 0)
print(test_box.get_pos())
print(test_box.get_sentence())
print(test_box.get_correct_sentence())
print(test_box.get_order())
print(test_box.get_processed())
test_box.shuffle_sentence()
print(test_box.get_sentence())

# 时钟事件处理函数，生产一个上升的方块
def box_spawner():
    global has_rising_box,rising_box,current_section_list,game_over

    if game_over:
        return
    if not has_rising_box:
        if len(current_section_list) == 0:
            current_section_list = generate_current_section_list()
        sentence = current_section_list.pop()
        random_pos = [random.randrange(4) * box_width,canvas_height]
        rising_box = Box(random_pos, box_width, box_height, text_shuffle(sentence[1:]), sentence[1:], int(sentence[0]))

    has_rising_box = True


# 屏幕刷新事件处理函数
def draw(canvas):
    if game_over:
        draw_game_over_msg(canvas,'游戏结束！')
    else:
        rising_box.draw(canvas)
        rising_box.update()
        draw_all_stopped_box(stopped_box, canvas)
        stop_box(stopped_box,rising_box)

# 处理键盘按下事件的函数
def keydown(key):
    if not game_over:
        if key == simplegui.KEY_MAP["left"]:    # 向左移动方块
            if rising_box.get_pos()[0] - horizontal_move_distance >= 0:
                rising_box.set_pos([rising_box.get_pos()[0] - horizontal_move_distance,rising_box.get_pos()[1]])
        elif key == simplegui.KEY_MAP["right"]: # 向右移动方块
            if rising_box.get_pos()[0] + box_width + horizontal_move_distance <= canvas_width:
                rising_box.set_pos([rising_box.get_pos()[0] + horizontal_move_distance,rising_box.get_pos()[1]])
        elif key == simplegui.KEY_MAP["space"]: # 重排文字顺序
            rising_box.shuffle_sentence()

# 为游戏开始或重新开始初始化全局变量，也是鼠标点击按钮的事件处理函数
def start_game():
    global prime_sentence_list, stopped_box, rising_box,current_section_list, has_rising_box, game_over, score, last_four_box
    score = 0
    label.set_text("游戏得分 = 0分")
    game_over = False
    prime_sentence_list = read_from_file('三字经.txt')
    stopped_box = set([])
    last_four_box = []
    current_section_list = generate_current_section_list()
    rising_sentence = current_section_list.pop()
    rising_box = Box([0,canvas_height], box_width, box_height, text_shuffle(rising_sentence[1:]), rising_sentence[1:], int(rising_sentence[0]))

    has_rising_box = True

# 创建窗口初始化画布
frame = simplegui.create_frame("挑战《三字经》", canvas_width, canvas_height)
label = frame.add_label("游戏得分 = 0分")

# 注册事件处理函数
frame.set_keydown_handler(keydown)                         # 按键处理，每次按键会调用keydown函数
frame.set_draw_handler(draw)                               # 显示处理，每秒调用draw函数60次
timer = simplegui.create_timer(1000.0, box_spawner)        # 每秒调用box_spawner函数1次
button = frame.add_button('重新开始游戏', start_game, 100)   # 鼠标每次点击“重新开始游戏”按钮，调用start_game函数1次

# 启动游戏
start_game()     # 为游戏开始或重新开始初始化全局变量
timer.start()    # 启动定时器
frame.start()    # 显示窗口
