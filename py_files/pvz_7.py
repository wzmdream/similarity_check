#####################################################
# project:   7th project of Python programming      #
# name:      Plants vs Zombies part1                #
# author:    Baitao                                 #
# date:      2014-7-1                               #
#####################################################

#coding: utf-8
import simpleguitk as simplegui
import math
import random

# globals for user interface
WIDTH = 800
HEIGHT = 600
score = 0
lives = 300
started = False
plantID = 0
zombie_vel = -0.5
zombie_interval = 5000

# globals set
zombie_group = set()
shooter_group = set()
sunflower_group = set()
sunshine_group = set()

# class definition
class ImageInfo:
    def __init__(self, center, size, radius = 0, animated = False, frame = None, lifespan = None):
        self.center = center
        self.size = size
        self.radius = radius
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        self.animated = animated
        if frame:
            self.frame = frame
        else:
            self.frame = 1
    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius

    def get_lifespan(self):
        return self.lifespan

    def get_animated(self):
        return self.animated
    
    def get_frame(self):
        return self.frame
    
class Sprite:
    def __init__(self, pos, vel, image, info, health = 0, attack = 0, attach = 0, attach_obj = None, sound = None):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.frame = info.get_frame()
        self.health = health
        self.attack = attack
        self.attach = attach
        self.attach_obj = attach_obj
        self.age = 0
        if sound:
            sound.rewind()
            sound.play()
   
    def get_position(self):
        return self.pos
    
    def get_radius(self):
        return self.radius
    
    def get_health(self):
        return self.health
        
    def get_attack(self):
        return self.attack
    
    def get_attach(self):
        return self.attach
    
    def init_attach(self):
        self.attach = 0
        
    def get_attach_obj(self):
        return self.attach_obj
    
    def draw(self, canvas):
        if self.animated:
            canvas.draw_image(self.image, [(0.5 + self.age % self.frame) * self.image_size[0], self.image_size[1] / 2], self.image_size, self.pos, self.image_size)
        else:
            canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size)
    
    def update(self):        
        self.pos[0] = self.pos[0] + self.vel[0]
        self.pos[1] = self.pos[1] + self.vel[1]
        self.age += 1
        if ((self.pos[0] < 0)  or (self.pos[0] > WIDTH)) or (self.age >= self.lifespan):
            return True
        else:
            return False
        
    def collide(self, other_object):
        dis = dist(self.get_position(), other_object.get_position())
        if dis <= self.get_radius() + other_object.get_radius():
            return True
        else:
            return False

# image and sound resource
background_info = ImageInfo([383, 165], [766, 330])
background_image = simplegui.load_image("http://d2.freep.cn/3tb_140711132516amq1535025.png")

splash_info = ImageInfo([286, 90], [572, 180])
splash_image = simplegui.load_image("http://d2.freep.cn/3tb_1407111325231o85535025.png")

gameover_info = ImageInfo([163, 147], [327, 294])
gameover_image = simplegui.load_image("http://d2.freep.cn/3tb_140711132519y8e8535025.png")

zombie_info = ImageInfo([32, 50], [64, 100], 20, True, 15)
zombie_image = simplegui.load_image("http://d2.freep.cn/3tb_140711132515f08j535025.png")

zombie1_info = ImageInfo([47.5, 56], [95, 112], 22, True, 17)
zombie1_image = simplegui.load_image("http://d2.freep.cn/3tb_140711132528kiko535025.png")

shooter_info = ImageInfo([28.5, 32], [55.5, 64], 20, True, 15)
shooter_image = simplegui.load_image("http://d3.freep.cn/3tb_140711132521gb83535025.png")

sunflower_info = ImageInfo([25, 30], [50, 60], 20, True, 6)
sunflower_image = simplegui.load_image("http://d3.freep.cn/3tb_140711132524uoiv535025.png")

sunshine_info = ImageInfo([20, 20], [40, 40], 20, False, 1, 100)
sunshine_image = simplegui.load_image("http://d2.freep.cn/3tb_140711132524wuwc535025.png")

bullet_info = ImageInfo([17, 17], [34, 34], 15)
bullet_image = simplegui.load_image("http://d2.freep.cn/3tb_1407111325179krj535025.png")

blood_info = ImageInfo([38, 31.5], [76, 63], 17, True, 6, 6)
blood_image = simplegui.load_image("http://d2.freep.cn/3tb_140711132517dge7535025.png")

explosion_info = ImageInfo([37, 32.5], [74, 65], 17, True, 8, 8)
explosion_image = simplegui.load_image("http://d3.freep.cn/3tb_140711132518pv37535025.png")

# common helper functions
def dist(p,q):
    return math.sqrt((p[0] - q[0]) ** 2+(p[1] - q[1]) ** 2)

# helper function to control game
def game_begin():
    global started, score, lives
    started = True
    score = 0
    lives = 300
    zombie_spawner()

def game_over():
    global started
    started = False
    zombie_group.clear()
    shooter_group.clear()
    sunflower_group.clear()
    sunshine_group.clear()
    
# helper function to draw and update sprite
def process_sprite_group(a_set, canvas):
    for s in list(a_set):
        s.draw(canvas)
        if s.update():
            a_set.remove(s)
        

# timer handler that spawns a sprite (include zombie, sunshine,bullet and flower_sunshine)
def zombie_spawner():
    if started:
        x = WIDTH
        y = random.randrange(1, 11, 2) * 60
        a_zombie = Sprite([x, y], [zombie_vel, 0], zombie_image, zombie_info, 100, 5) 
        zombie_group.add(a_zombie) 
        
def sunshine_spawner():
    global lives
    if started:
        x = random.randrange(WIDTH)
        y = 0
        a_sunshine = Sprite([x, y],[0, 2], sunshine_image, sunshine_info)
        sunshine_group.add(a_sunshine)
        lives += 10
        
def plant_spawner(plantID,pos):
    global lives
    if started:
        for p in list(sunflower_group.union(shooter_group)):
            if (p.get_position() == pos):
                return
        if plantID == 1:
            a_sunflower = Sprite(pos,[0, 0], sunflower_image, sunflower_info, 300)
            sunflower_group.add(a_sunflower)
            lives -= 100
        if plantID == 2:
            a_shooter = Sprite(pos,[0, 0], shooter_image, shooter_info, 360)
            shooter_group.add(a_shooter) 
            lives -= 150 
            
def draw(canvas):
    global score
    canvas.draw_image(background_image, background_info.get_center(), background_info.get_size(), [WIDTH / 2, HEIGHT / 2], [WIDTH, HEIGHT])
    canvas.draw_image(sunflower_image, sunflower_info.get_center(), sunflower_info.get_size(), [20, 20], [40,40])
    canvas.draw_text("100", (40, 40), 10, 'White', 'serif')
    canvas.draw_image(shooter_image, shooter_info.get_center(), shooter_info.get_size(), [80, 20], [40,40])
    canvas.draw_text("150", (100, 40), 10, 'White', 'serif')
    canvas.draw_image(sunshine_image, sunshine_info.get_center(), sunshine_info.get_size(), [140, 20], sunshine_info.get_size())
    canvas.draw_text(str(lives), (160, 30), 16, 'White', 'serif')
    canvas.draw_text('得分：'+ str(score), (WIDTH - 100, 30), 16, 'White', 'serif')
    if not started:
        canvas.draw_image(splash_image, splash_info.get_center(), splash_info.get_size(), (WIDTH / 2, HEIGHT / 2), splash_info.get_size())
    # draw and update ship and sprites
    process_sprite_group(zombie_group, canvas)
    process_sprite_group(shooter_group, canvas)
    process_sprite_group(sunflower_group, canvas)
    process_sprite_group(sunshine_group, canvas)
    
# mouseclick handler, keydown handler and input handler 
def mouseclick(pos):
    global plantID
    splash_size = splash_info.get_size() 
    x_range = (pos[0] <= WIDTH / 2 + splash_size[0] / 2) and (pos[0] >= WIDTH / 2 - splash_size[0] / 2)
    y_range = (pos[1] <= HEIGHT / 2 + splash_size[1] / 2) and (pos[1] >= HEIGHT / 2 - splash_size[1] / 2)
    if  not started and x_range and y_range:
        game_begin()
    if (plantID == 1) or (plantID == 2):
        plant_x = (pos[0] // 80) * 80 + 40
        plant_y = (pos[1] // 120) * 120 + 60
        plant_spawner(plantID,[plant_x, plant_y])
        
    if (pos[0] > 0) and (pos[0] < 40) and (pos[1] > 0) and (pos[1] < 40) and (lives >= 100):
        plantID = 1    
    elif (pos[0] > 60) and (pos[0] < 100) and (pos[1] > 0) and (pos[1] < 40) and (lives >= 150):
        plantID = 2
    else:
        plantID = 0

        
def key_down(key):
    if key == simplegui.KEY_MAP["space"]: 
        game_begin()
   
# initialize frame
frame = simplegui.create_frame("Asteroids", WIDTH, HEIGHT)
# register handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(key_down)
frame.set_mouseclick_handler(mouseclick)
timer = simplegui.create_timer(5000.0, sunshine_spawner)
# get things rolling
timer.start()
frame.start()

