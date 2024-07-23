# Author: Prakhar Agrawal

from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
Sky()
pa_player = FirstPersonController()

from ursina.shaders import basic_lighting_shader
pa_boxes = []
for pa_n in range(12):
    for pa_k in range(12):
        pa_box = Button(
            color=color.white,
            model='sphere',
            position=(pa_k, 0, pa_n),
            texture='grass',
            shader=basic_lighting_shader,
            parent=scene,
            origin_y=0.5
        )
        pa_boxes.append(pa_box)

def input(pa_key):
    for pa_box in pa_boxes:
        if pa_box.hovered:
            if pa_key == 'left mouse down':
                pa_new = Button(
                    color=color.white,
                    model='sphere',
                    position=pa_box.position + mouse.normal,
                    texture='grass',
                    shader=basic_lighting_shader,
                    parent=scene,
                    origin_y=0.5
                )
                pa_boxes.append(pa_new)
            if pa_key == 'right mouse down':
                pa_boxes.remove(pa_box)
                destroy(pa_box)

pa_sword = Entity(model='assets\\blade', texture='assets\sword', rotation=(30, -40),
                  position=(0.35, -0.6), parent=camera.ui, scale=(0.2, 0.15))

def update():
    if held_keys['left mouse']:
        pa_sword.position = (0.45, -0.5)
    elif held_keys['right mouse']:
        pa_sword.position = (0.45, -0.5)
    else:
        pa_sword.position = (0.5, -0.6)

app.run()

# End of code
