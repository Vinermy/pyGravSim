from PIL import Image, ImageDraw
from vector2d import Vector2D
from celestialBody import CelestialBody
from typing import Iterable
from model import calculate_step
from logger import LogEntry
import json


def drawframe(
        bodies: Iterable[CelestialBody],
        indexes: Iterable[str],
        drawvectors: bool,
        drawtrails: bool,
        frame_number: int,
        log: LogEntry,
        calculate: bool = True,
):
    frame = Image.new('RGB', (610, 610), 'black')
    pencil = ImageDraw.Draw(frame)
    if drawtrails:
        for body in bodies:
            prevpos = body.position - body.speed * 5

            pencil.line(
                xy=(
                    (prevpos.x, prevpos.y),
                    (body.position.x, body.position.y)
                ),
                fill='gray'
            )

    if calculate:
        calculate_step(bodies)

    for i in range(len(bodies)):
        body = bodies[i]
        top_left_x = body.position.x - body.radius
        top_left_y = body.position.y - body.radius
        bottom_right_x = body.position.x + body.radius
        bottom_right_y = body.position.y + body.radius
        print(f'''Body {i + 1}
             Pos: [{body.position.x}, {body.position.y}],
             Vel: [{body.speed.x}, {body.speed.y}]''')
        pencil.ellipse(
            xy=[
                (top_left_x, top_left_y),
                (bottom_right_x, bottom_right_y)
            ],
            fill='green'
        )
        pencil.text(
            xy=(body.position.x, body.position.y),
            text=indexes[i],
            stroke_fill='black'
        )

        pencil.text(
            xy=(0, 0),
            text=str(frame_number),
            stroke_fill='white'
        )

        if drawvectors:
            next_pos = body.position + body.speed * 5

            pencil.line(
                xy=(
                    (next_pos.x, next_pos.y),
                    (body.position.x, body.position.y)
                ),
                fill='red'
            )
    frame.save('frame.jpg')
    log.addframe(
        positions=[x.position.getxy() for x in bodies],
        velocities=[x.speed.getxy() for x in bodies]
    )
