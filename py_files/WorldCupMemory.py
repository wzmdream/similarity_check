# -*- coding: utf-8 -*-
"""
请在此处完善你个人的信息
学院：
班级：
学号：
姓名：
"""
# 世界杯16强连连看游戏
import simpleguitk as simplegui
import random
all_image = []         # 所有32张图片的索引下标，两两重复
exposed = []           # 真表示对应的图片已经翻开
check_list = []        # 正在对比的两种图片
turns = 0

flag_image = []  # 16强球队的国旗图标


# 初始化全局变量的辅助函数
def new_game():
    global all_image, exposed, check_list, turns,flag_image,back_image
    turns = 0
    all_image = []
    exposed = []
    check_list = []
    list1 = range(16)
    list2 = range(16)
    all_image.extend(list1)
    all_image.extend(list2)
    random.shuffle(all_image)
    for card in all_image:
        exposed.append(False)
    label.set_text('回合次数 = 0')

def clicked_card(point):
    # i * 8 + j
    return (point[0] // 128)  + (point[1] // 128) * 8

# 鼠标点击事件的处理函数
def mouseclick(pos):
    # 也是游戏逻辑的实现
    global exposed,check_list,turns
    image_index = clicked_card(pos)
    if not exposed[image_index]:
        exposed[image_index] = True
        if len(check_list) < 2:
            check_list.append(image_index)
            if len(check_list) == 2:
                turns +=1
        else:
            if all_image[check_list[0]] != all_image[check_list[1]]:
                for image in check_list:
                    exposed[image] = False
                check_list = []
                check_list.append(image_index)
            else:
                check_list.pop()
                check_list.pop()
                check_list.append(image_index)
    label.set_text('回合次数 = ' + str(turns))
                        
# 每个图片的显示大小为128x128像素，16强共32张图片，32张图片显示为4行8列
def draw(canvas):
    image_size = [128, 128]                    # 每张图片实际显示的大小
    flag_source_size = [1024, 1024]            # 国旗原始图片的大小
    flag_source_center = [1024 / 2, 1024 / 2]  # 国旗原始图片的中心
    logo_source_size = [256, 256]              # 2014巴西世界杯Logo原始图片的大小
    logo_source_center = [256 / 2, 256 / 2]    # 2014巴西世界杯Logo原始图片的中心
    for i in range(4):
        for j in range(8):
            index = i * 8 + j
            image_center = [j * image_size[0] + image_size[0] / 2, i * image_size[1] + image_size[1] / 2]
            if exposed[index]:
                canvas.draw_image(flag_image[all_image[index]], flag_source_center, flag_source_size,image_center,image_size)
            else:
                canvas.draw_image(logo_image, logo_source_center, logo_source_size, image_center, image_size)


# 创建窗口
# 16强共32张图片，每个图片的显示大小为128x128像素
# 32张图片显示为4行8列，因此窗口的宽度为128x8=1024像素，高度为128x4=512像素
frame = simplegui.create_frame("2014巴西世界杯16强连连看", 1024, 512)
frame.add_button("重新开始", new_game, 100)
label = frame.add_label("回合次数 = 0")

# 注册事件处理函数
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)


# 读取图片
logo_image = simplegui.load_image("images\\Logo.png")
flag_image.append(simplegui.load_image("images\\Algeria.png"))
flag_image.append(simplegui.load_image("images\\Argentina.png"))
flag_image.append(simplegui.load_image("images\\Belgium.png"))
flag_image.append(simplegui.load_image("images\\Brazil.png"))
flag_image.append(simplegui.load_image("images\\Chile.png"))
flag_image.append(simplegui.load_image("images\\Colombia.png"))
flag_image.append(simplegui.load_image("images\\Costa-rica.png"))
flag_image.append(simplegui.load_image("images\\France.png"))
flag_image.append(simplegui.load_image("images\\Germany.png"))
flag_image.append(simplegui.load_image("images\\Greece.png"))
flag_image.append(simplegui.load_image("images\\Mexico.png"))
flag_image.append(simplegui.load_image("images\\Netherlands.png"))
flag_image.append(simplegui.load_image("images\\Nigeria.png"))
flag_image.append(simplegui.load_image("images\\Switzerland.png"))
flag_image.append(simplegui.load_image("images\\Uruguay.png"))
flag_image.append(simplegui.load_image("images\\USA.png"))

# 启动游戏
new_game()
frame.start()
