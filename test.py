from ursina import *
# create a window
app = Ursina()
player = Entity(model='cube', color=color.orange, scale_y=4)

def update():
    player.x += held_keys['d'] * time.dt
    player.x -= held_keys['a'] * time.dt

def input(key):
    if key == 'space':
        player.y += 1
        invoke(setattr, player, 'y', player.y-1, delay=.25)

app.run()