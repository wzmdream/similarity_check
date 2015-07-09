# -*- coding: utf-8 -*-

import simpleguitk as simplegui
from copy import deepcopy
import math

## 定义常量
# 画布的尺寸和大正方形边长
WIDTH = 600
HEIGHT = 600
L = 200

# 10个顶点的初始坐标
POINTS = [[0, 0], [L, 0], [L*0.75, L*0.25], [L/2, L/2], [L*0.25, L*0.75],
          [0, L], [L, L/2], [L*0.75, L*0.75], [L/2, L], [L, L]]

# 七个形状的名称
SHAPE_NAME = ('s1', 's2', 's3', 's4', 's5', 's6', 's7')

# 7个形状对应的顶点
COORDINATE = {SHAPE_NAME[0] : [POINTS[3], POINTS[0], POINTS[1]],
              SHAPE_NAME[1] : [POINTS[3], POINTS[5], POINTS[0]],
              SHAPE_NAME[2] : [POINTS[2], POINTS[1], POINTS[6]],
              SHAPE_NAME[3] : [POINTS[2], POINTS[6], POINTS[7], POINTS[3]],
              SHAPE_NAME[4] : [POINTS[3], POINTS[7], POINTS[4]],
              SHAPE_NAME[5] : [POINTS[4], POINTS[7], POINTS[8], POINTS[5]],
              SHAPE_NAME[6] : [POINTS[9], POINTS[8], POINTS[6]]}

# 7个形状对应的颜色
COLOR = {SHAPE_NAME[0]:'Aqua', SHAPE_NAME[1]:'Blue', SHAPE_NAME[2]:'Red', SHAPE_NAME[3]:'Lime', 
         SHAPE_NAME[4]:'Purple', SHAPE_NAME[5]:'Orange', SHAPE_NAME[6]:'Yellow'}

SHAPES = []
selected_shape = None


# Shape 类描述七巧板里的一个图形
class Shape():
    def __init__(self, name):
        self.name = name
        self.color = COLOR[self.name]
        self.points = deepcopy(COORDINATE[self.name])   # 用深度拷贝得到顶点坐标的一个副本
        self.selected = False
        self.move_startpoint = None
        self.center = [0, 0]    # 计算图形的中心坐标，即取所有顶点坐标的平均值
        for point in self.points:
            self.center[0] += point[0]
            self.center[1] += point[1]
        self.center[0] /= len(self.points)
        self.center[1] /= len(self.points)

    def __str__(self):
        return self.name
    
    def draw(self, canvas):
        pass 
        
    def move(self, move_endpoint):
        # 顶点和中心坐标都需要移动
        pass
        
    def rotate(self, degree):
        pass


# 把七巧板恢复到初始状态
def play():
    global SHAPES, selected_shape
    pass


# 鼠标点击事件响应函数
def click(pos):
    global selected_shape
    selected_shape = get_shape(pos)
    # 函数其它代码写在这里
    pass


# 判定点击的是哪个图形    
def get_shape(pos):
    global SHAPES
    # 该函数对 SHAPES 列表里的图形依次计算，判断玩家点击的是哪个图形
    # 当图形有重叠是，会有多个图形满足要求，你只需要返回其中一个图形
    # 若没有图形满足要求，返回 None
    pass


# 余弦定理    
def cosine_law(PQ, PR, QR):
    # 函数应返回一个内角的角度
    pass


# 绘制画布
def draw(canvas):
    pass

          
# 鼠标拖拽事件响应函数    
def drag(pos):
    pass


# 键盘事件响应函数    
def keydown(key):
    pass

    
# 创建用户界面
frame = simplegui.create_frame("七巧板", WIDTH, HEIGHT)
frame.set_canvas_background("White")
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(click)
frame.set_mousedrag_handler(drag)
frame.set_keydown_handler(keydown)

# 创建按钮
frame.add_button("重新开始", play, 80)

play()
frame.start()
