'''
Created on 2014年7月5日

@author: ysy

说明：小游戏Guess的模板。
    主要练习：1.random模块生成随机数方法
        2.if-elif-else语句
        3.while循环
        4.二分法查找方法
        5.控制台输入输出方法
        6.函数调用方法
'''

import random
import math
guessesTaken = 0
guess = 0

print('您好! 请问您叫什么名字？')
myName = input()
  
#计算最大猜的次数,输入参数分别为猜测数字的最大值和最小值
def guess_number(num_range_low, num_range_high):
    guess_times = int(math.ceil(math.log(num_range_high - num_range_low + 1, 2)))
    return guess_times

def guess100(number):  
    global guess,guessesTaken
    #print (guess_number(0,100))
    while guessesTaken < guess_number(0,100):
        print('请输入您的数字.') 
        guess = input()
        guess = int(guess)
    
        guessesTaken = guessesTaken + 1
    
        if guess < number:
            print('您猜的数字太小了.') 
    
        if guess > number:
            print('您猜的数字太大了.')
    
        if guess == number:
            break
def guess1000(number):
    global guess,guessesTaken  
    #print (guess_number(0,1000))
    while guessesTaken < guess_number(0,1000):
        print('请输入您的数字.') 
        guess = input()
        guess = int(guess)
    
        guessesTaken = guessesTaken + 1
    
        if guess < number:
            print('您猜的数字太小了.') 
    
        if guess > number:
            print('您猜的数字太大了.') 
    
        if guess == number:
            break   
def guess_and_guess(): 
    #生成1或者2随机数
    choice = random.randint(1,2)             
    if choice == 1:
        number = random.randint(1,100)
        print('你好, ' + myName + ',  我想了一个1到100之间的数字快来猜一猜吧，你只有7次机会哦.')
        guess100(number)
    else:
        number = random.randint(1,1000)
        print('你好, ' + myName + ',  我想了一个1到1000之间的数字快来猜一猜吧，你只有10次机会哦.')
        guess1000(number)
    give_result(number)
    
def give_result(number):       
    if guess == number:
        guessesTaken = str(guessesTaken)
        print('恭喜, ' + myName + '! 你总共用了 ' + guessesTaken + ' 次机会猜对了!')
    
    if guess != number:
        number = str(number)
        print('对不起. 我心里想的数字是 ' + number)

guess_and_guess()
    