# -*- coding: utf-8 -*-
import simpleguitk as simplegui
import math
import random

## 定义常量
# 画布的尺寸
WIDTH = 450
HEIGHT = 600
SIZE = 30
STEP = SIZE
TIME_INTERVAL = 1000

# 形状名称及其组成方块的偏移量
SHAPES = ['s1','s2','s3','s4','s5','s6','s7']

OFFSET = {'s1':[[0, -2*SIZE], [0, -SIZE], [0, SIZE]],
          's2':[[0, -SIZE], [0, SIZE], [SIZE, SIZE]],
          's3':[[0, -SIZE], [0, SIZE], [-SIZE, SIZE]],
          's4':[[0, -SIZE], [SIZE, 0], [SIZE, SIZE]],
          's5':[[SIZE, -SIZE], [SIZE, 0], [0, SIZE]],
          's6':[[SIZE, 0], [0, SIZE], [SIZE, SIZE]],
          's7':[[-SIZE, 0], [0, -SIZE], [SIZE, 0]]}

COLORS = ['Aqua', 'Blue', 'Red', 'Lime', 'Purple', 'Orange', 'Yellow']

inplay = False
grid = None
current_shape = None
score = 0

# 描述单个方块
class Square:
    def __init__(self, center, color, father):
        self.center = center
        self.row = int(self.center[1] // SIZE)
        self.col = int(self.center[0] // SIZE)
        self.color = color
        self.father = father
        self.relocate()
        
    def __str__(self):
        pass
               
    def draw(self, canvas):
        canvas.draw_polygon(self.points, 1, self.color, fill_color = self.color) 
        
    def relocate(self):
        self.points = [[self.center[0]-SIZE/2, self.center[1]-SIZE/2], 
                       [self.center[0]+SIZE/2, self.center[1]-SIZE/2], 
                       [self.center[0]+SIZE/2, self.center[1]+SIZE/2], 
                       [self.center[0]-SIZE/2, self.center[1]+SIZE/2]]
        self.row = int(self.center[1] // SIZE)
        self.col = int(self.center[0] // SIZE)
        
    def move(self, direction, grid):
        if direction == 'down':
            self.center[1] += STEP
        elif direction == 'left':
            self.center[0] -= STEP
        elif direction == 'right':
            self.center[0] += STEP
        self.relocate()
        grid.update(self)

# 描述一个形状
class Shape:
    def __init__(self, name, center, color):
        self.freeze = False
        self.name = name
        self.center = center
        self.color = color
        self.squares = [Square(self.center, self.color, id(self))] #  首元素是移动/旋转的参考方块
        for offset in OFFSET[self.name]:
            self.squares.append(Square([self.center[0]+offset[0], self.center[1]+offset[1]], self.color, id(self)))       
            
    def move_capable(self, direction, grid):
        try:
            if direction == 'down':
                for square in self.squares:
                    if grid.square_ref[square.row+1][square.col] is not None \
                        and grid.square_ref[square.row+1][square.col].father != id(self):
                        return False               
            if direction == 'left':
                for square in self.squares:
                    if square.col-1 < 0:
                        raise
                    if grid.square_ref[square.row][square.col-1] is not None \
                        and grid.square_ref[square.row][square.col-1].father != id(self):
                        return False
            if direction == 'right':
                for square in self.squares:
                    if grid.square_ref[square.row][square.col+1] is not None \
                        and grid.square_ref[square.row][square.col+1].father != id(self):
                        return False
        except:
            return False
        else:
            return True
             
    def clear_trace(self, grid):
        for square in self.squares:
            if square.row < 0:
                continue
            grid.square_ref[square.row][square.col] = None       
    
    def move(self, direction, grid):
        if not self.freeze:
            if self.move_capable(direction, grid):
                self.clear_trace(grid)
                for square in self.squares:
                    square.move(direction, grid)
                                
    
    def rotate(self, grid): # 顺时针方向
        if not self.freeze:
            new_location = []
            for square in self.squares:
                if square.center[0] == self.center[0]: # 避免除零异常
                    if square.center[1] < self.center[1]: # 判断角度是 90度 还是 -90度
                        angle = 0
                    else:
                        angle = math.pi
                else:
                    angle = math.atan2((square.center[1]-self.center[1]) , (square.center[0]-self.center[0])) + math.pi/2
                length = math.sqrt((square.center[1]-self.center[1])**2 + (square.center[0]-self.center[0])**2)
                new_location.append([math.cos(angle) * length + self.center[0], math.sin(angle) * length + self.center[1]])
            try:
                for loc in new_location:
                    if loc[0]//SIZE < 0:
                        raise
                    if grid.square_ref[int(loc[1]//SIZE)][int(loc[0]//SIZE)] is not None \
                            and grid.square_ref[int(loc[1]//SIZE)][int(loc[0]//SIZE)].father != id(self):
                            raise
            except:
                return
            else:
                self.clear_trace(grid)
                for square, loc in zip(self.squares, new_location):
                    square.center[0] = loc[0]
                    square.center[1] = loc[1]
                    square.relocate()
                    grid.update(square)
                    
class Grid:
    def __init__(self):
        self.square_ref = []
        self.rows = int(HEIGHT/SIZE)
        self.cols = int(WIDTH/SIZE)
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(None)
            self.square_ref.append(row)
            
    def __str__(self):
        pass
            
    def update(self, square):
        if square.row < 0:
            return
        self.square_ref[square.row][square.col] = square
    
    def draw(self, canvas):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.square_ref[i][j] is not None:
                    self.square_ref[i][j].draw(canvas)     
                    
    def refresh(self):
        global score
        for i in range(self.rows):
            if all(self.square_ref[i]):
                score += 10
                for j in range(self.cols):
                    self.square_ref[i][j] = None
                for p in range(i-1, -1, -1): # 下移一层
                    for j in range(self.cols):
                        if self.square_ref[p][j] is not None:
                            self.square_ref[p][j].center[1] += SIZE
                            self.square_ref[p][j].relocate()
                            self.square_ref[p+1][j] = self.square_ref[p][j]
                            self.square_ref[p][j] = None
       
        
# 绘制画布
def draw(canvas):
    grid.draw(canvas)
    canvas.draw_text('得分：' + str(score), [20, 40], 15, 'White')
    
def create_shape():
    shape = SHAPES[random.randrange(len(SHAPES))]
    cols = WIDTH / SIZE
    location = random.randrange(4, cols-4)
    color = COLORS[random.randrange(len(COLORS))]
    return Shape(shape, [SIZE*location+SIZE/2, SIZE/2], color)

def move():
    global current_shape
    if current_shape.freeze:
        current_shape = create_shape()
    if not current_shape.move_capable('down', grid):
        current_shape.freeze = True
        grid.refresh()
    else:
        current_shape.move('down', grid)

def play():
    global inplay, grid, current_shape, score
    timer.stop()
    inplay = True
    grid = Grid()
    score = 0
    current_shape = create_shape()    
    timer.start()

def keydown(key):
    if key == simplegui.KEY_MAP['space']:
        current_shape.rotate(grid)
    if key == simplegui.KEY_MAP['left']:
        current_shape.move('left', grid)
    if key == simplegui.KEY_MAP['right']:
        current_shape.move('right', grid)
    if key == simplegui.KEY_MAP['down']:
        current_shape.move('down', grid)        
    

# 创建用户界面
frame = simplegui.create_frame("俄罗斯方块", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)

# 创建按钮
frame.add_button("开始游戏", play, 80)
# 创建定时器
timer = simplegui.create_timer(TIME_INTERVAL, move)

play()
frame.start()
