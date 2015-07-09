# -*- coding: utf-8 -*-
#屏幕保护
'''
请在此处完善你个人的信息
学院：
班级：
学号：
姓名：mxy

'''
import simpleguitk as simplegui
import random
WIDTH = 400
HEIGHT = 400
color_list = ['Aqua','Black','Blue','Fuchsia','Gray','Green','Lime','Maroon','Navy','Olive','Orange','Purple','Red','Silver','Teal','White','Yellow']
choice = 0
time = 0
text = ""
def click1():
    global choice
    timer.start()
    choice = 1

def click2():
    global choice
    timer.start()
    choice = 2

def click3():
    global choice,text
    if text != "":
        timer.start()
        choice = 3
    
def timer_handler():
    global time
    time += 1        

def pause():
    global choice
    if timer.is_running():
        timer.stop()
    time = 0    
    choice = 0
    
def input(inp):
    global text
    text = inp    
    
def draw(canvas):  
    line_width = random.randrange(0,6,2)
    line_color = random.choice(color_list)
    fill_color = random.choice(color_list)
    font_color = random.choice(color_list) 
    if choice ==1:
        radius = random.randint(1,10)
        circle_x = random.randrange(radius, WIDTH-radius)
        circle_y = WIDTH/2 * random.random()
        radius = random.randint(1,20)    
        canvas.draw_circle([circle_x,circle_y], radius, line_width, line_color, fill_color)
    if choice == 2:
         point_list = [[random.randrange(0, WIDTH),random.randint(0,HEIGHT)],[WIDTH/2,HEIGHT/2]]
         canvas.draw_polygon(point_list, line_width, line_color, fill_color)
    if choice == 3:
        point =[random.randrange(0, WIDTH),random.randint(0,HEIGHT)]
        font_size = random.choice([6,8,12,24,36,64])
        canvas.draw_text(text, point, font_size, font_color)
            
frame = simplegui.create_frame("屏幕保护程序",400, 400)

frame.add_button("画圆效果", click1, 50)
frame.add_button("折线效果", click2, 50)
frame.add_button("文字效果", click3, 50)
frame.add_input("请输入出现在屏保上的文字：",input,100)
frame.add_button("清空", pause, 50)

frame.set_draw_handler(draw)
timer = simplegui.create_timer(5000,timer_handler)

frame.start()