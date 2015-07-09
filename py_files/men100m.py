# 秒表游戏-StopWatch"

import simpleguitk as simplegui
import random

# 全局变量
tick_running = False    # 当该变量为False, 时间事件处理器（timer event handler）不做任何事
time_elapsed = 0        # 以0.01秒为单位的时间流逝
interval = 10           # 时间事件处理器触发的周期，0.01秒
width = 1000            # 跑道总长度
height= 300             # 跑道总宽度
start_width = 80        # 起跑区长度
end_width = 100         # 终点之后的跑道长度
line_number_width = 20  # 终点区宽度
player_position = []    # 每个选手的位置
player_velocity = []    # 每个选手的速度
player_finish_time = [] # 每个选手的比赛完成时间
player_name = ['加特林','布雷克','博尔特','盖　伊','马迪纳','鲍威尔','贝　利','汤普森']
text_width = 0          # 选手名字的显示宽度

# 定义把时间（百分之一秒为单位）转化为0:00.00显示格式的函数
def disp_format(t):
    hours = t // (60 * 60 * 100)
    minutes = (t - hours * 60 * 60 * 100) // (60 * 100)
    seconds = (t - hours * 60 * 60 * 100 - minutes * 60 *100) // 100
    centiseconds = t - hours * 60 * 60 * 100 - minutes * 60 *100 - seconds *100
    str_seconds = ""
    if seconds < 10:
        str_seconds = "0" + str(seconds)
    else:
        str_seconds = str(seconds)
    str_centiseconds = ""
    if centiseconds < 10:
        str_centiseconds = "0" + str(centiseconds)
    else:
        str_centiseconds = str(centiseconds)
    return str(minutes) + ":" + str_seconds + "." + str_centiseconds

# 初始化
def init():
    global player_position, player_velocity,text_width,player_finish_time
    player_position = []
    player_velocity = []
    player_finish_time = []
    text_width = frame.get_canvas_textwidth('博尔特', 24, 'sans-serif')
    for i in range(8):
        player_position.append(start_width - text_width)
        player_velocity.append(0.0)
        player_finish_time.append('')


# 定义按钮"各就位"的事件处理函数
def reset():
    global time_elapsed
    global tick_running
    init()
    time_elapsed = 0
    tick_running = False


# 定义按钮"开始跑"的事件处理函数
def start():
    global tick_running
    tick_running = True
    for i in range(8):
        player_velocity[i] = 0.35 + random.random()*0.2 + 0.8
        player_finish_time[i] =''

# 定义时钟事件的处理函数（每0.01秒被系统调用1次）
def tick():
    global time_elapsed
    if tick_running:
        time_elapsed += 1

# 绘制赛道
def draw_field(canvas):
    canvas.draw_line((start_width,0), (start_width, height), 2, 'Orange')
    canvas.draw_line((width - end_width,0), (width - end_width, height), 2, 'Orange')
    canvas.draw_line((width - end_width  + line_number_width,0), (width - end_width + line_number_width, height), 2, 'Orange')
    for i in range(8):
        canvas.draw_line((0, i * height // 8 + 1), (width, i * height // 8 + 1), 2, 'White')
        canvas.draw_text(str(i+1), [width - end_width, (i+1) * height // 8], 24, "White")

# 定义绘制屏幕的处理函数
def draw(canvas):
    draw_field(canvas)
    for i in range(8):
        if player_position[i] <= width - end_width - text_width:
            player_position[i] =  player_position[i] + player_velocity[i]
            player_finish_time[i] = disp_format(time_elapsed)[2:]
        else:
            canvas.draw_text(player_finish_time[i], [width - end_width + 26, (i+1) * height // 8], 24, "Yellow")
        canvas.draw_text(player_name[i], [player_position[i], (i+1) * height // 8], 24, "White")

    time.set_text(disp_format(time_elapsed))

# 创建窗口框架
frame = simplegui.create_frame("百米赛跑", width, height)


# 注册事件处理器
frame.add_button("各就位", reset, 25)
frame.add_button("开始跑", start, 25)
time = frame.add_label(disp_format(time_elapsed))

frame.set_draw_handler(draw)
timer = simplegui.create_timer(interval, tick)

# 启动时钟
timer.start()
# 启动窗口
frame.set_canvas_background('Maroon')
init()
frame.start()