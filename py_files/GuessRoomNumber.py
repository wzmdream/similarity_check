__author__ = 'zhangtaihong'
# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simpleguitk as simplegui # 简单用户图形界面接口
import random    # 用random.randrange(start, stop)随机产生秘密的房间号
import math      # 用math.log(x, base)计算猜中所需的最少次数

# 初始化全局变量
secret_number = 1    # 每个回合计算机随机产生的秘密数字
remaining_guesses =0 # 一个回合剩余的猜测次数
range_low = 1        # 秘密房间号的下限
range_high = 25     # 秘密房间号的上限
canvas_height = 500                   # 画布高度，单位为像素
canvas_width = 500                    # 画布宽度，单位为像素
room_list = []                        # 所有房间，
cat_image = simplegui.load_image("cat.png")
# 启动或重新启动游戏的辅助函数
def new_game():
    global secret_number
    global remaining_guesses
    global room_list
    secret_number = random.randrange(range_low, range_high + 1)
    remaining_guesses = int(math.ceil(math.log(range_high, 2)))
    print()  # 为新一轮游戏输出一空白行，以便和上一轮游戏的输出分开
    print("新一轮游戏开始")
    print("你应当在%s和%s之间猜测一个数字" % (range_low, range_high))
    print("你还剩%s次猜测机会！" % remaining_guesses)
    print("请输入你猜测的房间号并按回车键")

    room_list = []
    for i in range(range_high):
        room_list.append(False)

# define event handlers for control panel
def range100():
    # button that changes range to range [0,100) and restarts
    global range_low
    global range_high
    range_low = 1
    range_high = 100
    new_game()

def range25():
    # button that changes range to range [0,1000) and restarts
    global range_low
    global range_high
    range_low = 1
    range_high = 25
    new_game()
def range36():
    # button that changes range to range [0,1000) and restarts
    global range_low
    global range_high
    range_low = 1
    range_high = 36
    new_game()
def input_guess(guess):
    # main game logic goes here
    if not guess.isdigit():
        print("请输入一个整数!")
        return
    no_guess = int(guess)
    print("你猜测的房间号为：%s" % no_guess)
    global remaining_guesses
    remaining_guesses -= 1
    if no_guess == secret_number:
        print("恭喜你，猜对了！")
        print("点击房间按钮重新开始游戏。")
        #new_game()
    elif no_guess < secret_number:
        if remaining_guesses == 0:
            print("对不起！你已经用完所有猜测机会。")
            print("点击房间按钮重新开始游戏。")
            #new_game()
        else:
            print("太小了！")
            print("你还剩余%s次猜测机会！" % remaining_guesses)
    else:
        if remaining_guesses == 0:
            print("对不起！你已经用完所有猜测机会。")
            print("点击房间按钮重新开始游戏。")
            #new_game()
        else:
            print("太大了！")
            print("你还剩余%s次猜测机会！" % remaining_guesses)
    update_canvas(int(guess),secret_number, remaining_guesses)

def update_canvas(guess,secret_number, remaining_guesses):
    if guess==secret_number:
        for i in range(range_high):
            room_list[i] = True
    elif guess < secret_number:

        if remaining_guesses == 0:
            for i in range(range_high):
                room_list[i] = True
        else:
            for i in range(0,guess):
                room_list[i] = True
    else:
        if remaining_guesses == 0:
            for i in range(range_high):
                room_list[i] = True
        else:
            for i in range(guess - 1,range_high):
                room_list[i] = True
def draw(canvas):
    root = int(math.sqrt(range_high))
    length = canvas_width // root
    for row in range(root):
        for col in range(root):
            index = root * row + col
            text_width = frame.get_canvas_textwidth(str(index), 12, 'sans-serif')
            top_left = [length * col,length * row]
            top_right = [length * (col + 1),length * row]
            bottom_right = [length * (col + 1),length * (row + 1)]
            bottom_left = [length * col,length * (row + 1)]
            if not room_list[index]:
                canvas.draw_polygon([top_left, top_right, bottom_right, bottom_left], 1, 'Red', 'Green')
                canvas.draw_text(str(index+1), (top_left[0] + (length - text_width) / 2, top_left[1] + length - 2), 12, 'White', 'sans-serif')
            else:
                canvas.draw_polygon([top_left, top_right, bottom_right, bottom_left], 1, 'Red', 'Blue')
                canvas.draw_text(str(index+1), (top_left[0] + (length - text_width) / 2, top_left[1] + length - 2), 12, 'White', 'sans-serif')
                if index+1 != secret_number:
                    no_cat = frame.get_canvas_textwidth('没有猫', 12, 'sans-serif')
                    canvas.draw_text('没有猫', (top_left[0] + (length - no_cat) / 2, top_left[1] + length / 2), 12, 'White', 'sans-serif')
                else:
                    canvas.draw_image(cat_image, [256,256], [512,512],[top_left[0] + length//2,top_left[1]+length//2 ],[length,length])

# create frame
frame = simplegui.create_frame("猫咪藏在哪个房间", canvas_width, canvas_height)

# register event handlers for control elements
frame.set_draw_handler(draw)                               # 显示处理，每秒调用draw函数60次
frame.add_button("25个房间", range25, 100)
frame.add_button("36个房间", range36, 100)
frame.add_button("100个房间", range100, 100)
frame.add_input("输入你猜测的房间号:", input_guess, 100)

# call new_game and start frame
new_game()
frame.start()