

from pico2d import *


TUK_WIDTH, TUK_HEIGHT = 1080, 768
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
sonic = load_image('sonic.png')
# 850 x 1504
# 대충 35 x 45


def handle_events():
    global gRunning, x_dir

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            gRunning = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            gRunning = False


gRunning = True
gFrame = 0
x_dir = 0
x = TUK_WIDTH // 2

def not_move_sonic():
    sonic.clip_draw(220, 1439, 35, 45, x, TUK_HEIGHT // 2, 90, 100)
    pass


while gRunning:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    not_move_sonic()
    update_canvas()
    handle_events()
    if not gRunning:
        break
    gFrame = (gFrame + 1) % 8
    delay(0.05)

close_canvas()