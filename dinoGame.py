# Author: Prakhar Agrawal

from ursina import *
import random as r

app = Ursina()
window.fullscreen = True
window.color = color.white

pa_dino = Animation('assets\dino',
                    collider='box',
                    x=-5)

pa_ground1 = Entity(
    model='quad',
    texture='assets\ground',
    scale=(50, 0.5, 1),
    z=1
)
pa_ground2 = duplicate(pa_ground1, x=50)
pa_pair = [pa_ground1, pa_ground2]

pa_cactus = Entity(
    model='quad',
    texture='assets\cacti',
    x=20,
    collider='box'
)
pa_cacti = []
def pa_newCactus():
    pa_new = duplicate(pa_cactus,
                       x=12 + r.randint(0, 5))
    pa_cacti.append(pa_new)
    invoke(pa_newCactus, delay=2)
pa_newCactus()

pa_label = Text(
    text=f'Points: {0}',
    color=color.black,
    position=(-0.5, 0.4)
)
pa_points = 0

def update():
    global pa_points
    pa_points += 1
    pa_label.text = f'Points: {pa_points}'
    for pa_ground in pa_pair:
        pa_ground.x -= 6 * time.dt
        if pa_ground.x < -35:
            pa_ground.x += 100
    for pa_c in pa_cacti:
        pa_c.x -= 6 * time.dt
    if pa_dino.intersects().hit:
        pa_dino.texture = 'assets\hit'
        application.pause()

pa_sound = Audio(
    'assets\\beep',
    autoplay=False
)

def input(key):
    if key == 'space':
        if pa_dino.y < 0.01:
            pa_sound.play()
            pa_dino.animate_y(
                2,
                duration=0.4,
                curve=curve.out_sine
            )
            pa_dino.animate_y(
                0,
                duration=0.4,
                delay=0.4,
                curve=curve.in_sine
            )

camera.orthographic = True
camera.fov = 10

app.run()

# End of code
