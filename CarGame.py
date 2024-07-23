# Author: Prakhar Agrawal

from ursina import *
import random

app = Ursina()
camera.orthographic = True
camera.fov = 10

pa_car = Entity(model='quad', texture='assets\car', collider='box', scale=(2, 1), rotation_z=-90, y=-3)
pa_road1 = Entity(model='quad', texture='assets\\road', scale=15, z=1)
pa_road2 = duplicate(pa_road1, y=15)
pa_pair = [pa_road1, pa_road2]

pa_enemies = []
def pa_newEnemy():
    pa_val = random.uniform(-2, 2)
    pa_new = duplicate(pa_car, texture='assets\enemy', x=2 * pa_val, y=25, color=color.random_color(),
                       rotation_z=90 if pa_val < 0 else -90)
    pa_enemies.append(pa_new)
    invoke(pa_newEnemy, delay=0.5)
pa_newEnemy()

def update():
    pa_car.x -= held_keys['a'] * 5 * time.dt
    pa_car.x += held_keys['d'] * 5 * time.dt
    for pa_road in pa_pair:
        pa_road.y -= 6 * time.dt
        if pa_road.y < -15:
            pa_road.y += 30
    for pa_enemy in pa_enemies:
        if pa_enemy.x < 0:
            pa_enemy.y -= 10 * time.dt
        else:
            pa_enemy.y -= 5 * time.dt
        if pa_enemy.y < -10:
            pa_enemies.remove(pa_enemy)
            destroy(pa_enemy)
    if pa_car.intersects().hit:
        pa_car.shake()

app.run()

# End of code
