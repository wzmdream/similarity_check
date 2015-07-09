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
domino_images = simplegui.load_image("http://www.goldata.biz/images/dominoes.png")

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

# 每局下注数
bet_per_round = 10
total_bet = 0

# 对决结果
result_message = ""

# 是否下过注
betted = False

# 是否发过牌
dealed = False

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
        self.dominoes = []
        for domino in DOMINOES:
            self.dominoes.append(Domino(domino))

    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.dominoes)

    def deal_domino(self):
        return self.dominoes.pop()
    
    def __str__(self):
        for domino in self.dominoes:
            print(domino),

# 一手牌            
class Hand:
    def __init__(self, isDealer = False):
        self.dominoes = []
        self.points = 0
        self.isDealer = isDealer

    def __str__(self):
        for domino in self.dominoes:
            print(domino),      

    def add_domino(self, domino):
        if len(self.dominoes) < 2:
            self.dominoes.append(domino)
            self.points += POINTS[domino.get_domino()]
            
    def get_hand(self):
        self.dominoes.sort(key = lambda d: DOMINOES.index(d.name))
        return tuple([d.name for d in self.dominoes])
    
    def get_points(self):
        return self.points % 10
   
    def draw(self, canvas, pos):
        for i in range(len(self.dominoes)):
            self.dominoes[i].draw(canvas, [pos[0] + i * DOMINO_SIZE[0], pos[1]])

# 下注            
def bet():
    global chips, total_bet, betted, dealed
    if dealed:
        return
    chips -= bet_per_round
    total_bet += bet_per_round
    betted = True
    
    
# 洗牌，发牌，决胜负
def deal():
    global chips, total_bet, dealer_hand, player_hand, result_message, betted, dealed
    if not betted or dealed:
        return
    # 洗牌
    deck = Deck()
    deck.shuffle()
    # 发牌
    for i in range(2):
        dealer_hand.add_domino(deck.deal_domino())
        player_hand.add_domino(deck.deal_domino())
    dealed = True
#     print(dealer_hand.get_hand())
#     print(player_hand.get_hand())
    
    # 决胜负
    win = 0
    if dealer_hand.get_hand() in DOMINO_PATTERNS:
        result_message += "庄家：" + DOMINO_PATTERNS[dealer_hand.get_hand()][1] + " "
        if player_hand.get_hand() in DOMINO_PATTERNS:
            result_message += "玩家：" + DOMINO_PATTERNS[player_hand.get_hand()][1] + " "
            if DOMINO_PATTERNS[dealer_hand.get_hand()] < DOMINO_PATTERNS[player_hand.get_hand()]:
                win = -1
            elif DOMINO_PATTERNS[dealer_hand.get_hand()] == DOMINO_PATTERNS[player_hand.get_hand()]:
                win = 0
            else:
                win = 1
        else:
            result_message += "玩家：" + str(player_hand.get_points()) + "点 "
            win = -1
    else:
        result_message += "庄家：" + str(dealer_hand.get_points()) + "点 "
        if player_hand.get_hand() in DOMINO_PATTERNS:
            result_message += "玩家：" + DOMINO_PATTERNS[player_hand.get_hand()][1] + " "
            win = 1
        else:
            result_message += "玩家：" + str(player_hand.get_points()) + "点 "
            if dealer_hand.get_points() < player_hand.get_points():
                win = 1
            elif dealer_hand.get_points() == player_hand.get_points():
                win = 0
            else:
                win = -1
                
    if win == -1:
        result_message += "\n\n你损失了" + str(total_bet) + "点筹码"
        chips -= total_bet
    elif win == 0:
        result_message += "\n\n平手"
        chips += total_bet
    else:
        result_message += "\n\n你赢得了" + str(total_bet) + "点筹码"
        chips += (2 * total_bet)
    

# 启动游戏
def play():
    global total_bet, dealer_hand, player_hand, result_message, betted, dealed
    betted = False
    dealed = False
    total_bet = 0
    dealer_hand = Hand(True)
    player_hand = Hand()
    result_message = ""
    
        
def draw(canvas):
    # 显示下注数
    canvas.draw_text("下注："+str(total_bet), [15, 60], 20, "White")
    # 显示筹码数
    canvas.draw_text("筹码："+str(chips), [650, 60], 20, "White")
    # 绘制庄家的牌
    canvas.draw_text("庄家", [180, 120], 20, "White")
    dealer_hand.draw(canvas, [140, 140])
    # 绘制玩家的牌
    canvas.draw_text("玩家", [560, 120], 20, "White")
    player_hand.draw(canvas, [520, 140])
    # 显示游戏结果
    canvas.draw_text(result_message, [280, 480], 20, "Yellow")
    

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

