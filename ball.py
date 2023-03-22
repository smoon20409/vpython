from vpython import *


ball = sphere(pos=vector(-5,18,0), radius=1, color=color.green)
bottom = box(pos=vector(0,-9,0), size=vector(50,0.5,25))

v = vector(0.7, 0,0)
y = ball.pos
g = vector(0, -9.81, 0)

dt = 0.005
t = 0.0

while True:
    rate(300)

    if ball.pos.y < (bottom.pos.y + 1):
        v.y = -v.y

    v += g*dt
    y += v*dt + 0.5*g*dt**2

    ball.pos = y