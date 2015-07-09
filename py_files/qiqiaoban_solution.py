# -*- coding: utf-8 -*-

import simpleguitk as simplegui
from copy import deepcopy
import math

## 定义常量
# 画布的尺寸
WIDTH = 600
HEIGHT = 600
L = 200

# 10个顶点坐标
POINTS = [[0, 0], [L, 0], [L*0.75, L*0.25], [L/2, L/2], [L*0.25, L*0.75],
          [0, L], [L, L/2], [L*0.75, L*0.75], [L/2, L], [L, L]]

# 形状名称
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

class Shape():
    def __init__(self, name):
        self.name = name
        self.color = COLOR[self.name]
        self.points = deepcopy(COORDINATE[self.name]) # 深度拷贝
        self.selected = False
        self.move_startpoint = None
        # 计算中心坐标。即取所有顶点的坐标的平均值
        self.center = [0, 0]
        for point in self.points:
            self.center[0] += point[0]
            self.center[1] += point[1]
        self.center[0] /= len(self.points)
        self.center[1] /= len(self.points)
    
    def draw(self, canvas):
        if self.selected:
            edge_color = "Black"
            edge_width = 3
        else:
            edge_color = self.color
            edge_width = 1
        canvas.draw_polygon(self.points, edge_width, edge_color, fill_color = self.color) 
        
    def move(self, move_endpoint):
        dx = move_endpoint[0] - self.move_startpoint[0]
        dy = move_endpoint[1] - self.move_startpoint[1]
        for point in self.points:
            point[0] += dx
            point[1] += dy
        self.center[0] += dx
        self.center[1] += dy
        self.move_startpoint = move_endpoint # 关键语句
        
    def rotate(self, degree):
        if degree == 0:
            return
        angle_inc = math.pi / 180 * degree # 角度转换成弧度
        for point in self.points:
            if point[0] == self.center[0]: # 避免除零异常
                if point[1] < self.center[1]: # 判断角度是 90度 还是 -90度
                    angle = -math.pi / 2 + angle_inc
                else:
                    angle = math.pi / 2 + angle_inc
            else:
                angle = math.atan2((point[1]-self.center[1]) , (point[0]-self.center[0])) + angle_inc
                
            length = math.sqrt((point[1]-self.center[1])**2 + (point[0]-self.center[0])**2)
            point[0] = math.cos(angle) * length + self.center[0]
            point[1] = math.sin(angle) * length + self.center[1]

# 绘制画布
def draw(canvas):
    for shape in SHAPES:
        shape.draw(canvas)

# 把七巧板恢复到初始状态
def init():
    global SHAPES, selected_shape
    selected_shape = None
    SHAPES.clear()
    for shape_name in SHAPE_NAME:
        SHAPES.append(Shape(shape_name))
    
def cosine_law(A, B, C): # 余弦定理
    a = math.sqrt((B[0] - C[0])**2 + (B[1] - C[1])**2)
    b = math.sqrt((A[0] - C[0])**2 + (A[1] - C[1])**2)
    c = math.sqrt((A[0] - B[0])**2 + (A[1] - B[1])**2)
    return math.acos((b**2 + c**2 - a**2)/2/b/c)
    
    
def get_shape(pos):
    global SHAPES
    for shape in SHAPES:
        total_angle = 0
        A = pos
        for i, point in enumerate(shape.points):
            B = point
            C = shape.points[0] if i == len(shape.points)-1 else  shape.points[i+1]
            total_angle += cosine_law(A, B, C)
        if abs(total_angle - 2 * math.pi) < 1e-3:
            return shape
    return None

def deselect():
    global SHAPES
    for shape in SHAPES:
        shape.selected = False        

def click(pos):
    global selected_shape
    selected_shape = get_shape(pos)
    if selected_shape is None:
        deselect()
        return
    
    deselect()
    selected_shape.selected = True
    selected_shape.move_startpoint = pos
    
    # 把选中的图像放到列表最后一个位置，使得它显示在最上面
    idx = SHAPES.index(selected_shape)
    temp = SHAPES[idx]
    SHAPES[idx] =  SHAPES[-1]
    SHAPES[-1] = temp
          
    
def drag(pos):
    global selected_shape
    if selected_shape is None:
        return
    selected_shape.move(pos)
    
def keydown(key):
    global selected_shape
    coarse_tuning = 90 # 粗调
    fine_tuning = 1 # 细调
    if selected_shape is not None:
        if key == simplegui.KEY_MAP['left']:
            selected_shape.rotate(-fine_tuning)
        if key == simplegui.KEY_MAP['right']:
            selected_shape.rotate(fine_tuning)
        if key == simplegui.KEY_MAP['up']:
            selected_shape.rotate(-coarse_tuning)
        if key == simplegui.KEY_MAP['down']:
            selected_shape.rotate(coarse_tuning)

##def keyup(key):
##    global selected_shape
##    if selected_shape is not None:
##        if key in [simplegui.KEY_MAP['left'], simplegui.KEY_MAP['right'], simplegui.KEY_MAP['up'], simplegui.KEY_MAP['down']]:      
##            selected_shape.rotate(0)
            
    
# 创建用户界面
frame = simplegui.create_frame("七巧板", WIDTH, HEIGHT)
frame.set_canvas_background("White")
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(click)
frame.set_mousedrag_handler(drag)
frame.set_keydown_handler(keydown)
#frame.set_keyup_handler(keyup)

# 创建按钮
frame.add_button("重新开始", init, 80)

init()
frame.start()
