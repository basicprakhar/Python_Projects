# Author: Prakhar Agrawal

from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

pa_player = FirstPersonController()

pa_ground = Entity(
    model='plane',
    texture='grass',
    collider='mesh',
    scale=(100, 1, 100)
)

for pa_i in range(10):
    for pa_j in range(10):
        pa_robot = FrameAnimation3d(
            'assets\\robot',
            position=(2 * pa_i, 0, 2 * pa_j),
            fps=18,
            scale=0.015,
            color=color.black66
        )

Sky()

app.run()

# End of code
