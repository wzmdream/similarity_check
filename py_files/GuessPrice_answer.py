# -*- coding: utf-8 -*-
# 购物价游戏 - GuessPrice项目模板
# 通过按钮和文本框实现输入
# 所有和游戏相关的输出都显示在控制台上

'''
请在此处完善你个人的信息
学院：
班级：
学号：
姓名：

'''
import math
import simpleguitk as simplegui
import random
# 初始化全局变量
random_num = 0
num_range = 10
remain_time = 0

# 自定义函数，用于游戏和新一轮游戏的启动
def new_game():
    global random_num, num_range, remain_time
    remain_time = int(math.ceil(math.log(num_range + 1, 2)))
    print()
    print("欢迎来到购物街！")
    print("新一轮商品竞猜开始。竞猜价格范围从0到", num_range)
    print("总的竞猜机会有", remain_time,"次")
    random_num = random.randrange(0, num_range) 

# 为控制面板定义事件处理程序
def range10():
    #改变竞价范围[0,10)和重新启动游戏的按钮
    global num_range
    num_range = 10
    new_game()  
      
def range100():
    #改变竞价范围[0,100)和重新启动游戏的按钮
    global num_range
    num_range = 100
    new_game() 

def range1000():
    #改变竞价范围[0,1000)和重新启动游戏的按钮
    global num_range 
    num_range = 1000
    new_game() 
       
def input_guess(guess):
    global remain_time,random_num  
    #游戏主要的逻辑设计在这一部分    
    print( "")
    #print( "random num  is :",random_num)
    print( "还剩", remain_time,"次竞猜机会")
    print( "你报的竞猜价格是",guess,"元")
    remain_time = remain_time - 1
    
    if remain_time > 0:
        if  random_num == int(guess):
            print( "竞猜正确！")
            new_game()
        elif  random_num > int(guess):  
            print( "比实际价格低了") 
        else:
            print( "比实际价格高了") 
    else:
        if  random_num == int(guess):
            print( "竞猜正确！")
        else:
            print( "很遗憾，竞猜失败.商品的价格是 ", random_num)
        new_game()
    
# 创建框架
frame = simplegui.create_frame('价格竞猜', 300, 300)
# 为框架添加对象及处理事件
frame.add_button("第一件商品的竞猜价格是0~10元", range10, 200)
frame.add_button("第二件商品的竞猜价格是0~100元", range100, 200)
frame.add_button("第三件商品的竞猜价格是0~1000元", range1000, 200)
frame.add_input("输入竞猜价格", input_guess, 200)

# 调用new_game并且启动框架运行
new_game()
frame.start()

# 时刻记得根据得分标准检查你完成的程序

