'''
Created on 2014年7月21日

@author: xuesheng
'''
#coding: utf-8
import simpleguitk as simplegui
import random
import math

# Var
WIDTH = 800
HEIGHT = 600
bet_flag = False
follow_flag = False
SUITS = ['黑桃', '红桃', '梅花', '方块']
SUITS_VALUES = {'黑桃':4, '红桃':3, '梅花':2, '方块':1}
RANKS = ['K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2', 'A']    #为了排序方便，使用二十六个字母代替牌面的
VALUES = {'A':14, 'K':13, 'Q':12, 'J':11, '10':10, '9':9, '8':8, '7':7, '6':6, '5':5, '4':4, '3':3, '2':2}
mLst = []
pLst = []
m_rank = 0
p_rank = 0
same = True
started = False
hand_style = ''
m_hand_style = ''
p_hand_style = ''
outcome = ''
voiceover = ''
rule = '大规则：同花顺＞铁支(四张相同)＞葫芦(三带二)＞同花＞顺子＞三条＞两对＞对子＞散牌'
m_win_num = 0
p_win_num = 0
side_flag = ''
p_total_money = 10000
m_total_money = 1000000
bet_money = 0
p_bet_money = 100
m_bet_money = 100
p_is_bet = False
m_is_bet = False
# Source
CARD_SIZE = (72, 111)                 #加载图片资料
CARD_CENTER = (36, 55.5)
card_images = simplegui.load_image("image\\card.png")

CARD_BACK_SIZE = [72, 111]             #加载扑克背面图片
CARD_BACK_CENTER = [36, 55.5]
card_back = simplegui.load_image("image\\back.png")


background_size = [808, 606]           #加载开始前背景图片
background_center = [404, 303]
background_image = simplegui.load_image("image\\shguize1.png")

# initialize some useful global variables
in_play, stand_flag, bet_flag, flag= False, False, False, -1
value = -1
total = 0
pos = [140, 180]


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print ("Invalid card: ", suit, rank)

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + (3 + CARD_SIZE[0]) * RANKS.index(self.rank), 
                    CARD_CENTER[1] + (15 + CARD_SIZE[1]) * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.cards = []    # create Hand object

    def __str__(self):
        s = "Hand contain "            # return a string representation of a hand
        for card in self.cards:
            s += str(card) + " "
        return s

    def add_card(self, card):
        self.cards.append(card)        # add a card object to a hand

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        value = 0    # compute the value of the hand, see Blackjack video
        for index in range(len(self.cards)):
            card = self.cards[index].get_rank()
            value += VALUES[card]            
        return value        
        
    def draw(self, canvas, pos):
        pos_list = pos[:]    # draw a hand on the canvas, use the draw method for cards
        for index in range(len(self.cards)):
            self.cards[index].draw(canvas, pos_list)
            pos_list[0] += 72
        
# define deck class 
class Deck:
    def __init__(self):
        self.cards = []    # create a Deck object
        for suit in SUITS:
            for rank in RANKS:
                card = Card(suit, rank)
                self.cards.append(card)        
        
    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.cards)    # use random.shuffle()

    def deal_card(self):
        return self.cards.pop()    # deal a card object from the deck
    
    def __str__(self):
        s = 'Deck contains '    # return a string representing the deck
        for card in self.cards:
            s += str(card) + ' '
        return s    

#define event handlers for buttons
def get_max(lst):          #返回牌面最大的值
    s = ''.join(lst)
    return max(s.rfind('1'),s.rfind('2'),s.rfind('3'),s.rfind('4'))

def get_max_flower(lst,idx):   #返回牌面最大值的花色  
    fLst = list()
    for i in lst:
        if i[idx] != '0':
            fLst.append(i[0])
    return max(fLst)                       

def add(lst):        #将手中的牌用列表形式表示，首位代表花色，后13位代表牌面值做列表和
    global same
    same = True
    tList = ['0','0','0','0','0','0','0','0','0','0','0','0','0','0']
    flower = None
    for l in lst:
        if flower == None:
            flower =  l[0]
        elif flower != l[0]:
            same = False            
        for i in range(1, 14):
            tList[i] = str(int(l[i]) + int(tList[i]))
    return tList


def judge_type(sumList, sideID):#评级，返回评级后的列表及级别全局变量
    global m_rank, p_rank, hand_style
    tList = add(sumList)    
    s = ''.join(tList)
    if s.find('11111') > -1 and same:
        hand_style = '同花顺'
        tList[0] = get_max_flower(sumList, get_max(tList))
        rank = 9
    elif s.find('4')> -1:
        hand_style = '铁支'
        rank = 8
    elif s.find('3') > -1 and s.find('2')> -1:
        hand_style = '葫芦'
        rank = 7
    elif same and len(player.cards) >2:
        hand_style = '同花'
        rank = 6
        tList[0] = get_max_flower(sumList, get_max(tList))
    elif s.find('11111') > -1:
        hand_style = '顺子'
        rank = 5
        tList[0] = get_max_flower(sumList, get_max(tList))
    elif s.find('3') > -1:
        hand_style = '三条'
        rank = 4
    elif s.count('2') == 2:
        hand_style = '两对'
        rank = 3
        tList[0] = get_max_flower(sumList, s.rfind('2'))
    elif s.find('2') > -1:
        hand_style = '对子'
        rank = 2
        tList[0] = get_max_flower(sumList, s.rfind('2'))
    else:
        hand_style = '散牌'
        rank = 1
        tList[0] = get_max_flower(sumList, get_max(tList))
    if sideID == 0:
        m_rank = rank
    else:
        p_rank = rank 
    return tList        

def comp(mList, pList):      #比较两手牌
    global m_hand_style, p_hand_style, outcome
    ml = judge_type(mList, 0)
    m_hand_style = hand_style
    pl = judge_type(pList, 1)
    p_hand_style = hand_style
    sml = ''.join(ml)
    spl = ''.join(pl)
    if m_rank > p_rank:
        outcome = '电脑赢！'
    elif m_rank < p_rank:
        outcome = '玩家赢！'
    else:
        if m_rank == 9 or m_rank == 5 or m_rank == 1:
            if get_max(ml) > get_max(pl):
                outcome = '电脑赢！'
            elif get_max(ml) < get_max(pl):
                outcome = '玩家赢！'
            else:
                if ml[0] > pl[0]:
                    outcome = '电脑赢！'
                else:
                    outcome = '玩家赢！'
        if m_rank == 8:
            if sml.rfind('4') > spl.rfind('4'):
                outcome = '电脑赢！'
            else:
                outcome = '玩家赢！'
        if m_rank == 7 or m_rank == 4:
            if sml.rfind('3') > spl.rfind('3'):
                outcome = '电脑赢！'
            else:
                outcome = '玩家赢！'
        if m_rank == 6:
            if ml[0] > pl[0]:
                outcome = '电脑赢！'
            elif ml[0] < pl[0]:
                outcome = '玩家赢！'
            else:
                if get_max(ml) > get_max(pl):
                    outcome = '电脑赢！'
                elif get_max(ml) < get_max(pl):
                    outcome = '玩家赢！'
        if m_rank == 3 or m_rank == 2:
            if sml.rfind('2') > spl.rfind('2'):
                outcome = '电脑赢！'
            elif sml.rfind('2') < spl.rfind('2'):
                outcome = '玩家赢！'
            else:
                if ml[0] > pl[0]:
                    outcome = '电脑赢！'
                else:
                    outcome = '玩家赢！'

def start():
    global outcome, in_play, player, dealer, deck, stand_flag, total, bet_flag, mLst, pLst, started, voiceover, side_flag, p_is_bet, m_is_bet, m_total_money, bet_money
    # your code goes here
    player, dealer, deck = Hand(), Hand(), Deck()
    outcome = ''
    bet_money = 0
    mLst , pLst = [], []
    stand_flag = False
    bet_flag, p_is_bet, m_is_bet = False, False, False    
    deck.shuffle()
    card1, card2, card3, card4= deck.deal_card(), deck.deal_card(), deck.deal_card(), deck.deal_card()
    while len(player.cards) < 2:
        tLst = ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
        card = deck.deal_card()
        if VALUES[card.get_rank()] > 7:
            tLst[VALUES[card.get_rank()]-1] = 1
            tLst[0] = str(SUITS_VALUES[card.get_suit()])
            pLst.append(tLst)                      
            player.add_card(card)
    while len(dealer.cards) < 2:
        tLst = ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
        card = deck.deal_card()
        if VALUES[card.get_rank()] > 7:
            tLst[VALUES[card.get_rank()]-1] = 1
            tLst[0] = str(SUITS_VALUES[card.get_suit()])
            mLst.append(tLst)                      
            dealer.add_card(card)
    if in_play:          
        total += 1
    else:
        outcome = ""    
        stand_flag = False
        total += 1
    in_play = True
    started = True   
    comp(mLst[1:], pLst[1:])       
    if outcome == '电脑赢！':
        m_is_bet = True
        voiceover = '电脑牌大，电脑说话！'        
        side_flag = 'm'
        m_total_money -= m_bet_money
        bet_money += m_bet_money
        side_flag = 'p'
    else:
        voiceover = '玩家牌大，玩家说话！'
        side_flag = 'p'    
    
    
def bet():
    # replace with your code below 
    # if the hand is in play, hit the player   
    # if busted, assign a message to outcome, update in_play and score
    global in_play, outcome, stand_flag, side_flag, p_total_money,m_total_money, bet_money, p_is_bet, m_is_bet
    if in_play:
        if side_flag == 'p':        
            p_total_money -= p_bet_money
            bet_money += p_bet_money 
            p_is_bet = True
            side_flag = 'm'
            m_is_bet = False
            judge_type(mLst, 0)
            if get_max(judge_type(mLst, 0)) > 9 or m_rank == 2:
                m_total_money -= m_bet_money
                bet_money += m_bet_money
                m_is_bet = True
                sent()
            else:
                turn_card()
                outcome = '玩家赢！'
                stand_flag = True
        elif side_flag == 'm':
            m_total_money -= m_bet_money
            bet_money += m_bet_money
            m_is_bet = True
            side_flag = 'p'
            bet()
        #player.add_card(deck.deal_card())
         

def show():    #梭了，把玩家所有的财富抵押
    pass

def sent():    #发牌，最多到5张结束
    global in_play, bet_flag, flag
    bet_flag = False  
    if in_play and len(player.cards) < 5:
        card = deck.deal_card()
        while VALUES[card.get_rank()] < 8:
            card = deck.deal_card()
        tLst = ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
        tLst[VALUES[card.get_rank()]-1] = 1
        tLst[0] = str(SUITS_VALUES[card.get_suit()])
        pLst.append(tLst)                      
        player.add_card(card)
        card = deck.deal_card()
        while VALUES[card.get_rank()] < 8:
            card = deck.deal_card()
        tLst = ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
        tLst[VALUES[card.get_rank()]-1] = 1
        tLst[0] = str(SUITS_VALUES[card.get_suit()])
        mLst.append(tLst) 
        dealer.add_card(card)          
                
def turn_card():    #翻牌，比较双方牌面大小，确定输赢
    global stand_flag, m_win_num, p_win_num, m_total_money, p_total_money, bet_money
    if len(player.cards) == 5:
        stand_flag = True
        comp(mLst, pLst)
        if outcome == '电脑赢！':
            m_total_money += bet_money
            print ("test1")
            m_win_num += 1
        elif outcome == '玩家赢！':
            p_total_money += bet_money
            print("test2")
            p_win_num += 1
        bet_money = 0
    
def stand():    #弃牌认输
    # replace with your code below   
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    # assign a message to outcome, update in_play and score
    global in_play, stand_flag, outcome, m_total_money, bet_money  
    print("test1")  
    if side_flag == 'p':
        print(side_flag)
        print("test2")
        m_total_money += bet_money
        bet_money = 0
        m_is_bet = False
    outcome = "庄家赢"
    in_play, stand_flag = False, True   
    
def tick():
    #每隔0.1秒增加1
    global seconds
    seconds += 1
    format(seconds)    

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    if started == False:canvas.draw_image(background_image, background_center, background_size, [WIDTH / 2, HEIGHT / 2], [WIDTH, HEIGHT])
    if started == True:
        #canvas.draw_text("旁白：", [80, 50], 20, "Yellow")
        #canvas.draw_text(voiceover, [150, 50], 20, "Yellow")
        canvas.draw_text(rule, [14, 120], 14, "Blue")       
        canvas.draw_text("总局数：" , [550, 50], 20, "Yellow")
        canvas.draw_text(total, [650, 50], 20, "White")
        canvas.draw_text("电脑赢：" , [550, 80], 15, "Yellow")
        canvas.draw_text(m_win_num , [630, 80], 15, "Yellow")
        canvas.draw_text("玩家赢：" , [680, 80], 15, "Yellow")
        canvas.draw_text(p_win_num , [760, 80], 15, "Yellow")
        canvas.draw_text("电脑", [15, 240], 30, "Yellow")
        canvas.draw_text("电脑钱袋：", [15, 260], 10, "Yellow")
        canvas.draw_text(m_total_money, [78, 260], 10, "Yellow")
        canvas.draw_text('合计押注：', [120, 500], 20, "Yellow")
        canvas.draw_text(bet_money, [250, 500], 20, "Yellow")
        if m_is_bet :
            canvas.draw_text("电脑押注：", [15, 285], 10, "Yellow")  
            canvas.draw_text(m_bet_money, [75, 285], 10, "Yellow") 
        canvas.draw_text("玩家", [15, 405], 30, "Yellow")
        canvas.draw_text("玩家钱袋：", [15, 425], 10, "Yellow") 
        canvas.draw_text(p_total_money, [78, 425], 10, "Yellow")
        if p_is_bet:
            canvas.draw_text("玩家押注：", [15, 445], 10, "Yellow")  
            canvas.draw_text(p_bet_money, [75, 445], 10, "Yellow")                      
        dealer.draw(canvas, pos)
        if stand_flag == True:
            canvas.draw_text(m_hand_style, [540, 240], 30, "Yellow")
            canvas.draw_text(p_hand_style, [540, 405], 30, "Yellow")
            canvas.draw_text("本局结果：", [120, 570], 20, "Yellow")
            canvas.draw_text(outcome, [250, 570], 20, "White") 
        if stand_flag == False:
            canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)                       
        player.draw(canvas, [pos[0], pos[1] + 160])
    
# initialization frame
frame = simplegui.create_frame("梭哈", WIDTH, HEIGHT)
frame.set_canvas_background("Green")
timer = simplegui.create_timer(3000, tick)   

#create buttons and canvas callback
frame.add_button("开始", start, 100)
frame.add_button("下注",  bet, 100)
frame.add_button("梭了",  show, 100)
frame.add_button("翻牌",  turn_card, 100)
frame.add_button("弃牌", stand, 100)
frame.set_draw_handler(draw)

# get things rolling

frame.start()


