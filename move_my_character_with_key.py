

from pico2d import *


TUK_WIDTH, TUK_HEIGHT = 1080, 768
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
sonic = load_image('sonic.png')
# 850 x 1504
# 대충 35 x 45

gRunning = True
gFrame = 0
gSpeed = 12
x_dir = 0
y_dir = 0
x = TUK_WIDTH // 2
y = TUK_HEIGHT // 2

def handle_events():
    global gRunning, x_dir, y_dir

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            gRunning = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                gRunning = False
                return

            if event.key == SDLK_RIGHT:
                x_dir += 1 # 한번만 들어옴
            elif event.key == SDLK_LEFT:
                x_dir -= 1

            if event.key == SDLK_UP:
                y_dir += 1
            elif event.key == SDLK_DOWN:
                y_dir -= 1

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                x_dir -= 1
            elif event.key == SDLK_LEFT:
                x_dir += 1

            if event.key == SDLK_UP:
                y_dir -= 1
            elif event.key == SDLK_DOWN:
                y_dir += 1




def not_move_sonic():
    sonic.clip_draw(220, 1439, 35, 45, x, y, 90, 100)

def right_move_sonic():
    global x
    if x + gSpeed > TUK_WIDTH-1-35:
        x -= gSpeed
    sonic.clip_draw(300 + gFrame * 38, 1438, 35, 45, x, y, 90, 100)

def left_move_sonic():
    global x
    if x - gSpeed < 0 + 35:
        x += gSpeed
    sonic.clip_composite_draw(300 + gFrame * 38, 1438, 35, 45, 0, 'h', x, y, 90, 100)

def up_move_sonic():
    global y
    if y + gSpeed > TUK_HEIGHT-1:
        y -= gSpeed
    if x_dir >= 0 and y_dir > 0:
        sonic.clip_draw(300 + gFrame * 38, 1438, 35, 45, x, y, 90, 100)
    elif x_dir < 0:
        sonic.clip_composite_draw(300 + gFrame * 38, 1438, 35, 45, 0, 'h', x, y, 90, 100)
def down_move_sonic():
    global y
    if y - gSpeed < 0+45:
        y += gSpeed
    if x_dir >= 0 and y_dir < 0:
        sonic.clip_draw(300 + gFrame * 38, 1438, 35, 45, x, y, 90, 100)
    elif x_dir < 0:
        sonic.clip_composite_draw(300 + gFrame * 38, 1438, 35, 45, 0, 'h', x, y, 90, 100)

def RenderingSonic():
    if x_dir == 0 and y_dir == 0:
        not_move_sonic()
    if x_dir == 1:
        right_move_sonic()
    if x_dir == -1:
        left_move_sonic()
    if y_dir == 1:
        up_move_sonic()
    if y_dir == -1:
        down_move_sonic()

while gRunning:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)

    handle_events()

    RenderingSonic()
    update_canvas()
    gFrame = (gFrame + 1) % 9
    x += x_dir * gSpeed
    y += y_dir * gSpeed
    delay(0.05)

close_canvas()