# Author: Prakhar Agrawal

from ursina import *

app = Ursina()
window.color = color.olive

pa_table = Entity(
    model='cube',
    color=color.black,
    scale=(2, 1, 3),
    rotation=(90, 0, 0)
)

pa_ball = Entity(
    model='sphere',
    color=color.cyan,
    z=-1,
    scale=0.1,
    collider='box'
)

pa_player1 = Entity(
    model='cube',
    color=color.cyan,
    scale=(0.6, 0.1, 1),
    position=(0, -1.4, -1),
    collider='box'
)
pa_player2 = duplicate(pa_player1, y=1.4)

pa_speed_x = pa_speed_y = 0.5

def update():
    global pa_speed_x, pa_speed_y
    pa_player1.x += held_keys['d'] * time.dt
    pa_player1.x -= held_keys['a'] * time.dt
    pa_player2.x += held_keys['right arrow'] * time.dt
    pa_player2.x -= held_keys['left arrow'] * time.dt
    pa_ball.x += pa_speed_x * time.dt
    pa_ball.y += pa_speed_y * time.dt
    if abs(pa_ball.x) > 0.9:
        pa_speed_x = -pa_speed_x
    if abs(pa_ball.y) > 1.4:
        pa_ball.x = pa_ball.y = 0
    if pa_ball.intersects().hit:
        pa_speed_y = -pa_speed_y
        pa_speed_x *= 1.1
        pa_speed_y *= 1.1

camera.orthographic = True
camera.fov = 4

app.run()

# End of code
