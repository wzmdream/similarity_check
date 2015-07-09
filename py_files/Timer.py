# -*- coding: utf-8 -*-
"""
首次创建于2014年07月7日
@author: 寇晓斌
"""

# “秒表、定时器”游戏

# 该程序的关键点是：
# 1、对时间按制式格式输出
# 2、设置两个独立的时间触发器

import simpleguitk as simplegui  

# 全局变量
message1, message2, seconds, success_times, tap_times, = "00:00.0", "0/0", 0, 0, 0

# 辅助函数
def format(t):
    #利用字符串的连接制式输出
    global message1, message2, success_times, tap_times
    message1 = str((int)(t / 6000) % 6) + str((int)(t / 600) % 10) + ":" + str((int)((t / 100) % 6)) + str((int)((t / 10) % 10)) + "." + str((int)(t % 10))
    message2 = str(success_times) + "/" + str(tap_times)
   
def start1():
    #时间触发器1开始
    timer1.start()
    
def start2():
    #时间触发器2开始
    timer2.start()
    
def stop():
    #暂停时间触发器，根据最后一位数字改变敲击次数和成功次数，最后制式输出
    global success_times, tap_times, message1, seconds    
    if message1[6] == "0": success_times = success_times + 1
    tap_times += 1
    timer1.stop()
    timer2.stop()
    format(seconds)    
      
def reset():
    #初始化
    global seconds, message2, success_times, tap_times 
    seconds, message2, success_times, tap_times = 0, "0/0", 0, 0, 
    format(seconds)
    timer1.stop()
    timer2.stop()

# 定义间隔0.1秒timer1事件函数
def tick1():
    #每隔0.1秒增加1
    global seconds
    seconds += 1
    format(seconds) 

# 定义间隔0.1秒timer2事件函数    
def tick2():
    #每隔0.1秒减1
    global seconds
    if seconds > 0:
        seconds -= 1
        format(seconds)     
 
#定义定时器增加分钟函数   
def minut_add():
    #每点击一次增加600，这里的600相当于60秒，即1分钟。
    global seconds
    seconds += 600
    format(seconds)

#定义定时器增加秒钟函数
def second_add():
    #每点击一次增加10，这里的10相当于1秒。
    global seconds
    seconds += 10
    format(seconds)
    
#定义绘制画布函数
def draw(canvas):
    #画布中绘制文本
    global message1, message2 
    canvas.draw_text(message2 , [260, 50], 40, "Green")
    canvas.draw_text(message1 , [160, 200], 60, "White")   
    
frame = simplegui.create_frame("秒表、计时器", 600, 400)   #创建框架
timer1 = simplegui.create_timer(100, tick1)               #创建时间触发器1，每0.1秒更新一次tick1
timer2 = simplegui.create_timer(100, tick2)               #创建时间触发器2，每0.1秒更新一次tick2

# register event handlers
frame.add_button("秒表开始", start1, 150)                  #框架上增加”秒表开始“按钮        
frame.add_button("暂停", stop, 150)                        #框架上增加”暂停“按钮
frame.add_button("复位", reset, 150)                       #框架上增加”复位“按钮
frame.add_button("定时器开始",start2, 150 )                 #框架上增加”计时器按钮“按钮
frame.add_button("加分钟",minut_add, 150 )                  #框架上增加”加分钟“按钮
frame.add_button("加秒钟",second_add, 150 )                 #框架上增加”加秒钟“按钮
frame.set_draw_handler(draw)                               #执行画布绘制

#框架开始执行
frame.start()