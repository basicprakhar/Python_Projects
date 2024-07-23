# Author: Prakhar Agrawal

from ursina import *
app = Ursina()
window.fullscreen = True
Sky()

pa_bird = Animation(
    'assets\doodle\\bird',
    collider='box',
    color=color.orange,
    y=15
)
camera.add_script(
    SmoothFollow(
        target=pa_bird,
        offset=[0, 0, -50],
        speed=3
    )
)

pa_platform = Entity(
    model='cube',
    color=color.green,
    texture='white_cube',
    collider='box',
    scale=(3, 0.5)
)
pa_plates = []
for pa_i in range(5):
    pa_p = duplicate(
        pa_platform,
        y=pa_platform.y + 5
    )
    pa_plates.append(pa_p)

from random import randint

pa_down = True
def pa_makeTrue():
    global pa_down
    pa_down = True

pa_label = Text(
    text='',
    color=color.olive,
    position=(-0.2, 0.4),
    size=2 * Text.size
)
pa_points = pa_bird.y

def update():
    global pa_down, pa_points
    pa_points = max(pa_points, pa_bird.y)
    pa_label.text = str(round(
        100 * pa_points
    ))
    if pa_points - pa_bird.y > 15:
        quit()

    pa_bird.x -= held_keys['a'] * 12 * time.dt
    pa_bird.x += held_keys['d'] * 12 * time.dt
    pa_bird.y -= 7 * time.dt
    if pa_down and pa_bird.intersects().hit:
        pa_down = False
        invoke(pa_makeTrue, delay=0.5)
        pa_bird.animate_y(
            pa_bird.y + 7,
            duration=0.4,
            curve=curve.in_circ
        )
        pa_plates.append(
            duplicate(
                pa_platform,
                y=pa_plates[-1].y + 5,
                x=randint(-5, 5)
            )
        )
        pa_obj = pa_plates[0]
        pa_plates.pop(0)
        destroy(pa_obj)

app.run()

# End of code
