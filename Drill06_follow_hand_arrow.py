import random
from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
arrow = load_image('hand_arrow.png')


# 클릭한 위치에 화살표 만들어지고 소년 도착시 사라짐
# 마우스 클릭 이벤트 추가
# 클릭 좌표 저장 리스트 추가해서 for문으로 그려야겠다

def handle_events():
    global running
    global x, y, mx, my
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            mx, my = event.x, TUK_HEIGHT - 1 - event.y
        elif event.type == SDL_MOUSEBUTTONDOWN:
            arrows.append(arrow)
            px.append(event.x)
            py.append(TUK_HEIGHT - 1 - event.y)
    pass


def follow_arrow():
    get_follow_point()
    if is_collision(x, y, px[0], py[0]):
        arrows.pop(0)
        px.pop(0), py.pop(0)
    pass


def is_collision(x1, y1, x2, y2):
    if -20 < x2 - x1 < 20 and -20 < y2 - y1 < 20:
        return True
    else:
        return False
    pass

def get_follow_point():
    global x, y
    t = 0.1
    x = (1 - t) * x + t * px[0]
    y = (1 - t) * y + t * py[0]
    pass

def set_img_dir():
    # global x, rx, direction
    # if x < rx:
    #     direction = 1
    # else:
    #     direction = 0
    pass


running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
mx, my = x, y
px, py = [], []
frame = 0
direction = 1
arrows = []

hide_cursor()

while running:
    clear_canvas()
    set_img_dir()

    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    character.clip_draw(frame * 100, 100 * direction, 100, 100, x, y)
    arrow.draw(mx, my)
    if not len(arrows) == 0:
        for i in range(0, len(arrows)):
            arrows[i].draw(px[i], py[i])
        follow_arrow()
    update_canvas()
    frame = (frame + 1) % 8
    delay(0.05)
    handle_events()

close_canvas()
