# Author: Prakhar Agrawal

from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
Sky()
pa_player = FirstPersonController()
window.fullscreen = True

pa_arm = Entity(
    parent=camera.ui,
    model='cube',
    color=color.blue,
    position=(0.75, -0.6),
    rotation=(150, -10, 6),
    scale=(0.2, 0.2, 1.5)
)

def update():
    if held_keys['left mouse']:
        pa_arm.position = (0.6, -0.5)
    elif held_keys['right mouse']:
        pa_arm.position = (0.6, -0.5)
    else:
        pa_arm.position = (0.75, -0.6)

pa_boxes = []

for pa_n in range(15):
    for pa_k in range(15):
        pa_box = Button(
            position=(pa_k, 0, pa_n),
            color=color.orange,
            highlight_color=color.lime,
            model='cube',
            texture=load_texture('assets\wood'),
            origin_y=0.5,
            parent=scene
        )
        pa_boxes.append(pa_box)

def input(pa_key):
    for pa_box in pa_boxes:
        if pa_box.hovered:
            if pa_key == 'left mouse down':
                pa_newBox = Button(
                    position=pa_box.position + mouse.normal,
                    color=color.orange,
                    highlight_color=color.lime,
                    model='cube',
                    texture=load_texture('assets\wood'),
                    origin_y=0.5,
                    parent=scene
                )
                pa_boxes.append(pa_newBox)
            if pa_key == 'right mouse down':
                pa_boxes.remove(pa_box)
                destroy(pa_box)

app.run()

# End of code
