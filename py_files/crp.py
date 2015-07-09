#####################################################
# project:   6th project of Python programming      #
# name:      Chinese ring puzzle                    #
# author:    Baitao                                 #
# date:      2014-7-1                               #
#####################################################

#coding: utf-8
import simpleguitk as simplegui
import random

# globals for user interface
WIDTH = 800
HEIGHT = 600
COUNT = 9
finished = False
started = False
game_type = 1
steps = 0
circle_group = list()
num_group = list() 
info = list()
# class definition
class ImageInfo:
    def __init__(self, center, size):
        self.center = center
        self.size = size
    def get_center(self):
        return self.center

    def get_size(self):
        return self.size
    
class Sprite:
    def __init__(self, pos, image, info):
        self.pos = [pos[0],pos[1]]
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
   
    def get_position(self):
        return self.pos
    
    def set_y(self, y):
        self.pos[1] = y
    
    def draw(self, canvas):
            canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, [90, 240])

background_info = ImageInfo([400, 337], [800, 673])
background_image = simplegui.load_image("http://d2.freep.cn/3tb_1407151317143r1o535025.png")

circle_info = ImageInfo([76, 205], [152, 410])
circle_image = simplegui.load_image("http://d2.freep.cn/3tb_1407141630147118535025.png")

pole_info = ImageInfo([298, 15], [596, 29])
pole_image = simplegui.load_image("http://d2.freep.cn/3tb_140715131715ya7m535025.png")

  
success_info = ImageInfo([166, 33], [332, 66])
success_image = simplegui.load_image("http://d2.freep.cn/3tb_140715131715lw5u535025.png")
 
info_info = ImageInfo([471, 244], [942, 489])
info_image = simplegui.load_image("http://d3.freep.cn/3tb_140715131714rgsh535025.png")


# common helper functions
def down(n):
    if(n > 2):
        down(n-2)
    info.append(str(n))  
    if(n > 2):
        up(n-2)  
    if(n > 1):
        down(n-1)
        
def up(n):
    if(n>1):
        up(n-1)
    if(n > 2):
        down(n-2)
    info.append(str(n))
    if(n > 2):
        up(n-2)
        
def start():
    global started, finished, steps
    circle_group.clear()
    info.clear()
    num_group.clear()
    started = True
    finished = False
    steps = 0
    for i in range(0, COUNT):
        if game_type == 1:
            a_circle = Sprite([(150 + i * 60), 250], circle_image, circle_info) 
            num_group.append('1')
        if game_type == 2:
            a_circle = Sprite([(150 + i * 60), 300], circle_image, circle_info) 
            num_group.append('0')
        if game_type == 3:
            rn = random.randint(0, 1)
            a_circle = Sprite([(150 + i * 60), 300 - rn * 50], circle_image, circle_info) 
            num_group.append(str(rn))           
        circle_group.append(a_circle)    
        
def check(n):
    if n ==1:
        return True
    s = ''.join(num_group)
    s = s[:n-1]
    if int(s) == 1:
        return True
    return False

def succeed(gtype):
    s = ''.join(num_group)    
    if gtype == 1 and int(s) == 0:
        return True
    if gtype == 2 and int(s) == int('1' * COUNT):
        return True
    if gtype == 3 and (int(s) == 0 or int(s) == int('1' * COUNT)):
        return True
    return False 

def show_num(canvas):
    for i in range(0, COUNT):
        canvas.draw_text(str(i + 1), (160 + i * 60, 500), 30, 'Green', 'serif')
    
        
def draw(canvas):
    canvas.draw_image(background_image, background_info.get_center(), background_info.get_size(), [WIDTH / 2, HEIGHT / 2], [WIDTH, HEIGHT])
    if len(circle_group)>0:
        for c in circle_group:
            c.draw(canvas)
        canvas.draw_image(pole_image, pole_info.get_center(), pole_info.get_size(), [450, 170], [650, 29])    
        canvas.draw_text('二进制：', (150, 55), 20, 'White', 'serif')    
        canvas.draw_text(num_group, (250, 60), 30, 'White', 'serif')
        canvas.draw_text('步数：' + str(steps), (620, 55), 20, 'White', 'serif')
        show_num(canvas)
    if not started:
        canvas.draw_image(info_image, info_info.get_center(), info_info.get_size(), [WIDTH / 2, HEIGHT / 2], [600,300])
    if finished:
        canvas.draw_image(success_image, success_info.get_center(), success_info.get_size(), [WIDTH / 2, HEIGHT / 2], success_info.get_size())
    if len(info) > 0:
        for i in range(0, 8):
            t_info = info[i * 50 : (i + 1) * 50]
            canvas.draw_text(','.join(t_info), (10, 450 + i * 20), 12, 'White', 'serif')
            
def key_down(key):
    global finished, steps
    if not finished:
        if len(circle_group) > 0:
            for i in range(0, COUNT):
                if (key == simplegui.KEY_MAP[str(i+1)]) and check(i + 1):
                    if circle_group[i].pos[1] == 250:
                        circle_group[i].set_y(300)
                        num_group[i] = '0'
                    else:
                        circle_group[i].set_y(250)
                        num_group[i] = '1' 
                    steps += 1
            if succeed(game_type):
                finished = True

def type1():
    global game_type
    game_type = 1
    start()
    
def type2():
    global game_type
    game_type = 2
    start()
    
def type3():
    global game_type
    game_type = 3
    start()
    
def game_info():
    info.clear()
    if game_type == 1:
        down(COUNT)
    if game_type == 2: 
        up(COUNT)           

# initialize frame    
frame = simplegui.create_frame("Chinese ring puzzle", WIDTH, HEIGHT)
button2 = frame.add_button('玩法一', type1, 100)
button3 = frame.add_button('玩法二', type2, 100)
button4 = frame.add_button('随机玩法', type3, 100)
button4 = frame.add_button('游戏提示', game_info, 100)

# register handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(key_down)
frame.start()
