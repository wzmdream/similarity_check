# -*- coding: utf-8 -*-
"""
@author: zhangtaihong
"""

# 守卫家园游戏
import simpleguitk as simplegui
import math
import random

# globals for user interface
WIDTH = 800
HEIGHT = 600
enemy_killed = 0
castle_left = 4
enemy_escaped = 0
escaped_limit = 10
success_limit = 100
time = 0
game_started = False
gameover = False
success = False
soldier = None
enemy_group = set([])
castle_group = set([])
arrow_group = set([])
explosion_group  = set([])
class ImageInfo:
    def __init__(self, center, size, radius = 0, lifespan = None, animated = False):
        self.center = center
        self.size = size
        self.radius = radius
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

    def get_lifespan(self):
        return self.lifespan

    def get_animated(self):
        return self.animated

grassland_info = ImageInfo([960, 600], [1920, 1200])
grassland_image = simplegui.load_image("resources/grassland.jpg") # 地面背景
arrow_info = ImageInfo([21, 5], [42, 10],5,60)
arrow_image = simplegui.load_image("resources/arrow.png")         # 箭
castle_info = ImageInfo([54, 52], [109, 105],50)
castle_image = simplegui.load_image("resources/castle.png")       # 城堡
enemy_info = ImageInfo([32, 15], [64, 29], 15, 1000, True)
enemy_image = simplegui.load_image("resources/enemy.png")         # 敌人，图像文件中包含4副图片用来实现动画
soldier_info = ImageInfo([32, 26], [64, 52])
soldier_image = simplegui.load_image("resources/soldier.png")     # 战士，图像文件中包含2副图片用来实现动画
win_info = ImageInfo([320, 240], [640, 480])
win_image = simplegui.load_image("resources/win.png")             # 游戏成功
gameover_info = ImageInfo([320, 240], [640, 480])
gameover_image = simplegui.load_image("resources/gameover.png")   # 游戏结束
explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, True)
explosion_image = simplegui.load_image("resources/explosion.png") # 爆炸，图像文件中包含多副图片用来实现动画

back_sound = simplegui.load_sound("resources/moonlight.wav")      # 背景音乐
shoot_sound = simplegui.load_sound("resources/shoot.wav")         # 箭发射声音
explode_sound = simplegui.load_sound("resources/explode.wav")     # 箭击中敌人的声音
enemy_sound = simplegui.load_sound("resources/enemy.wav")         # 敌人击中城堡的声音

# helper functions to calculate distance of two points
def dist(p,q):
    return math.sqrt((p[0] - q[0]) ** 2+(p[1] - q[1]) ** 2)

# helper functions to process multiple process
def process_sprite_group(sprites,canvas):
    set_sprites = set(sprites)
    for sprite in set_sprites:
        sprite.draw(canvas)
        if not gameover and not success:
            if not sprite.update():
                sprites.discard(sprite)
def enemy_escape_check():
    global enemy_escaped
    set_enemy = set(enemy_group)
    for enemy in set_enemy:
        if enemy.get_pos()[0] < 0:
            enemy_escaped += 1
            enemy_group.discard(enemy)
# 一组对象和另一个对象的碰撞检测
def group_collide(group,other_object):
    global explosion_group
    tmp_group = set(group)
    collided = False
    for sprite in tmp_group:
        if sprite.collide(other_object):
            explosion_pos = sprite.get_pos()
            a_explosion = Sprite(explosion_pos, [0,0], 0, explosion_image,explosion_info, explode_sound)
            explosion_group.add(a_explosion)
            group.discard(sprite)
            collided = True
    return collided

# 两组对象的碰撞检测
def group_group_collide(group1, group2):
    global explosion_group
    tmp_group1 = set(group1)
    i = 0
    for object in tmp_group1:
        if group_collide(group2, object):
            explosion_pos = object.get_pos()
            a_explosion = Sprite(explosion_pos, [0,0], 0, explosion_image,explosion_info, explode_sound)
            explosion_group.add(a_explosion)
            group1.discard(object)
            i += 1
    return i

# 战士类
class Soldier:
    def __init__(self, pos, vel, angle, image, info):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.shooting = False
        self.angle = angle
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
    def get_pos(self):
        return self.pos
    def get_radius(self):
        return self.radius
    def shoot(self):
        global arrow_group
        arrow_pos = [self.pos[0] + self.image_size[0] * math.cos(self.angle), self.pos[1] + self.image_size[0] * math.sin(self.angle)]
        arrow_vel =[0,0]
        arrow_vel[0] = 10 * math.cos(self.angle)
        arrow_vel[1] = 10 * math.sin(self.angle)
        a_arrow = Sprite(arrow_pos, arrow_vel, self.angle, arrow_image, arrow_info, shoot_sound)
        arrow_group.add(a_arrow)

    def set_angle(self, angle):
        self.angle = angle
    def set_shooting(self, is_shooting):
        self.shooting = is_shooting
    def set_vel(self,new_vel):
        self.vel=new_vel
    def draw(self,canvas):
        source_center = [0,0]
        if self.shooting:
            source_center = [self.image_center[0]+self.image_size[0],self.image_center[1]]
            self.shooting = False
        else:
            source_center = self.image_center
        canvas.draw_image(self.image, source_center, self.image_size, self.pos, self.image_size, self.angle)

    def update(self):
        self.pos[0] += self.vel[0]
        self.pos[0] = self.pos[0] % WIDTH
        self.pos[1] += self.vel[1]
        self.pos[1] = self.pos[1] % HEIGHT

# Sprite class
class Sprite:
    def __init__(self, pos, vel, ang, image, info, sound = None):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.angle = ang
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.age = 0
        if sound:
            sound.set_volume(0.05)
            sound.rewind()
            sound.play()
    def get_radius(self):
        return self.radius
    def get_pos(self):
        return self.pos
    def collide(self,other_object):
        if dist(self.pos, other_object.get_pos()) <=  self.radius + other_object.get_radius():
            return True
        else:
            return False

    def draw(self, canvas):
        if self.animated:
            source_center = [self.image_center[0] +self.age % 4 * self.image_size[0], self.image_center[1] ]
            canvas.draw_image(self.image, source_center, self.image_size, self.pos, self.image_size, self.angle)
        else:
            canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)

    def update(self):
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        self.age += 1
        if self.age < self.lifespan:
            return True
        else:
            return False
def draw(canvas):
    global enemy_killed, castle_left,gameover,enemy_escaped,success

    # 绘制背景
    canvas.draw_image(grassland_image,grassland_info.get_center(),grassland_info.get_size(), [WIDTH / 2, HEIGHT / 2], [WIDTH, HEIGHT])

    soldier.draw(canvas)                         # 绘制战士
    soldier.update()
    process_sprite_group(castle_group, canvas)   # 绘制城堡
    process_sprite_group(enemy_group, canvas)    # 绘制敌人
    process_sprite_group(arrow_group,canvas)     # 绘制箭
    process_sprite_group(explosion_group,canvas) # 绘制爆炸
    enemy_escape_check()
    enemy_killed += group_group_collide(enemy_group,arrow_group)
    label_killed.set_text("消灭敌人 = " + str(enemy_killed))
    i = group_group_collide(enemy_group,castle_group)
    castle_left -= i
    enemy_escaped += i
    label_escaped.set_text("逃脱敌人 = " + str(enemy_escaped))
    label_attacked.set_text("完好城堡 = " + str(castle_left))
    if castle_left == 0 or enemy_escaped >= escaped_limit:
        gameover = True
    if enemy_killed >= success_limit:
        success = True
    if gameover:
        canvas.draw_image(gameover_image,gameover_info.get_center(),gameover_info.get_size(), [WIDTH / 2, HEIGHT / 2],[320,240])
        back_sound.pause()
    if success:
        canvas.draw_image(win_image,win_info.get_center(),win_info.get_size(), [WIDTH / 2, HEIGHT / 2],[320,240])
        back_sound.pause()
# 处理鼠标点击事件
def mouse_handler(pos):
    global soldier
    if not gameover and not success:
        angle = math.atan2((pos[1] -soldier.get_pos()[1]) , (pos[0] -soldier.get_pos()[0]))
        soldier.set_angle(angle)
        soldier.set_shooting(True)
        soldier.shoot()

# 处理键盘按下事件
def keydown(key):
    global soldier
    if key == simplegui.KEY_MAP["w"]:          # 向上
        soldier.set_vel([0,-10])
    elif key == simplegui.KEY_MAP["a"]:        # 向左
       soldier.set_vel([-10,0])
    elif key == simplegui.KEY_MAP["d"]:        # 向右
        soldier.set_vel([10,0])
    elif key == simplegui.KEY_MAP["s"]:        # 向下
        soldier.set_vel([0,10])

# 处理键盘释放事件
def keyup(key):
    global soldier
    soldier.set_vel([0,0])

# timer handler that spawns a rock
def enemy_spawner():
    global game_started, enemy_group
    if not gameover and not success:
        random_pos = [WIDTH,abs(random.randrange(HEIGHT) - 80) + 40]
        random_vel = [-(1.0 + random.random()*0.8),0]
        random_ang = 0
        a_enemy = Sprite(random_pos, random_vel, random_ang, enemy_image, enemy_info)
        enemy_group.add(a_enemy)

def init():
    global soldier, enemy_group, castle_group,arrow_group,enemy_killed,castle_left, explosion_group,gameover, enemy_escaped,success
    gameover = False
    success = False
    enemy_killed = 0
    castle_left = 4
    enemy_escaped = 0
    soldier = Soldier([castle_info.get_size()[0], HEIGHT / 2], [0, 0], 0, soldier_image, soldier_info)
    for i in range(4):
        castle = Sprite((castle_info.get_size()[0]/2,HEIGHT / 8 + i * (HEIGHT / 4)),(0,0),0,castle_image,castle_info)
        castle_group.add(castle)
    enemy_group = set([])
    arrow_group = set([])
    explosion_group = set([])
    back_sound.rewind()
    back_sound.set_volume(0.5)
    back_sound.play()

# initialize frame
frame = simplegui.create_frame("守卫家园", WIDTH, HEIGHT)
frame.add_button("重新开始", init, 50)
label_killed = frame.add_label("消灭敌人 = 0")
label_escaped = frame.add_label("逃脱敌人 = 0")
label_attacked = frame.add_label("受到袭击 = 0")
# register handlers
frame.set_mouseclick_handler(mouse_handler)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.set_draw_handler(draw)

timer = simplegui.create_timer(1000.0, enemy_spawner)

# get things rolling
init()
timer.start()
frame.start()