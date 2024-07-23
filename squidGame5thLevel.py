# Author: Prakhar Agrawal

from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
window.fullscreen = True
window.color = color.black

pa_player = FirstPersonController(
    collider='box', jump_duration=0.35
)
pa_player.cursor.visible = False

pa_ground = Entity(
    model='plane',
    texture='grass',
    collider='mesh',
    scale=(30, 0, 3)
)

pa_pill1 = Entity(
    model='cube',
    color=color.violet,
    scale=(0.4, 0.1, 53),
    z=28, x=-0.7
)
pa_pill2 = duplicate(pa_pill1, x=-3.7)
pa_pill3 = duplicate(pa_pill1, x=0.6)
pa_pill4 = duplicate(pa_pill1, x=3.6)

from random import randint

pa_blocks = []
for pa_i in range(12):
    pa_block = Entity(
        model='cube', collider='box',
        color=color.white33,
        position=(2, 0.1, 3 + pa_i * 4),
        scale=(3, 0.1, 2.5)
    )
    pa_block2 = duplicate(pa_block, x=-2.2)
    pa_blocks.append(
        (pa_block, pa_block2, randint(0, 10) > 7, randint(0, 10) > 7)
    )

pa_goal = Entity(
    color=color.brown,
    model='cube',
    z=55,
    scale=(10, 1, 10),
)

pa_pillar = Entity(
    color=color.brown,
    model='cube',
    z=58,
    scale=(1, 15, 1), y=8
)

def update():
    for pa_block1, pa_block2, pa_k, pa_n in pa_blocks:
        for pa_x, pa_y in [(pa_block1, pa_k), (pa_block2, pa_n)]:
            if pa_x.intersects() and pa_y:
                invoke(destroy, pa_x, delay=0.1)
                pa_x.fade_out(duration=0.1)

def input(pa_key):
    if pa_key == 'q':
        quit()

app.run()

# End of code
