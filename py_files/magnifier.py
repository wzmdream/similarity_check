__author__ = 'expressyang'
"""
简易放大镜
"""
import simpleguitk as simplegui


MAP_WIDTH = 2000
MAP_HEIGHT = 1818
#map_image = simplegui.load_image("http://ads.xjts.cn/zt/xj_map/images/1.jpg")
map_image = simplegui.load_image("1.jpg")
# 常量
MAP_SCALE = 3
CANVAS_WIDTH = MAP_WIDTH / MAP_SCALE
CANVAS_HEIGHT = MAP_HEIGHT / MAP_SCALE
MAGNIFIER_SIZE = 120

# Event handlers
def click(pos):
    magnifier_center[0] = pos[0]
    magnifier_center[1] = pos[1]

def drag(pos):
    magnifier_center[0] = pos[0]
    magnifier_center[1] = pos[1]

def draw(canvas):
    # 绘制图片
    canvas.draw_image(map_image, (MAP_WIDTH / 2, MAP_HEIGHT / 2), (MAP_WIDTH, MAP_HEIGHT),
                     (CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2), (CANVAS_WIDTH, CANVAS_HEIGHT))

    # 绘制放大镜
    source_center = (MAP_SCALE * magnifier_center[0], MAP_SCALE * magnifier_center[1])
    canvas.draw_image(map_image, source_center, [MAGNIFIER_SIZE, MAGNIFIER_SIZE],
                      magnifier_center, [MAGNIFIER_SIZE, MAGNIFIER_SIZE])

    # 绘制放大镜边框
    mag_left = magnifier_center[0] - MAGNIFIER_SIZE / 2
    mag_right = magnifier_center[0] + MAGNIFIER_SIZE / 2
    mag_top = magnifier_center[1] - MAGNIFIER_SIZE / 2
    mag_bottom = magnifier_center[1] + MAGNIFIER_SIZE / 2
    mag_topleft = (mag_left, mag_top)
    mag_topright = (mag_right, mag_top)
    mag_botleft = (mag_left, mag_bottom)
    mag_botright = (mag_right, mag_bottom)
    box = [mag_topleft, mag_botleft, mag_botright,
           mag_topright, mag_topleft]
    canvas.draw_polyline(box, 4, "Blue")


# event handler for timer
def tick():
    """
    向右下方移动
    """
    magnifier_center[0] += 1
    magnifier_center[1] += 1

# 创建框架
frame = simplegui.create_frame("放大镜", CANVAS_WIDTH, CANVAS_HEIGHT)
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(click)
frame.set_mousedrag_handler(drag)

# 计时器
timer = simplegui.create_timer(60.0,tick)

# 开始
magnifier_center = [CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2]
timer.start()
frame.start()
