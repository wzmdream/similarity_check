# -*- coding: utf-8 -*-
# 欢天喜地接元宝
"""
请在此处完善你个人的信息
学院：
班级：
学号：
姓名： mxy
"""
import simpleguitk as simplegui
import math
import random
import time

#定义全局变量
WIDTH = 800          #画布大小
HEIGHT = 600
#falling_object = {10:"钻石",5:"元宝",1:"铜钱", -5:"恶狗",-10:"炸弹"}
score = 0            #得分
time = 120           #剩余时间
lives = 3            #3次机会
started = False
over = False
wealthgod = None
falling_group = set([])

#定义图像类
class ImageInfo:
    def __init__(self, center, size, radius = 0, id = 0,  lifespan = None, animated = False):
        self.center = center
        self.size = size
        self.radius = radius
        self.id = id
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        self.animated = animated
    def get_center(self):
        return self.center
    def get_size(self):
        return self.size
    def get_radius(self):
        return self.radius
    def get_id(self):
        return self.id
    def get_lifespan(self):
        return self.lifespan
    def get_animated(self):
        return self.animated

#定义财神类   
class Wealthgod:
    def __init__(self, pos, image, info):
        self.pos = [pos[0], pos[1]]
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
    
    def get_position(self):
        return self.pos
    
    def get_radius(self):
        return self.radius
   
    # 向左平移
    def moveLeft(self):
        if self.pos[0] - self.image_center[0] <= 0 :
            self.pos[0] = self.image_center[0]
        else:
            self.pos[0] -= 10
            
    # 向右平移
    def moveRight(self):
        if self.pos[0] + self.image_center[0] >= WIDTH :
            self.pos[0] =  WIDTH - self.image_center[0]
        else:
            self.pos[0] += 10
            
    def set_pos(self,pos):
        self.pos = pos
        
    def draw(self,canvas):
        canvas.draw_image(self.image, self.image_center , self.image_size, self.pos, self.image_size, 0)       
     
     
#定义坠落物类            
class Fallings:
    def __init__(self,pos,image,info,sound=None):
        self.pos = [pos[0],pos[1]]
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.id = info.get_id()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.age = 0
        if sound:
            sound.rewind()
            sound.play()
        
    def get_position(self):
        return self.pos    
    
    def get_radius(self):
        return self.radius
    
    def get_id(self):
        return self.id
    
    #坠物碰撞到财神
    def collide(self,other_object):
        if dist(self.get_position(), other_object.get_position()) <=  self.radius + other_object.get_radius():
            return True
        else:
            return False
         
    def draw(self,canvas):       
        canvas.draw_image(self.image, self.image_center , self.image_size,
                              self.pos, self.image_size, 0)
 
    def update(self):        
        self.pos[1] = (self.pos[1] + 1 ) % HEIGHT  
        self.age += 1
        if self.age >= self.lifespan:
            return True
        else:
            return False
#图片、声音资源
#开始背景start，游戏背景background，财神wealthgod，钻石diamond，元宝ingot，铜钱copper，恶狗dog，炸弹bomb,开始游戏按钮startbutton
#背景音乐sound1
start_info = ImageInfo([400, 300], [800, 600])
start_image = simplegui.load_image("images\\start.png")
    
background_info = ImageInfo([195, 110], [391, 220])
background_image = simplegui.load_image("images\\background.jpg")    

wealthgod_info = ImageInfo([50, 58], [100, 117],40)
wealthgod_image = simplegui.load_image("images\\wealthgod.png")

diamond_info = ImageInfo([25, 25], [50, 50],20, 1)
diamond_image = simplegui.load_image("images\\diamond.png") 
    
ingot_info = ImageInfo([25, 25], [50, 50],20, 2)
ingot_image = simplegui.load_image("images\\ingot.png")

copper_info = ImageInfo([25, 25], [50, 50],20, 3)
copper_image = simplegui.load_image("images\\copper.png")

dog_info = ImageInfo([25, 25], [50, 50],20, 4)
dog_image = simplegui.load_image("images\\dog.png")

bomb_info = ImageInfo([25, 25], [50, 50],20, 5)
bomb_image = simplegui.load_image("images\\bomb.png")

startbutton_info = ImageInfo([114, 50], [228, 99])
startbutton_image = simplegui.load_image("images\\startbutton.png")

end_info = ImageInfo([400, 300], [800, 600])
end_image = simplegui.load_image("images\\end.png")

collision_info = ImageInfo([10, 10], [20, 20], 17, 24, True)
collision_image = simplegui.load_image("images\\collision.png")    # 碰撞效果

back_sound = simplegui.load_sound("sound\\sound1.ogg")  

#定义函数
def dist(p,q):
    return math.sqrt((p[0] - q[0]) ** 2+(p[1] - q[1]) ** 2)

def newgame():
    global started, over,score,lives
    started = True
    over = False
    score = 0
    lives = 3
    timer.start()

def gameover():
    global started,over,time,sprit_group,wealthgod,falling_group
    started = False
    over = True
    time = 0
    #wealthgod.clear()
    falling_group.clear()

#坠落物随机出现    
def falling_spawner():
    global falling_group, time, falling_id
    if started:
        x = random.randrange(25,WIDTH-25) 
        falling_id = random.randint(0, 4)
        print ( "a_falling ",falling_id)
        if falling_id == 0:
            a_falling = Fallings([x, diamond_info.get_center()[1]], diamond_image, diamond_info)
        elif falling_id == 1:
            a_falling = Fallings([x, ingot_info.get_center()[1]], ingot_image, ingot_info)
        elif falling_id == 2:
            a_falling = Fallings([x, copper_info.get_center()[1]], copper_image, copper_info)
        elif falling_id == 3:
            a_falling = Fallings([x, dog_info.get_center()[1]], dog_image, dog_info)
        elif falling_id == 4:
            a_falling = Fallings([x, bomb_info.get_center()[1]], bomb_image, bomb_info)
        falling_group.add(a_falling)
        time -= 1  
      
#组和一个对象之间的碰撞          
def group_collide(group,other_object):
    global score,lives,wealthgod
    tmp_set = set([])
    collided = False
    for a_falling in list(group):
        print("a_falling.get_id()=",a_falling.get_id())
        if a_falling.collide(other_object):
            tmp_set.add(a_falling)
            collided = True
            if lives == 0:
                over = True
                started = False
            else:
                if a_falling.get_id() == 1:
                    score += 10
                elif a_falling.get_id() == 2:
                    score += 5
                elif a_falling.get_id() == 3:
                    score += 1 
                elif a_falling.get_id() == 4:
                    score -= 5 
                elif a_falling.get_id() == 5:
                    score -= 10
                    lives -= 1
                    wealthgod = Wealthgod([WIDTH/2,HEIGHT - wealthgod_info.get_size()[0]/2], wealthgod_image, wealthgod_info)    
    group.difference_update(tmp_set)    
    return collided     

#在画布上画一组坠物
def process_falling_group(group, canvas):
    tmp_set = set([])
    for a_falling in list(group):
        a_falling.draw(canvas)
        if not over and  a_falling.update():
            tmp_set.add(a_falling)
    group.difference_update(tmp_set) 
                
# 处理鼠标、键盘按下事件       
def mouseclick(pos):
    global started
    if not started and not over:
        if 85<pos[0]<234 and 418<pos[1]<478:
            newgame()  
    wealthgod.set_pos(pos[0],HEIGHT - wealthgod_info.get_size()[0]/2)
    
def keydown(key):
    global wealthgod
    if key == simplegui.KEY_MAP['space']:
        newgame()
    elif key == simplegui.KEY_MAP["left"]:        # 向左
        wealthgod.moveLeft()
    elif key == simplegui.KEY_MAP["right"]:        # 向右
        wealthgod.moveRight()
  
def init():
    global started, over, score, lives, wealthgod, falling_group
    over = False
    score = 0
    lives = 3
    back_sound.rewind()
    back_sound.play()
     
def draw(canvas):
    global time, score, lives, over, started,wealthgod,falling_group
    
    print(started,over,time)
    if not started and not over:
        canvas.draw_image(start_image, start_info.get_center(), start_info.get_size(), [WIDTH / 2, HEIGHT / 2], [WIDTH, HEIGHT])
        #canvas.draw_image(startbutton_image, startbutton_info.get_center(), startbutton_info.get_size(), [400, 500], startbutton_info.get_size()) 
    elif over or time == 0:
        timer.stop()
        canvas.draw_image(end_image, end_info.get_center(), end_info.get_size(), [WIDTH / 2, HEIGHT / 2], end_info.get_size())
        canvas.draw_text('总成绩\n'+" "+ str(score), (20, HEIGHT-100),36, 'Red', 'serif')
        gameover()
    else:    
        canvas.draw_image(background_image, background_info.get_center(), background_info.get_size(), [WIDTH / 2, HEIGHT / 2], [WIDTH, HEIGHT])
        canvas.draw_text('时间：'+ str(time), (100, 30), 16, 'White', 'serif')
        canvas.draw_text('成绩：'+ str(score), (WIDTH/2, 30), 16, 'White', 'serif')
        canvas.draw_text('还有：'+ str(lives) + "次机会", (WIDTH - 200, 30), 16, 'White', 'serif')
        wealthgod.draw(canvas)
        process_falling_group(falling_group, canvas)
        if group_collide(falling_group,wealthgod):
            if lives>0:
            #lives -= 1
                wealthgod.draw(canvas)
            else:
                over = True  
 
# 创建用户界面
frame = simplegui.create_frame("欢天喜地接元宝", WIDTH, HEIGHT)
wealthgod = Wealthgod([WIDTH/2, HEIGHT - wealthgod_info.get_size()[0]/2], wealthgod_image, wealthgod_info)
frame.add_button("再来一局", init, 50)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_mouseclick_handler(mouseclick)
# 创建定时器,1秒掉一个
timer = simplegui.create_timer(1000, falling_spawner)

init()
timer.start()
frame.start()
   
