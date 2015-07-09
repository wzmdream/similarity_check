#############################
# 
#      十二生肖过独木桥
#
#      设计者：陈燕红
#      单位：新疆农业大学
#      时间：2014年7月8日
# 
#############################

# -*- coding: utf-8 -*-
"""
请在此处完善你个人的信息
学院：
班级：
学号：
姓名：
"""

# “十二生肖过独木桥”游戏
# 子鼠、丑牛、寅虎、卯兔、辰龙、巳蛇、午马、未羊、申猴、酉鸡、戌狗、亥猪

# 该程序的关键点是把12生肖中的动物映射为以下数字
# 级别比较规则：不相邻生肖的级别均相同，相邻的两个生肖数字越大则级别越高，为了形成环形，特规定子鼠比亥猪的级别高）：
# 0 - 子鼠
# 1 - 丑牛
# 2 - 寅虎
# 3 - 卯兔
# 4 - 辰龙
# 5 - 巳蛇
# 6 - 午马
# 7 - 未羊
# 8 - 申猴
# 9 - 酉鸡
# 10 - 戌狗
# 11 - 亥猪


import random   # 包含random.randrange(startNumber, endNumber)函数的模块

# 用if/elif/else将name转换为对应数字代码，-1表示name无效
# name参数可以为"随机"、"子鼠"、"丑牛"、"寅虎"、"卯兔"、"辰龙"、"巳蛇"、"午马"、"未羊"、"申猴"、"酉鸡"、"戌狗"、"亥猪"
def name_to_code(name):
    if name == "随机":
        return random.randrange(0, 12)
    elif name =="子鼠":
        return 0
    elif name == "丑牛":
        return 1
    elif name == "寅虎":
        return 2
    elif name == "卯兔":
        return 3
    elif name == "辰龙":
        return 4
    elif name == "巳蛇":
        return 5
    elif name == "午马":
        return 6
    elif name == "未羊":
        return 7
    elif name == "申猴":
        return 8
    elif name == "酉鸡":
        return 9
    elif name == "戌狗":
        return 10
    elif name == "亥猪":
        return 11
    else:
        # 无效的name
        return -1


# 用if/elif/else将数字代码number转换为对应的字符名称，number无效时返回"所喊无效！"
def code_to_name(code):
    if code == 0:
        return "子鼠"
    elif code == 1:
        return "丑牛"
    elif code == 2:
        return "寅虎"
    elif code == 3:
        return "卯兔"
    elif code == 4:
        return "辰龙"
    elif code == 5:
        return "巳蛇"
    elif code == 6:
        return "午马"
    elif code == 7:
        return "未羊"
    elif code == 8:
        return "申猴"
    elif code == 9:
        return "酉鸡"
    elif code == 10:
        return "戌狗"
    elif code == 11:
        return "亥猪"
    else:
        # 无效的number
        return ("无效！")      

 
# 分别统计独木桥两端渡桥成功的动物数量          
east_count = 0 
west_count = 0

def ChineseZodiac_bridge(east_code, west_code):
    global east_count , west_count
    if east_code not in range(0,12):
        print (str(east_code) + "不是有效的十二生肖编码！")
        print()
        return
    
    if west_code not in range(0,12):
        print (str(west_code) + "不是有效的十二生肖编码！")
        print()
        return    
        
    east_name = code_to_name(east_code)
    west_name = code_to_name(west_code)
    print ("独木桥东头走来的是" + east_name )
    print ("独木桥西头走来的是" + west_name)
    
    # 计算east_code和west_code之差对12取模
    diff_mod_twelve = (east_code - west_code) % 12

    # 用if/elif/else判定哪边的动物可以过桥，并输出结果信息
    if diff_mod_twelve == 1:
        print (east_name + "比" + west_name + "级别高，" + east_name + "过桥了")
        east_count = east_count + 1  
    elif diff_mod_twelve == 11:
        print (west_name + "比" + east_name + "级别高，" + west_name + "过桥了")
        west_count = west_count + 1  
    else:
        # 独木桥两头走来的动物级别相同，则需要随机判定哪边来的动物需要回退，而另一边来的动物可以过桥（0代表东头来的动物需要回退；1代表西头来的动物需要回退）
        print ("独木桥两端走来的动物级别相同")
        rand_num = random.randrange(0, 2)
        if rand_num == 0:
            west_count = west_count + 1
            print("独木桥西边走来的" + west_name + "过桥了") 
        else:
            east_count = east_count + 1  
            print("独木桥西边走来的" + east_name + "过桥了") 
    print()
 
    

# 以下为测试代码，请在你提交的程序中保留以下代码    
def test_and_probability():    
    global east_count , west_count
    for i in range(1,5):
       east_code = random.randint(0,11); 
       west_code = random.randint(0,11); 
       
       print("*****************************************")
       print("*****************************************")
       print("第" + str(i) + "回合：")
      
       ChineseZodiac_bridge( east_code , west_code ) 
     
    print("*****************************************")
    print("*****************************************")         
    print("独木桥上共通过了" + str(i) + "只动物，其中：") 
    print("独木桥东边共通过了" + str(east_count) + "只动物，过桥率为" + str(int(float(east_count)/i*100)) +"%")
    print("独木桥西边共通过了" + str(west_count) + "只动物，过桥率为" + str(int(float(west_count)/i*100)) +"%")
    print()
       
test_and_probability()

print("*****************************************")
print("*****************************************")
print(0 , "对应的生肖是：" , code_to_name(0))
print(1 , "对应的生肖是：" , code_to_name(1))
print(2 , "对应的生肖是：" , code_to_name(2))
print(3 , "对应的生肖是：" , code_to_name(3))
print(4 , "对应的生肖是：" , code_to_name(4))
print(5 , "对应的生肖是：" , code_to_name(5))
print(6 , "对应的生肖是：" , code_to_name(6))
print(7 , "对应的生肖是：" , code_to_name(7))
print(8 , "对应的生肖是：" , code_to_name(8))
print(9 , "对应的生肖是：" , code_to_name(9))
print(10 , "对应的生肖是：" , code_to_name(10))
print(11 , "对应的生肖是：" , code_to_name(11))
print("随机产生的生肖是：" ,code_to_name(name_to_code("随机")))
print()

print("*****************************************")
print("*****************************************")
print("子鼠的编码是：" , name_to_code("子鼠" ))
print("丑牛的编码是：" , name_to_code("丑牛" ))
print("寅虎的编码是：" , name_to_code("寅虎" ))
print("卯兔的编码是：" , name_to_code("卯兔" ))
print("辰龙的编码是：" , name_to_code("辰龙" ))
print("巳蛇的编码是：" , name_to_code("巳蛇" ))
print("午马的编码是：" , name_to_code("午马" ))
print("未羊的编码是：" , name_to_code("未羊" ))
print("申猴的编码是：" , name_to_code("申猴" ))
print("酉鸡的编码是：" , name_to_code("酉鸡" ))
print("戌狗的编码是：" , name_to_code("戌狗" ))
print("亥猪的编码是：" , name_to_code("亥猪" ))
print("乌鸦的编码是：" , code_to_name("乌鸦" ))
print()

print("*****************************************")
print("*****************************************")
ChineseZodiac_bridge( 2 , 2 ) 
ChineseZodiac_bridge( 1 , 6 ) 
ChineseZodiac_bridge( 1 , 2 ) 
ChineseZodiac_bridge( 2 , 1 ) 
ChineseZodiac_bridge( 13 , 1 ) 
ChineseZodiac_bridge( 0 , 100 ) 

print("*****************************************")
print("*****************************************")
ChineseZodiac_bridge( name_to_code("丑牛") , name_to_code("丑牛") ) 
ChineseZodiac_bridge( name_to_code("午马") , name_to_code("未羊") ) 
ChineseZodiac_bridge( name_to_code("酉鸡") , name_to_code("卯兔") ) 
ChineseZodiac_bridge( name_to_code("酉鸡") , name_to_code("卯兔") ) 
ChineseZodiac_bridge( name_to_code("酉蛇") , name_to_code("卯兔") ) 
