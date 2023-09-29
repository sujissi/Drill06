import random
from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
arrow = load_image('hand_arrow.png')


def handle_events():
    global running
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    pass


def set_arrow_point():
    global rx, ry, is_collision
    margin = 100
    check_collision()
    if is_collision:
        rx = random.randint(0 + margin, TUK_WIDTH - margin)
        ry = random.randint(0 + margin, TUK_HEIGHT - margin)
        is_collision = False
    pass


def follow_arrow():
    global x, y, rx, ry
    t = 0.1
    x = (1 - t) * x + t * rx
    y = (1 - t) * y + t * ry
    pass


def check_collision():
    global x, y, rx, ry, is_collision
    if -20 < x - rx < 20 and -20 < y - ry < 20:
        is_collision = True
    pass


def set_img_dir():
    global x, rx, direction
    if x < rx:
        direction = 1
    else:
        direction = 0
    pass


running = True
is_collision = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
rx, ry = x, y

frame = 0
direction = 1
hide_cursor()

while running:
    clear_canvas()
    set_arrow_point()
    set_img_dir()
    follow_arrow()

    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    character.clip_draw(frame * 100, 100 * direction, 100, 100, x, y)
    arrow.draw(rx, ry)

    update_canvas()
    frame = (frame + 1) % 8
    delay(0.05)
    handle_events()

close_canvas()
