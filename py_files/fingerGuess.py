# -*- coding: utf-8 -*-
"""
请在此处完善你个人的信息
学院：
班级：
学号：
姓名：
"""
import simpleguitk as simplegui
import random

#定义全局变量
WIDTH = 400
HEIGHT = 400               #画布高度和宽度 
image_size= [60,60]        #手势图像高度和宽度
gesture_image = []         # 3张手势图片
choice_image = []          # 显示的2张出拳的图片 
#index_image = [0,1,2]
turns = 0                  #表示局数
score1,score2 = 0, 0       #得分
started = False            #控制是否进入游戏界面
mouse_pos =(0,0)
message = ""               #屏幕上显示输赢的信息 

background1_image = simplegui.load_image("images\\background1.png")
background2_image = simplegui.load_image("images\\background2.png")
start_image = simplegui.load_image("images\\start.png")
gesture_image.append(simplegui.load_image("images\\scissors.png"))
gesture_image.append(simplegui.load_image("images\\stone.png"))
gesture_image.append(simplegui.load_image("images\\cloth.png"))
choice_image.append(simplegui.load_image("images\\stone.png"))
choice_image.append(simplegui.load_image("images\\stone.png"))
background_sound = simplegui.load_sound("sound\\sound1.ogg")
# 定义函数

#定义事件处理函数
def newgame():
    global turns, score1, score2, message 
    turns = 0
    score1,score2 = 0, 0
    #choice_image.append(gesture_image[1])
    #choice_image.append(gesture_image[1])
    background_sound.rewind()
    background_sound.play()
    message = ""

def clicked_card(point):
    return (point[0]-38) // image_size[0] -1     

#定义鼠标单击事件
def click2(pos):
    global started,choice_image,turns,message, score1, score2
    if not started:
        if 150<pos[0]<280 and 200<pos[1]<300:
            started = True
    else:
        if 100<pos[0]<280 and 60<pos[1]<120:
            turns += 1
            image_index = clicked_card(pos)
            computer_index = random.randrange(3) 
            if image_index  == computer_index:
                message = "平手" 
            elif image_index  < computer_index:  
                message = "电脑赢"
                score1 += 1
            elif image_index  == computer_index:
                message = "玩家赢"
                score2 += 1 
            choice_image.pop()
            choice_image.pop()
            choice_image.append(gesture_image[computer_index])
            choice_image.append(gesture_image[image_index])
           
def draw(canvas):
    global started,image_size,message,gesture_image,choice_image,score1,score2
    image_center = [38, 38]
    if not started :
        canvas.draw_image(background1_image,[200,200],[400,400],[200,200],[400,400])
        canvas.draw_image(start_image,[86,39],[171,77],[200,300],[171,77])
    else:
        canvas.draw_image(background2_image,[200,200],[400,400],[200,200],[400,400])
        canvas.draw_text("第"+str(turns)+"回合",[130,60],24,"Black")
        canvas.draw_text("电脑 "+str(score1) + " / " + str(score2)+" 玩家",[80,190],20,"Red")
        for i in range(3):
            canvas.draw_image(gesture_image[i],image_center,image_size,[140+ i * 60,120],image_size)
        canvas.draw_image(choice_image[0],image_center,image_size,[120,260],[120,120])
        canvas.draw_image(choice_image[1],image_center,image_size,[300,260],[120,120])
        canvas.draw_text(message,[140,380],30,"Red")

#创建框架
frame = simplegui.create_frame('石头剪刀布',400,400)
frame.add_button("重来一局", newgame, 50)
#frame.add_button("一局定输赢", newgame, 100)
#frame.add_button("三局两胜", newgame, 100)
#frame.add_button("无尽模式", newgame, 100)

#注册事件处理函数

frame.set_draw_handler(draw)
frame.set_mouseclick_handler(click2)

#启动框架
newgame()
frame.start()

