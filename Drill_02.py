from pico2d import *
import math
open_canvas()
grass = load_image('grass.png')
character = load_image('character.png')
x, y = 100, 90
speed = 5
angle = 0
radius = 200
center_x, center_y = 400, 300
current_state = 'square'
square_direction = 'right'
while True:
    clear_canvas_now()
    grass.draw_now(400, 30)
    if current_state == 'square':
        if square_direction == 'right':
            x += speed
            if x >= 700:
                square_direction = 'up'
        elif square_direction == 'up':
            y += speed
            if y >= 500:
                square_direction = 'left'
        elif square_direction == 'left':
            x -= speed
            if x <= 100:
                square_direction = 'down'
        elif square_direction == 'down':
            y -= speed
            if y <= 90:
                square_direction = 'right'
                current_state = 'circle'
    elif current_state == 'circle':
        angle += 2
        x = center_x + radius * math.cos(math.radians(angle))
        y = center_y + radius * math.sin(math.radians(angle))
        if angle >= 360:
            angle = 0
            current_state = 'square'
    character.draw_now(x, y)
    delay(0.01)
close_canvas()
#구글 제미나이의 도움을 받아 작성하고 코파일럿을 통해 공부했습니다.