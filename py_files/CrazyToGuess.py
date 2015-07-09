'''
Created on 2014年7月10日

@author: ysy
说明：疯狂猜物价CrazyToGuess的模板。
    主要练习：1.random模块生成随机数方法
        2.if-elif-else语句
        3.while循环
        4.二分法查找方法
        5.python控制台输入输出方法
        6.函数调用方法
'''

import random
import math

choice = 0
Answer=[0,0,0] 
AttemptTimes=0 
digit=0
guessesTaken = 0
#计算最大猜的次数,输入参数分别为猜测数字的最大值和最小值
def guess_number(num_range_low, num_range_high):
    guess_times = int(math.ceil(math.log(num_range_high - num_range_low + 1, 2)))
    return guess_times

def BuildAnswer():  
    global Answer ,digit   
    random.seed() 
    digit = random.randint(1, 999) 

    Answer[0]=math.trunc(digit/100) #取百位数字
    Answer[1]=math.trunc(digit%100/10) #取十位数字 
    Answer[2] = digit%10 #取个位数字

def guess_one_digit(Answer):  
    global guess,guessesTaken,digit
    guess_times = guess_number(0,10)
    while guess_times > 0:
        guess = input()
        guess = int(guess)
    
        guess_times = guess_times - 1
    
        if guess < Answer[0]:
            print('您猜的数字太小了.') 
            print('您还有',str(guess_times),'次机会')
    
        if guess > Answer[0]:
            print('您猜的数字太大了.')
            print('您还有',str(guess_times),'次机会')
        if guess == Answer[0]:
            print("恭喜你，猜对了，红米手机秒杀价为",digit)
            break 
    if guess != Answer[0]:
        digit = str(digit)
        print('对不起. 您没有猜对，红米手机秒杀价格为',digit)      
def guess_two_digit(Answer):  
    global guess,guessesTaken,digit
    guess_times = guess_number(0,100)
    while guess_times > 0:
        guess = input()
        #guess = int(guess)  
        guess_times = guess_times - 1
    
        if guess < str(Answer[0])+str(Answer[1]):
            print('您猜的数字太小了.') 
            print('您还有',str(guess_times),'次机会')
    
        if guess > str(Answer[0])+str(Answer[1]):
            print('您猜的数字太大了.')
            print('您还有',str(guess_times),'次机会')
    
        if guess == str(Answer[0])+str(Answer[1]):
            print("恭喜你，猜对了，华为荣耀6秒杀价为",digit)
            break 
    if guess != str(Answer[0])+str(Answer[1]):
        digit = str(digit)
        print('对不起. 您没有猜对，华为荣耀6秒杀价格为',digit)  
            
def guess_three_digit():  
    global guess,guessesTaken,digit
    guess_times = guess_number(0,100)
    while guess_times > 0:
        guess = input()
        guess = int(guess)
    
        guess_times = guess_times - 1
    
        if guess < digit:
            print('您猜的数字太小了.') 
            print('您还有',str(guess_times),'次机会')
    
        if guess > digit:
            print('您猜的数字太大了.')
            print('您还有',str(guess_times),'次机会')
        if guess == digit:
            print("恭喜你，猜对了，锤子手机秒杀价为",digit)
            break  
    if guess != digit:
        digit = str(digit)
        print('对不起. 您没有猜对，锤子手机秒杀价格为',digit)   
def crazy_to_guess(): 
    #生成1或者2或者3
    global choice,Answer
    BuildAnswer()
    choice = random.randint(1,3)    
    choice = 1      
    if choice == 1:
        print('淘宝店庆疯狂秒杀开始了,请猜一猜红米手机的秒杀价是*'+str(Answer[1])+str(Answer[2])) 
        print('请输入您的数字.您总够有',str(guess_number(0,10)),'次机会') 
        guess_one_digit(Answer)
    elif choice == 2:
        print('淘宝店庆疯狂秒杀开始了,请猜一猜华为荣耀6的秒杀价是**',str(Answer[2]),'呢.') 
        print('请输入您的数字.您总够有',str(guess_number(0,100)),'次机会')
        guess_two_digit(Answer)
    else:
        print('淘宝店庆疯狂秒杀开始了,请猜一猜锤子手机的秒杀价是多少呢.') 
        print('请输入您的数字.范围在1到1000之间，您总够有',str(guess_number(0,1000)),'次机会') 
        guess_three_digit()
        
crazy_to_guess()