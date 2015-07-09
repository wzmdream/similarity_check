# -*- coding: utf-8 -*-

import simpleguitk as simplegui
import random

## 定义常量
# 画布的尺寸
WIDTH = 800
HEIGHT = 600

# 骨牌的尺寸、中心位置及所有骨牌的图像
DOMINO_SIZE = (70, 190)
DOMINO_CENTER = (35, 95)
domino_images = simplegui.load_image("http://")

# 所有骨牌。文牌是成对的，武牌是独一无二的。
DOMINOES = ('TIAN', 'TIAN', 'DI', 'DI', 'REN', 'REN', 'HE', 'HE', 'MEI', 'MEI', 'CHANG', 'CHANG', \
            'BAN', 'BAN', 'FU', 'FU', 'HONG', 'HONG', 'GAO', 'GAO', 'LING', 'LING', \
            'JIU1', 'JIU2', 'BA1', 'BA2', 'QI1', 'QI2', 'WU1', 'WU2', 'ZHIZUN1', 'ZHIZUN2')

# 所有骨牌对应的点数
POINTS = {'TIAN':12, 'DI':2, 'REN':8, 'HE':4, 'MEI':10, 'CHANG':6, 'BAN':4, 'FU':11, 'HONG':10, \
          'GAO':7, 'LING':6, 'JIU1':9, 'JIU2':9, 'BA1':8, 'BA2':8, 'QI1':7, 'QI2':7, 'WU1':5, \
          'WU2':5, 'ZHIZUN1':6, 'ZHIZUN2':3}

# 对牌与其排位、名称
DOMINO_PATTERNS = {('ZHIZUN1', 'ZHIZUN2'):(1, '至尊宝'), ('TIAN', 'TIAN'):(2, '双天'), ('DI', 'DI'):(3, '双地'), \
                   ('REN', 'REN'):(4, '孖人'), ('HE', 'HE'):(5, '孖和'), ('MEI', 'MEI'):(6, '孖梅'), \
                   ('CHANG', 'CHANG'):(7, '孖长'), ('BAN', 'BAN'):(8, '孖板凳'), ('FU', 'FU'):(9, '孖斧头'), \
                   ('HONG', 'HONG'):(10, '孖红头'), ('GAO', 'GAO'):(11, '孖高脚'), ('LING', 'LING'):(12, '孖零霖'), \
                   ('JIU1', 'JIU2'):(13, '杂九'), ('BA1', 'BA2'):(14, '杂八'), ('QI1', 'QI2'):(15, '杂七'), \
                   ('WU1', 'WU2'):(16, '杂五'), ('TIAN', 'JIU1'):(17, '天王'), ('TIAN', 'JIU2'):(17, '天王'), \
                   ('DI', 'JIU1'):(18, '地王'), ('DI', 'JIU2'):(18, '地王'), ('TIAN', 'REN'):(19, '天杠'), \
                   ('TIAN', 'BA1'):(19, '天杠'), ('TIAN', 'BA2'):(19, '天杠'), ('DI', 'REN'):(20, '地杠'), \
                   ('DI', 'BA1'):(20, '地杠'), ('DI', 'BA2'):(20, '地杠'), \
                   ('TIAN', 'QI2'):(21, '天高九'), ('DI', 'GAO'):(22, '地高九')}


# 初始筹码
chips = 100

# 一些逻辑值。
betted = False # 是否下过注
dealer = False # 是否发过牌


# 骨牌 
class Domino:
    def __init__(self, name):
        if name in DOMINOES:
            self.name = name
        else:
            self.name = None
            print("无效的骨牌: ", name)

    def __str__(self):
        return self.name

    def get_domino(self):
        return self.name

    def draw(self, canvas, pos):
        if self.name != None:
            domino_loc = (DOMINO_CENTER[0] + DOMINO_SIZE[0] * DOMINOES.index(self.name), DOMINO_CENTER[1])
            
            canvas.draw_image(domino_images, domino_loc, DOMINO_SIZE, \
                              [pos[0] + DOMINO_CENTER[0], pos[1] + DOMINO_CENTER[1]], DOMINO_SIZE)

# 一副骨牌
class Deck:
    def __init__(self):
        pass # 初始化一副牌
            
    def __str__(self):
        pass # 返回一个字符串

    def shuffle(self):
        pass # 洗牌。利用 random.shuffle

    def deal_domino(self):
        pass # 发牌。返回一个 Domino 对象
       

# 一手牌            
class Hand:
    def __init__(self, isDealer = False):
        pass # 初始化一手牌

    def __str__(self):
        pass # 返回一个描述一手牌的字符串     

    def add_domino(self, domino):
        pass # 添加一个 Domino 对象
            
    def get_hand(self):
        pass # 返回一个元组
    
    def get_points(self):
        pass # 返回点数和的个位数
   
    def draw(self, canvas, pos):
        pass # 在 canvas 的 pos 位置绘制一手牌

# 下注            
def bet():
    global chips, betted, dealed
    # 不用考虑庄家的筹码变化
    
    betted = True
    
    
# 洗牌，发牌，决胜负
def deal():
    global chips, betted, dealed
    # 按顺序完成洗牌、发牌和决胜负的过程
    # 其中决胜负包含：判断输赢、修改筹码、产生提示信息
    
    dealed = True
    

# 启动游戏
def play():
    global betted, dealed
    # 必要的初始化
    
    betted = False
    dealed = False
    
        
def draw(canvas):
    # 显示下注数

    # 显示筹码数

    # 绘制庄家的牌
    
    # 绘制玩家的牌

    # 显示游戏结果
    pass
    

# 创建用户界面
frame = simplegui.create_frame("推牌九", WIDTH, HEIGHT)
frame.set_canvas_background("Green")
frame.set_draw_handler(draw)

# 创建按钮
frame.add_button("下注", bet, 60)
frame.add_button("发牌",  deal, 60)
frame.add_button("再来一局", play, 60)

# 启动程序
play()
frame.start()

