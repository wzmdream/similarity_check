# 秒表游戏-StopWatch"

import simpleguitk as simplegui
import math
from datetime import datetime

# 全局变量
interval = 1000       # 时间事件处理器触发的周期，1秒
hour = 0.0
minute = 0.0
second = 0.0
hour_radian = 0.0
minute_radian = 0.0
second_radian = 0.0
digit_date = ''
digit_time = ''
display_digit = False

clock_face = simplegui.load_image("images/ClockFace.jpg")
hour = simplegui.load_image("images/Hour.png")
minute = simplegui.load_image("images/Minute.png")
second = simplegui.load_image("images/Second.png")


# 定义按钮的事件处理函数
def toggle():
    global display_digit
    display_digit = not display_digit
    if display_digit:
        button.set_text('关闭数显')
    else:
        button.set_text('开启数显')

def init():
    global hour, minute, second, hour_radian, minute_radian,second_radian,digit_date, digit_time
    dt = datetime.now()
    second_radian = 2.0 * math.pi * dt.second / 60.0
    minute_radian = 2.0 * math.pi * (dt.minute + dt.second / 60.0) / 60.0
    if dt.hour <= 12:
        hour_radian = 2.0 * math.pi * (dt.hour + float(dt.minute) / 60.0) / 12.0
    else:
        hour_radian = 2.0 * math.pi * (dt.hour + float(dt.minute) / 60.0) / 24.0
    smonth = ''
    if dt.month < 10:
        smonth = '0' + str(dt.month)
    else:
        smonth = str(dt.month)
    sday = ''
    if dt.day < 10:
        sday = '0' + str(dt.day)
    else:
        sday = str(dt.day)
    digit_date = str(dt.year) + '年' + smonth + '月' + sday + '日'
    shour = ''
    if dt.hour < 10:
        shour = '0' + str(dt.hour)
    else:
        shour = str(dt.hour)
    sminute = ''
    if dt.minute < 10:
        sminute = '0' + str(dt.minute)
    else:
        sminute = str(dt.minute)
    ssecond = ''
    if dt.second < 10:
        ssecond = '0' + str(dt.second)
    else:
        ssecond = str(dt.second)
    digit_time =  shour + '时' + sminute+ '分' + ssecond +'秒'

# 定义时钟事件的处理函数（每1秒被系统调用1次）
def tick():
    init()

# 定义绘制屏幕的处理函数
def draw(canvas):
    canvas.draw_image(clock_face,[300,300],[600,600],[300,300],[600,600])
    if display_digit:
        canvas.draw_text(digit_date, [155, 230], 36, "Black")
        canvas.draw_text(digit_time, [180, 400], 36, "Black")
    canvas.draw_image(hour,[8,300],[16,600],[300,300],[18,600], hour_radian)
    canvas.draw_image(minute,[6,300],[12,600],[300,300],[12,600], minute_radian)
    canvas.draw_image(second,[15,300],[30,600],[300,300],[30,600], second_radian)
# 创建窗口框架
frame = simplegui.create_frame("时钟", 600, 600)

# 注册事件处理器
button = frame.add_button("开启数显", toggle, 50)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(interval, tick)

# 启动时钟
timer.start()
init()
# 启动窗口
frame.start()