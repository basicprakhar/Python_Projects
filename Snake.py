# Author: Prakhar Agrawal

from ursina import *
app = Ursina()

pa_snake = Entity(model='cube', texture='assets\snake', scale=0.4, z=-1, collider='box')
pa_ground = Entity(model='cube', texture='grass', rotation=(90, 0, 0), scale=(5, 1, 5), z=1)
pa_apple = Entity(model='cube', texture='assets\\apple', scale=0.4, position=(1, -1, -1), collider='mesh')
pa_body = [Entity(model='cube', scale=0.2, texture='assets\\body') for _ in range(14)]

camera.orthographic = True
camera.fov = 8

from random import randint
pa_dx = pa_dy = 0

def update():
    pa_info = pa_snake.intersects()
    if pa_info.hit:
        pa_apple.x = randint(-4, 4) / 2
        pa_apple.y = randint(-4, 4) / 2
        pa_new_body = Entity(model='cube', z=-1, scale=0.2, texture='assets\\body')
        pa_body.append(pa_new_body)
    for i in range(len(pa_body) - 1, 0, -1):
        pa_pos = pa_body[i - 1].position
        pa_body[i].position = pa_pos
    pa_body[0].x = pa_snake.x
    pa_body[0].y = pa_snake.y
    pa_snake.x += time.dt * pa_dx
    pa_snake.y += time.dt * pa_dy

def input(pa_key):
    global pa_dx, pa_dy
    for pa_x, pa_y, pa_z in zip(['d', 'a'], [2, -2], [270, 90]):
        if pa_key == pa_x:
            pa_snake.rotation_z = pa_z
            pa_dx = pa_y
            pa_dy = 0
    for pa_x, pa_y, pa_z in zip(['w', 's'], [2, -2], [180, 0]):
        if pa_key == pa_x:
            pa_snake.rotation_z = pa_z
            pa_dy = pa_y
            pa_dx = 0

app.run()

# End of code
