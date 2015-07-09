
'''
Created on 2014年7月5日

@author: ysy

说明：小游戏Guess的模板，需要用到按钮和输入框控件，所有 的输出信息都将打印输出到控制台。
    主要练习：1.random模块生成随机数方法
        2.if-elif-else语句
        3.二分法
        4.frame创建方法
        5.添加button和文本输入框input控件的方法
        6.函数调用方法
'''

import simpleguitk as simplegui
import random
import math
# 初始化全局变量
remain_range10 = 0
remain_range100 = 0
remain_range1000 = 0
rand1 = random.randrange(0, 10)
rand2 = random.randrange(0, 100)
rand3 = random.randrange(0, 1000)  

#定义三个变量，分别标记对应的按钮事件 
range10_flag = False
range100_flag = False
range1000_flag = False

#计算最大猜的次数,输入参数分别为猜测数字的最大值和最小值
def guess_number(num_range_low, num_range_high):
    guess_times = int(math.ceil(math.log(num_range_high - num_range_low + 1, 2)))
    return guess_times
# 定义游戏开始函数，默认范围为0-100之间
def new_game():
    global range10_flag, remain_range10    
    print ("猜测树上有几只小麻雀？数字范围是 0 - 10。")
    print ("该轮游戏您可以尝试的最大次数为 4次 ")
    print ("                                ")
    remain_range10 = guess_number(0,10)
    range10_flag = True
    
# 定义按钮事件，将数字范围改变到[0,100)，并且重新开始游戏
def range10():
    print ("猜测树上有几只小麻雀？数字范围是 0 - 10。")
    print ("该轮游戏您可以尝试的最大次数为 4次 ")
    print ("                                ")
    
    global rand1, remain_range10    
    global range10_flag, range100_flag, range1000_flag
    
    rand1 = random.randrange(0, 10)
    remain_range10 = guess_number(0,10)
    
    range10_flag = True
    range100_flag = False
    range1000_flag = False
# 定义按钮事件，将数字范围改变到[0,100)，并且重新开始游戏
def range100():
    print ("猜猜糖罐里有多少颗大白兔奶糖。数字范围是 0 - 100。")
    print ("该轮游戏您可以尝试的最大次数为 7次 ")
    print ("                                ")
    
    global rand2,remain_range100
    global range10_flag, range100_flag, range1000_flag
    
    rand2 = random.randrange(0, 100)
    remain_range100 = guess_number(0,100)
    
    range100_flag = True
    range10_flag = False
    range1000_flag = False

# 定义按钮事件，将数字范围改变到[0,1000)，并且重新开始游戏  
def range1000():   
    print ("猜猜池塘里有多少只小蝌蚪。数字范围是 0 - 1000。")
    print ("该轮游戏您可以尝试的最大次数为 10次")
    print ("                                ")
    
    global rand3, remain_range1000
    global range10_flag, range100_flag, range1000_flag
    
    rand3 = random.randrange(0, 1000)
    remain_range1000 = guess_number(0,1000)
    
    range1000_flag = True
    range100_flag = False
    range10_flag = False
    
#文本输入框事件处理
def input_guess(guess):
    global remain_range10, remain_range100, remain_range1000
    global range10_flag, range100_flag, range1000_flag
    
    num = int(guess)
    if range10_flag :
        if num >=0 and num < 10 and remain_range10 > 0:
            if num > rand1:
                print('您猜的数字太大了.') 
            elif num < rand1:
                print('您猜的数字太小了.') 
            elif num == rand1:
                print ("恭喜您，猜对了")
                print ("                                ")
                range10() 
                return;
            remain_range10 = remain_range10 - 1 
            if remain_range10 == 0:
                print ("您没有猜对，请重新开始" )
                range10()
                return
            else:
                print ("游戏剩余次数 " , remain_range10 ) 
                print ("                                ")
        else:
            print('输入错误，范围应该在[0,10)之间.')
            return
    elif range100_flag :
        print(remain_range100)
        if num >=0 and num < 100 and remain_range100 > 0:   
            if num > rand2:
                print('您猜的数字太大了.') 
            elif num < rand2:
                print('您猜的数字太小了.') 
            elif num == rand2:
                print ("恭喜您，猜对了")
                print ("                                ")
                range100() 
                return;
            remain_range100 = remain_range100 - 1 
            if remain_range100 == 0:
                print ("您没有猜对，请重新开始" )
                range100()
                return
            else:
                print ("游戏剩余次数 " , remain_range100 )
                print ("                                ")
        else:
            print('输入错误，范围应该在[0,100)之间.')
            return
    elif range1000_flag :
        if num >=0 and num < 10000 and remain_range1000 > 0:   
            if num > rand3:
                print('您猜的数字太大了.') 
            elif num < rand3:
                print('您猜的数字太小了.') 
            elif num == rand3:
                print ("恭喜你，猜对了")
                print ("                                ")
                range1000() 
                return;
            remain_range1000 = remain_range1000 - 1 
            if remain_range1000 == 0:
                print ("您没有猜对，请重新开始" )
                range1000()
                return
            else:
                print ("游戏剩余次数 " , remain_range1000 )
                print ("                                ")
        else:
            print('输入错误，范围应该在[0,1000)之间.')
            return
        
# 创建一个 frame
frame = simplegui.create_frame("猜一猜", 200, 200)

# 注册事件触发句柄
frame.add_button("猜猜 树上有几只小麻雀( [0,10))？ ",range10, 200)
frame.add_button("猜猜糖罐里有多少颗大白兔奶糖([0,100))？",range100, 200)
frame.add_button("猜猜池塘里有多少只小蝌蚪( [0,1000))？",range1000, 200)
frame.add_input("输入您的数字", input_guess, 200)

# 调用new_game()，开始游戏
new_game()

frame.start()