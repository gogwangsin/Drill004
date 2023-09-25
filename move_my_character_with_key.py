

from pico2d import *


TUK_WIDTH, TUK_HEIGHT = 1080, 768
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')

def handle_events():

    global gRunning

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            gRunning = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            gRunning = False


gRunning = True
gFrame = 0

while gRunning:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)

    update_canvas()
    handle_events()
    if not gRunning:
        break
    gFrame = ( gFrame + 1 ) % 8
    delay(0.05)

close_canvas()