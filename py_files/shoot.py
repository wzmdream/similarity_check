'''
Created on 2014年7月17日

@author: ysy

'''
import simpleguitk as simplegui
import random,math


WIDTH = 566
HEIGHT = 572
started = False

time = 0
score = 0
enemy_ID = 0
#图像类
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

#游戏开始背景
background_info = ImageInfo([283, 286], [566, 572])
background_image = simplegui.load_image("image\\shoot_background.png")

# begin image
begin_info = ImageInfo([200, 150], [400, 300])
begin_image = simplegui.load_image("image\\begingame.png")

#游戏进行中背景
back_info = ImageInfo([283, 286], [566, 572])
back_image = simplegui.load_image("image\\background.png")

# 飞机图像
plane_info = ImageInfo([60, 60], [120, 120], 40)
plane_image = simplegui.load_image("image\\plane.png")

#敌机1图像
enemy1_info = ImageInfo([35, 45], [70, 90], 35)
enemy1_image = simplegui.load_image("image\\enemy1.png")
#子弹图像
bullet_info = ImageInfo([6, 10], [12, 20], 6, 50)
bullet_image = simplegui.load_image("image\\bullet.png")
#敌机2图像
enemy2_info = ImageInfo([24, 18], [48, 36],24)
enemy2_image = simplegui.load_image("image\\enemy2.png")
#敌机3图像
enemy3_info = ImageInfo([24, 108], [48, 216])
enemy3_image = simplegui.load_image("image\\enemy3.png")
#敌机1爆炸图像
enemy1_explosion_info = ImageInfo([35, 45], [70, 90], 35, 4, True)
enemy1_explosion_image = simplegui.load_image("image\\enemy1_exp.png")
#敌机2爆炸图像
enemy2_explosion_info = ImageInfo([24, 18], [48, 36],24, 4, True)
enemy2_explosion_image  = simplegui.load_image("image\\enemy2_exp.png")
#爆炸声音
explosion_sound = simplegui.load_sound("sound\\enemy2_down.wav")

#游戏结束声音
gameover_sound = simplegui.load_sound("sound\\game_over.wav")
gameover_sound.set_volume(.2)
#子弹声音
bullet_sound = simplegui.load_sound("sound\\bullet.wav")
bullet_sound.set_volume(.2)
#游戏声音
gamemusic_sound = simplegui.load_sound("sound\\game_music.wav")
gamemusic_sound.set_volume(.2)
# 计算两点之间距离
def dist(p, q):
    return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)

# 子弹类
class Bullet:
    def __init__(self, bullet_img, vel, init_pos, info, sound = None):
        self.image = bullet_img
        self.pos = init_pos
        self.vel = [vel[0],vel[1]]
        self.speed = 2
        self.image_center= info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.age = 0
        self.lifespan = info.get_lifespan()
        if sound:
            sound.rewind()
            sound.play()

    def update(self):
        self.pos[1] -= self.speed
        self.age += 1
        if self.age >= self.lifespan:
            return True
        else:
            return False
    def get_radius(self):
        return self.radius
    def draw(self,canvas):
        canvas.draw_image(self.image, self.image_center , self.image_size, self.pos, self.image_size, 0)
    #子弹打中飞机
    def collide(self, other_object):
        if dist(self.pos, other_object.get_position()) < self.radius + other_object.get_radius():
            return True
        else:
            return False
# 玩家类
class Player:
    def __init__(self, pos,  image, info):
        self.pos = [pos[0], pos[1]]
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.bullet_pos = [0,0]
        self.speed = 5
        self.radius = info.get_radius()

    def moveLeft(self):
        # 飞机向左平移
        if self.pos[0] - self.image_center[0] <= 0 :
            self.pos[0] = self.image_center[0]
        else:
            self.pos[0] = (self.pos[0] - 10)

    def moveRight(self):
        # 飞机向右平移
        if self.pos[0] + self.image_center[0] >= WIDTH :
            self.pos[0] =  WIDTH - self.image_center[0]
        else:
            self.pos[0] = (self.pos[0] + 10)

    def moveForward(self):
        # 飞机前进
        if self.pos[1] - self.image_center[1] <=0 :
            self.pos[1] =  self.image_center[1]
        else:
            self.pos[1] = (self.pos[1] - 5)

    def moveBackward(self):
        # 飞机后退
        if self.pos[1] + self.image_center[1] >= HEIGHT :
            self.pos[1] =  HEIGHT - self.image_center[1]
        else:
            self.pos[1] = (self.pos[1] + 5)

    def shoot(self):
        global bullets
        self.bullet_pos[0] = self.pos[0] - bullet_info.get_center()[0]
        self.bullet_pos[1] = self.pos[1] - self.image_center[1] - bullet_info.get_center()[1]
        bullet = Bullet(bullet_image, [0,0],self.bullet_pos, bullet_info,bullet_sound)
        bullets.add(bullet)

    def get_position(self):
        return self.pos
    def get_radius(self):
        return self.radius
    def draw(self,canvas):
        canvas.draw_image(self.image, self.image_center , self.image_size,
                              self.pos, self.image_size, 0)
# 敌机类
class Enemy:
    def __init__(self, pos, image, info, sound = None):
        self.pos = [pos[0], pos[1]]
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.animated = info.get_animated()
        self.lifespan = info.get_lifespan()
        self.age = 0
        if sound:
            sound.rewind()
            sound.play()

    def get_position(self):
        return self.pos
    def get_radius(self):
        return self.radius
    def update(self):
        self.pos[1] = (self.pos[1] + 1) % HEIGHT
        self.age += 1
        if self.age >= self.lifespan:
            return True
        else:
            return False
    #敌机撞到飞机
    def collide(self, other_object):
        if dist(self.pos, other_object.get_position()) <= self.radius + other_object.get_radius():
            return True
        else:
            return False
    def draw(self, canvas):
        global time
        if self.animated:
            self.age = (time % self.lifespan) // 1
            canvas.draw_image(self.image, [self.image_center[0], self.image_center[1]+ self.age * self.image_size[1]],
                              self.image_size,  self.pos, self.image_size, 0)
            time += 1
        else:
            canvas.draw_image(self.image, self.image_center , self.image_size,
                              self.pos, self.image_size, 0)

#按键按下事件
def keydown(key):
    global player
    if key == simplegui.KEY_MAP['left']:
        player.moveLeft()
    elif key == simplegui.KEY_MAP['right']:
        player.moveRight()
    elif key == simplegui.KEY_MAP['up']:
        player.moveForward()
    elif key == simplegui.KEY_MAP['down']:
        player.moveBackward()
    elif key == simplegui.KEY_MAP['space']:
        player.shoot()
#敌机随机出现
def enemy_spawner():
    global enemy_group,enemy_ID
    if started:
        random.seed()
        x = random.randrange(35, (WIDTH - 35))
        enemy_ID = random.randint(0, 3)
        if enemy_ID == 0:
            a_enemy = Enemy([x, enemy1_info.get_center()[1]],  enemy1_image, enemy1_info)
        else:
            a_enemy = Enemy([x, enemy2_info.get_center()[1]],  enemy2_image, enemy2_info)
        enemy_group.add(a_enemy)
#组和一个物体 的 碰撞
def group_collide(group, other_object):
    global explosion_group,enemy_ID
    remove_set = set([])
    check = False
    for a_element in list(group):
        if 	a_element.collide(other_object):
            remove_set.add(a_element)
            check = True
            if a_element.get_radius() == 20 :#1号敌机
                 a_explosion = Enemy(other_object.get_position(), enemy1_explosion_image,enemy1_explosion_info, explosion_sound)
            else:
                a_explosion = Enemy(other_object.get_position(), enemy2_explosion_image,enemy2_explosion_info, explosion_sound)
            explosion_group.add(a_explosion)

    group.difference_update(remove_set)
    return check
#组和组 之间的 碰撞
def group_group_collide(enemy_group, bullets):
    remove_set = set([])
    #分别记录打掉敌机1和2的个数
    collide = [0,0]
    for a_element in list(enemy_group):
        if group_collide(bullets, a_element):
            if a_element.get_radius() == 20:
                collide[0] += 1
            else:
                collide[1] += 1
            remove_set.add(a_element)

    enemy_group.difference_update(remove_set)
    return collide
# 鼠标单击事件
def click(pos):
    global started, score,enemy_group,explosion_group,bullets,player
    center = [WIDTH / 2, HEIGHT / 2]
    size = begin_info.get_size()
    width = (center[0] - size[0] / 2) < pos[0] < (center[0] + size[0] / 2)
    height = (center[1] - size[1] / 2) < pos[1] < (center[1] + size[1] / 2)
    if (not started) and width and height:
        started = True
        score = 0
        enemy_group = set([])
        explosion_group = set([])
        bullets = set([])
        gamemusic_sound.rewind()
        gamemusic_sound.play()
        #游戏重新开始，飞机回到初始位置
        player = Player([WIDTH/2, HEIGHT - plane_info.get_size()[0]/2], plane_image, plane_info)
#按照group画图
def process_group(canvas, group_set):
    remove_set = set([])
    for a_element in list(group_set):
        a_element.draw(canvas)
        if a_element.update():
            remove_set.add(a_element)

    group_set.difference_update(remove_set)
#绘图事件
def draw(canvas):
    global player, bullets, enemy_group,explosion_group
    global started,score,lives
    center = background_info.get_center()
    size = background_info.get_size()
    canvas.draw_image(background_image,  center, size,center, size, 0)

    # 如果没有开始，画开始图像begin_image，如果点击开始，画背景图像、飞机等
    if not started:
        canvas.draw_image(begin_image, begin_info.get_center(), 
                          begin_info.get_size(), [WIDTH / 2, HEIGHT / 2], 
                          begin_info.get_size())
    else:
        canvas.draw_image(back_image, back_info.get_center(), 
                          back_info.get_size(), [WIDTH / 2, HEIGHT / 2], 
                          back_info.get_size())
        player.draw(canvas)
        process_group(canvas, enemy_group)
        process_group(canvas, bullets)
    #敌机和玩家碰撞，游戏结束
    if group_collide(enemy_group, player):
        started = False
        gamemusic_sound.pause()
        gameover_sound.rewind()
        gameover_sound.play()
    #子弹打中敌机个数，记录成绩
    collide_num = group_group_collide(enemy_group, bullets)
    if collide_num[0] > 0 or collide_num[1] > 0:
        process_group(canvas, explosion_group)
        score = score  + 20 * collide_num[0] + 10 * collide_num[1]

    canvas.draw_text("Score:", [400, 50], 20, "red")
    canvas.draw_text(str(score), [500, 50], 20, "red")

# 创建frame
frame = simplegui.create_frame("飞机大战", WIDTH, HEIGHT)
player = Player([WIDTH/2, HEIGHT - plane_info.get_size()[0]/2], plane_image, plane_info)

#创建需要的set集合
enemy_group = set([])
explosion_group = set([])
bullets = set([])

#设置事件句柄
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(click)
frame.set_keydown_handler(keydown)

#创建定时器，每2s产生一架敌机
timer = simplegui.create_timer(2000.0, enemy_spawner)

timer.start()
frame.start()