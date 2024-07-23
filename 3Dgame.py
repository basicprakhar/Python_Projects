# Author: Prakhar Agrawal

from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from random import uniform

app = Ursina()

pa_ground = Entity(model='plane',
                   texture='grass',
                   collider='mesh',
                   scale=(100, 1, 100))

pa_player = FirstPersonController(collider='box')
pa_player.cursor.visible = False

pa_myBox = Entity(model='cube',
                  color=color.black,
                  collider='box',
                  position=(15, 0.5, 5))
pa_myBall = Entity(model='sphere',
                   color=color.red,
                   collider='sphere',
                   position=(5, 0.5, 10))

pa_sky = Sky()
pa_lvl = 1

pa_blocks = []
pa_directions = []
window.fullscreen = True

for pa_i in range(10):
    pa_r = uniform(-2, 2)
    pa_block = Entity(position=(pa_r, 1 + pa_i, 3 + pa_i * 5),
                      model='cube',
                      texture='white_cube',
                      color=color.azure,
                      scale=(3, 0.5, 3),
                      collider='box')
    pa_blocks.append(pa_block)
    if pa_r < 0:
        pa_directions.append(1)
    else:
        pa_directions.append(-1)

pa_goal = Entity(color=color.gold,
                 model='cube',
                 texture='white_cube',
                 position=(0, 11, 55),
                 scale=(10, 1, 10),
                 collider='box')

pa_pillar = Entity(color=color.green,
                   model='cube',
                   position=(0, 36, 58),
                   scale=(1, 50, 1))

pa_jump = Audio('assets\jump.mp3', loop=False, autoplay=False)

pa_walk = Audio('assets\walk.mp3', loop=False, autoplay=False)


def update():
    global pa_lvl
    pa_i = 0
    for pa_block in pa_blocks:
        pa_block.x -= pa_directions[pa_i] * time.dt
        if abs(pa_block.x) > 5:
            pa_directions[pa_i] *= -1
        if pa_block.intersects().hit:
            pa_player.x -= pa_directions[pa_i] * time.dt
        pa_i = pa_i + 1
    if pa_player.z > 56 and pa_lvl == 1:
        pa_lvl = 2
        pa_sky.texture = 'sky_sunset'
    pa_walking = held_keys['a'] or \
                 held_keys['d'] or \
                 held_keys['w'] or \
                 held_keys['s']
    if pa_walking and pa_player.grounded:
        if not pa_walk.playing:
            pa_walk.play()
    else:
        if pa_walk.playing:
            pa_walk.stop()


def input(key):
    if key == 'q':
        quit()
    if key == 'space':
        if not pa_jump.playing:
            pa_jump.play()

app.run()

# End of code
