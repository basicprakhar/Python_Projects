# Author: Prakhar Agrawal

from ursina import *

app = Ursina()
pa_bg = Entity(model='quad', texture='assets\BG', scale=36, z=1)
window.fullscreen = True
pa_player = Animation('assets\player', collider='box', y=5)
pa_fly = Entity(model='cube', texture='assets\\fly1', collider='box',
                 scale=2, x=20, y=-10)

pa_flies = []
def pa_newFly():
  pa_new = duplicate(pa_fly, y=-5 + (5124 * time.dt) % 15)
  pa_flies.append(pa_new)
  invoke(pa_newFly, delay=1)


pa_newFly()
camera.orthographic = True
camera.fov = 20

def update():
  pa_player.y += held_keys['w'] * 6 * time.dt
  pa_player.y -= held_keys['s'] * 6 * time.dt
  pa_a = held_keys['w'] * -20
  pa_b = held_keys['s'] * 20
  if pa_a != 0:
    pa_player.rotation_z = pa_a
  else:
    pa_player.rotation_z = pa_b
  for pa_fly in pa_flies:
    pa_fly.x -= 4 * time.dt
    pa_touch = pa_fly.intersects()
    if pa_touch.hit:
      pa_flies.remove(pa_fly)
      destroy(pa_fly)
      destroy(pa_touch.entity)
  pa_t = pa_player.intersects()
  if pa_t.hit and pa_t.entity.scale == 2:
    quit()


def input(key):
  if key == 'space':
    pa_entity = Entity(y=pa_player.y, x=pa_player.x + 1, model='cube', scale=1,
                       texture='assets\Bullet', collider='cube')
    pa_entity.animate_x(30, duration=2, curve=curve.linear)
    invoke(destroy, pa_entity, delay=2)

app.run()

# End of code
