# -*- coding: utf-8 -*-
import simpleguitk as simplegui
import pickle
import random

## 定义常量
# 画布的尺寸
WIDTH = 600
HEIGHT = 400
CHAR_WIDTH = 45
CHAR_SIZE = 60
TIME_INTERVAL = 3000

word = None
flag = None
pointer = 0     # 指示当前需要输入的位置
score = 0

# 载入单词列表
f = open('words.dat', 'rb')
words = pickle.load(f)
random.shuffle(words)

# 初始化游戏环境
def play():
    global score, word, flag, pointer
    timer.stop()
    word = list(words.pop())
    flag = [None for i in word]
    score = 0
    pointer = 0
    timer.start()
    

# 显示单词、提示短线和得分
def draw(canvas):
    pass
    

# 检查玩家的输入与指针位置的字母是否一致
def check_typing(char):
    global flag, pointer
    pass
            

# 计算得分            
def calculate_score():
    pass
    

# 按键事件响应函数    
def keydown(key):
    global score
    try:
        ch = chr(key)
    except:     # 捕捉 TypeError 或其它异常
        return  # 不做任何处理
    else:
        pass
        # 代码填在这里
            

# 换一个词            
def change_word():
    global word, flag, pointer, score
    pass
    

# 创建用户界面
frame = simplegui.create_frame("疯狂英语", WIDTH, HEIGHT)
frame.set_canvas_background("White")
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)

# 创建按钮
frame.add_button("开始游戏", play, 80)
# 创建定时器
timer = simplegui.create_timer(TIME_INTERVAL, change_word)

play()
frame.start()