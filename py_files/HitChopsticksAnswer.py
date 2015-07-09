# -*- coding: utf-8 -*-
"""
请在此处完善你个人的信息
学院：
班级：
学号：
姓名：
"""

# “杠子老虎鸡虫”游戏

# 该程序的关键点是把“虫子”、“鸡”、“老虎”、“杠子”映射为以下数字：
# 0 - 虫子
# 1 - 鸡
# 2 - 老虎
# 3 - 杠子

import random   # 包含random.randrange(start, stop)函数的模块

# 辅助函数
def name_to_number(name):
    # 用if/elif/else将name转换为对应数字代码，-1表示name无效
    if name =="虫子":
        return 0
    elif name == "鸡":
        return 1
    elif name == "老虎":
        return 2
    elif name == "杠子":
        return 3
    else:
        # 无效的name
        return -1


def number_to_name(number):
    # 用if/elif/else将数字代码number转换为对应的字符名称，number无效时返回"所喊无效！"
    if number == 0:
        return "虫子"
    elif number == 1:
        return "鸡"
    elif number == 2:
        return "老虎"
    elif number == 3:
        return "杠子"
    else:
        # 无效的number
        return ("所喊无效！")      
    
# name参数可以为“随机”、“杠子”、“老虎”、“鸡”或“虫子”
def shout_out(name):
    number = -1
    if name == "随机":
        number = random.randrange(0, 4)
    else:
        number = name_to_number(name)
    #play_sound(number)  #播放音效，有兴趣的同学可以尝试实现次函数
    return number
        
def play_one_round(player1_name, player1_code, player2_name, player2_code, print_msg = True):
    if print_msg == True:
        print("") # 输出空白行
    if player1_code == -1 or player1_code > 3:
        if print_msg == False:
            print("") # 输出空白行
        print (player1_name + "所喊无效！")
        return
    if player2_code == -1 or player2_code > 3:
        if print_msg == False:
            print("") # 输出空白行
        print (player2_name + "所喊无效！")
        return        
    player1_choice = number_to_name(player1_code)
    player2_choice = number_to_name(player2_code)
    if print_msg == True:
        print (player1_name + "喊的为：" + player1_choice)
        print (player2_name + "喊的为：" + player2_choice)
    
    # 计算player1_code和player2_code之差对4的模
    diff_mod_four = (player1_code - player2_code) % 4

    # 用if/elif/else判定输赢结果，并输出结果信息
    if diff_mod_four == 0 or diff_mod_four == 2:
        if print_msg == True:
            print ( player1_name + "和" + player2_name + "打成平手！")
        return 0
    elif diff_mod_four == 1:
        if print_msg == True:
            print ("%s获胜！" % player1_name)
        return 1
    else:
        if print_msg == True:
            print ("%s获胜！" % player2_name)
        return 2
def result_probability():
    #变量声明及初始化
    play_times = 0           # 对决总次数
    player1_win_times = 0    # 甲方获胜次数
    player1_loss_times = 0   # 甲方失败次数
    tie_times = 0            # 双方平局次数
    
    # 第1次对决
    result = play_one_round("甲", shout_out("随机"), "乙", shout_out("随机"), False)
    play_times = play_times + 1 
    if result == 0:
        tie_times = tie_times + 1
    elif result == 1:
        player1_win_times = player1_win_times + 1
    else:
        player1_loss_times = player1_loss_times + 1

    # 第2次对决
    result = play_one_round("甲", shout_out("随机"), "乙", shout_out("随机"), False)
    play_times = play_times + 1 
    if result == 0:
        tie_times = tie_times + 1
    elif result == 1:
        player1_win_times = player1_win_times + 1
    else:
        player1_loss_times = player1_loss_times + 1
        
    # 第3次对决
    result = play_one_round("甲", shout_out("随机"), "乙", shout_out("随机"), False)
    play_times = play_times + 1 
    if result == 0:
        tie_times = tie_times + 1
    elif result == 1:
        player1_win_times = player1_win_times + 1
    else:
        player1_loss_times = player1_loss_times + 1

    # 第4次对决
    result = play_one_round("甲", shout_out("随机"), "乙", shout_out("随机"), False)
    play_times = play_times + 1 
    if result == 0:
        tie_times = tie_times + 1
    elif result == 1:
        player1_win_times = player1_win_times + 1
    else:
        player1_loss_times = player1_loss_times + 1
        
    #你可以在这里添加更多的对决来验证概率理论计算的结果   
   
   
    player1_win_prob  = player1_win_times / play_times    # 甲方获胜概率
    tie_prob  = tie_times / play_times                    # 双方平局概率
    player1_loss_prob  = player1_loss_times / play_times  # 甲方失败概率
    print("") # 输出空白行
    print("甲乙随机比赛"+str(play_times)+"次，验证对决结果的概率为：")
    print("甲方获胜的概率为：" + str(player1_win_prob))
    print("双方平局的概率为：" + str(tie_prob))
    print("甲方失败的概率为：" + str(player1_loss_prob))


# 以下为测试代码，请在你提交的程序中保留以下代码
result1 = play_one_round("计算机", 1, "玩家", 1)
result2 = play_one_round("张太红", 2, "白涛", 3)
result3 = play_one_round("甲", 3, "乙", 1)
result4 = play_one_round("A", 2, "B", 1)
play_one_round("A", 4, "B", 1)
play_one_round("张太红", shout_out("随机"), "白涛", shout_out("随机"))
play_one_round("张太红", shout_out("老虎"), "白涛", shout_out("虫子"))
print(play_one_round("计算机", shout_out("随机"), "糊涂玩家", shout_out("豹子"), False))
print(play_one_round("计算机", shout_out("随机"), "糊涂玩家", shout_out("豹子")))

result_probability()
#print(shout_out("杠子"))
#print(shout_out("老虎"))
#print(shout_out("鸡"))
#print(shout_out("虫子"))
#print(shout_out("苍蝇"))
#print(shout_out("随机"))
