'''
Created on 2014年7月10日

@author: ysy
说明：疯狂秒杀CrazyToSeckill的模板。
    主要练习：1.random模块生成随机数方法
        2.if-elif-else语句
        3.二分法查找法
        4.创建frame的方法
        5.添加按钮和文本框
        6.函数调用方法
        7、事件驱动
'''
import simpleguitk as simplegui
import random
import math
# 初始化全局变量
#定义三个变量，计算三种情况的剩余次数
one_digit_remain = 0
two_digit_remain = 0
three_digit_remain = 0

#定义三个变量，分别标记对应的按钮事件 
one_digit_flag = False
two_digit_flag = False
three_digit_flag = False

#定义三个变量，分别表示新的游戏开始时，三件物品的初始值
one_digit_init = [0,0,0]
two_digit_init = [0,0,0]
three_digit_init = [0,0,0]

#计算最大猜的次数,输入参数分别为猜测数字的最大值和最小值
def guess_number(num_range_low, num_range_high):
    guess_times = int(math.ceil(math.log(num_range_high - num_range_low + 1, 2)))
    return guess_times

#list转为字符串
def list_to_str(digit):
    return str(digit[0]) +  str(digit[1]) + str(digit[2])
#生成随机的三位数，并取出其各个位的数字
def BuildAnswer(): 
    #定义一个list，保存随机生成三位数的各个位上的数字
    answer = [0,0,0] 
    #采用random.seed方法，给随机数对象一个种子值，用于产生随机序列  
    random.seed() 
    #生成随机数，范围[1,999]
    digit = random.randint(1, 999) 
    
    #计算随机数各个位上的数字，保存在Answer中
    answer[0]=digit//100 #取百位数字
    answer[1]=digit%100//10 #取十位数字 
    answer[2] = digit%10 #取个位数字
    #返回answer
    return answer
# 定义游戏开始函数
def new_game():
    global one_digit_init, two_digit_init, three_digit_init
    global one_digit_remain ,one_digit_flag
    
    #调用 BuildAnswer，随机生成一个三位数，表示红米手机的价钱
    one_digit_init = BuildAnswer()

    #调用 BuildAnswer，随机生成一个三位数，表示华为荣耀手机的价钱
    two_digit_init = BuildAnswer()
    
    #调用 BuildAnswer，随机生成一个三位数，表示锤子手机的价钱
    three_digit_init = BuildAnswer()
    
    #计算范围 (0,10)时最大尝试次数 
    one_digit_remain = guess_number(0,10)
    #将控制one_digit_button的标志设为True
    one_digit_flag = True  
    
    #输出提示信息
    print('淘宝店庆疯狂秒杀开始了,请猜一猜红米手机的秒杀价是*'+str(one_digit_init[1])+str(one_digit_init[2])) 
    print('请输入您的数字.您总够有',str(guess_number(0,10)),'次机会') 
    print ("                                ")

#秒杀红米手机即猜测一个数字的事件处理函数    
def guess_one_digit():        
    global one_digit_init
    global one_digit_remain 
    global one_digit_flag,two_digit_flag,three_digit_flag
    #调用 BuildAnswer，随机生成一个三位数，表示红米手机的价钱
    one_digit_init = BuildAnswer()
    #计算最大尝试次数
    one_digit_remain = guess_number(0,10)
    
    #将控制one_digit_button的标识设为True，其他两个按钮标识设为False
    one_digit_flag = True
    two_digit_flag = False
    three_digit_flag = False 
    
    #利用set_text方法更新one_digit_button的text   
    mes = "猜一猜红米手机的秒杀价是*"+str(one_digit_init[1])+str(one_digit_init[2])+'?'
    one_digit_button.set_text(mes)
    print (mes)
    print ("该轮游戏您可以尝试的最大次数为 " + str(one_digit_remain) + "次 ")
    print (" ")
    
#猜两个数字的事件处理函数        
def guess_two_digit():  
    global two_digit_init
    global two_digit_remain 
    global one_digit_flag,two_digit_flag,three_digit_flag
  
    #调用 BuildAnswer，随机生成一个三位数，表示红米手机的价钱
    two_digit_init = BuildAnswer()
    
    #计算最大尝试次数
    two_digit_remain = guess_number(0,100)
    
    #将控制three_digit_button的标识设为True，其他两个按钮标识设为False
    one_digit_flag = False
    two_digit_flag = True
    three_digit_flag = False 
    
    #利用set_text方法更新two_digit_button的text  
    mes = "猜一猜华为荣耀6的秒杀价是**"+str(two_digit_init[2])+'?'
    two_digit_button.set_text(mes)
    #输出提示信息
    print (mes) 
    print ("该轮游戏您可以尝试的最大次数为 " + str(two_digit_remain) +"次 ")
    print (" ")  

#猜三个数字的事件处理函数            
def guess_three_digit():  
    global three_digit_init
    global three_digit_remain 
    global one_digit_flag,two_digit_flag,three_digit_flag
  
    #调用 BuildAnswer，随机生成一个三位数，表示锤子手机的价钱
    three_digit_init = BuildAnswer()
    #计算最大尝试次数
    three_digit_remain = guess_number(0,1000)
    
    #将控制three_digit_button的标识设为True，其他两个按钮标识设为False
    one_digit_flag = False
    two_digit_flag = False
    three_digit_flag = True 
    
    #打印提示信息  
    print ("猜一猜锤子手机的秒杀价是***?")
    print ("该轮游戏您可以尝试的最大次数为 " + str(three_digit_remain) + "次 ")
    print (" ")  
        
#文本输入框事件处理
def input_guess(guess):
    global one_digit_init,two_digit_init,three_digit_init
    global one_digit_flag, two_digit_flag, three_digit_flag    
    global one_digit_remain, two_digit_remain,three_digit_remain 
    
    #将字符串转成数字
    num = int(guess)
    
    if one_digit_flag :
        digit = int(list_to_str(one_digit_init))
        if num >=0 and num < 10 and one_digit_remain > 0:
            if num > one_digit_init[0]:
                print('您猜的数字太大了.')
            elif num < one_digit_init[0]:
                print('您猜的数字太小了.')             
            elif num == one_digit_init[0]:
                print("恭喜，猜对了，红米手机秒杀价为",str(digit))
                print (" ")
                guess_one_digit() 
                return;
            one_digit_remain = one_digit_remain - 1 
            if one_digit_remain == 0:
                print ("您没有猜对，请重新开始" )
                guess_one_digit()
                return
            else:
                print('您还有',str(one_digit_remain),'次机会') 
                print ("                                ")
        else:
            print('输入错误，范围应该在[0,10)之间.')
            return
    elif two_digit_flag :
        digit = int(list_to_str(two_digit_init))
        digit_tmp = int(str(two_digit_init[0]) + str(two_digit_init[1]))
        if num >=0 and num < 100 and two_digit_remain > 0:   
            if num > digit_tmp:
                print('您猜的数字太大了.')
            elif num < digit_tmp:
                print('您猜的数字太小了.')         
            elif num == digit_tmp:
                print("恭喜你，猜对了，华为荣耀6的秒杀价为",str(digit))
                print (" ")
                guess_two_digit() 
                return;
            two_digit_remain = two_digit_remain - 1 
            if two_digit_remain == 0:
                print ("您没有猜对，请重新开始" )
                guess_two_digit()
                return
            else:
                print('您还有',str(two_digit_remain),'次机会') 
                print ("                                ")
        else:
            print('输入错误，范围应该在[0,100)之间.')
            return
    elif three_digit_flag :  
        digit = int(list_to_str(three_digit_init))
        print(digit)
        if num >=0 and num < 1000 and three_digit_remain > 0:   
            if num > int(digit):
                print('您猜的数字太大了.')
            elif num < int(digit):
                print('您猜的数字太小了.')         
            elif num == int(digit):
                print("恭喜，猜对了，锤子手机秒杀价为",str(digit))
                print ("                                ")
                guess_three_digit() 
                return;
            three_digit_remain = three_digit_remain - 1 
            if three_digit_remain == 0:
                print ("您没有猜对，请重新开始" )
                print()
                guess_three_digit()
                return
            else:
                print('您还有',str(three_digit_remain),'次机会') 
                print ("                                ")  
        else:
            print('输入错误，范围应该在[0,1000)之间.')
            return
# 创建 frame
frame = simplegui.create_frame("疯狂秒杀", 200, 200)

# 调用new_game()，开始游戏
new_game()

# 添加按钮，注册事件触发句柄
one_digit_button = frame.add_button("猜一猜红米手机的秒杀价是*"+str(one_digit_init[1])+str(one_digit_init[2])+'?',guess_one_digit, 200)
two_digit_button =frame.add_button('猜一猜华为荣耀6的秒杀价是**'+str(two_digit_init[2])+'?',guess_two_digit, 200)
three_digit_button =frame.add_button("猜一猜锤子手机的秒杀价是***?",guess_three_digit, 200)
frame.add_input("输入您的数字", input_guess, 200)

frame.start()
