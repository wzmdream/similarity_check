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

# 载入单词列表
f = open('words.dat', 'rb')
words = pickle.load(f)
random.shuffle(words)

class Word:
    def __init__(self, word):
        self.word = word
        self.length = len(word)
        self.index = 0
        self.correct = [None for i in range(self.length)]
        self.freeze = False
        self.startpos = [(WIDTH - self.length*CHAR_WIDTH) / 2, (HEIGHT + CHAR_SIZE)/2]
        
    def draw(self, canvas):
        for i,c in enumerate(self.word):
            pos = [self.startpos[0] + i*CHAR_WIDTH, self.startpos[1]]
            if self.correct[i] is None:
                color = 'Black'
            elif self.correct[i] is True:
                color = 'Green'
            else:
                color = 'Red'
            canvas.draw_text(self.word[i], pos, CHAR_SIZE, color, 'Dejavu Sans Mono')
            if i == self.index:
                canvas.draw_line([pos[0], pos[1]+3], [pos[0]+CHAR_WIDTH, pos[1]+3], 3, 'Gray')
                
    def check_typing(self, char):
        if not self.freeze:
            if char == self.word[self.index]:
                self.correct[self.index] = True
            else:
                self.correct[self.index] = False
            self.index += 1
            if self.index == self.length:
                self.freeze = True
                
    def get_score(self):
        return self.correct.count(True) * 10 // self.length

def play():
    global score, word
    timer.stop()
    score = 0
    word = Word(words.pop())
    timer.start()
    
def draw(canvas):
    word.draw(canvas)
    canvas.draw_text('得分：' + str(score), [20, 40], 15, 'Black')
    
def keydown(key):
    global score
    try:
        ch = chr(key)
    except: # 存在 TypeError 或其它异常
        return
    else:
        word.check_typing(ch.lower())
        if word.freeze:
            score += word.get_score()
    
def change_word():
    global word, score
    score += word.get_score()
    word = Word(words.pop())
    
    

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