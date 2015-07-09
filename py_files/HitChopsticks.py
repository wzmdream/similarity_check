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
    pass


def number_to_name(number):
    # 用if/elif/else将数字代码number转换为对应的字符名称，number无效时返回"所喊无效！"
    pass   
    
# name参数可以为“随机”、“杠子”、“老虎”、“鸡”或“虫子”,返回对应喊拳的数字代码
def shout_out(name):
    pass
        
def play_one_round(player1_name, player1_code, player2_name, player2_code, print_msg = True):
    pass

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