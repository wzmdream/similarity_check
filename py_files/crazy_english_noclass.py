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
score = 0
word = None
flag = None
pointer = 0

# 载入单词列表
f = open('words.dat', 'rb')
words = pickle.load(f)
random.shuffle(words)


def play():
    global score, word, flag, pointer
    timer.stop()
    score = 0
    word = list(words.pop())
    flag = [None for i in word]
    pointer = 0
    timer.start()
    
def draw(canvas):
    word_length = len(word)
    startpos = [(WIDTH - word_length*CHAR_WIDTH) / 2, (HEIGHT + CHAR_SIZE)/2]
    for i,c in enumerate(word):
        pos = [startpos[0] + i*CHAR_WIDTH, startpos[1]]
        if flag[i] is None:
            color = 'Black'
        elif flag[i] is True:
            color = 'Green'
        else:
            color = 'Red'
        canvas.draw_text(word[i], pos, CHAR_SIZE, color, 'Dejavu Sans Mono')
        if i == pointer:
            canvas.draw_line([pos[0], pos[1]+3], [pos[0]+CHAR_WIDTH, pos[1]+3], 3, 'Gray')
    canvas.draw_text('得分：' + str(score), [20, 40], 15, 'Black')
    
    
def check_typing(char):
    global flag, pointer
    if char == word[pointer]:
        flag[pointer] = True
    else:
        flag[pointer] = False
    pointer += 1
            
            
def calculate_score():
    return flag.count(True) * 10 // len(word)
    
    
def keydown(key):
    global score
    try:
        ch = chr(key)
    except: # 存在 TypeError 或其它异常
        return
    else:
        if pointer < len(word):
            check_typing(ch.lower())
            
    
def change_word():
    global word, flag, pointer, score
    score += calculate_score() 
    word = list(words.pop())
    flag = [None for i in word]
    pointer = 0
    

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