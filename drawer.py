from PIL import Image, ImageDraw
from vector2d import Vector2D
from celestialBody import CelestialBody
from typing import Iterable
from model import calculate_step


def drawFrame(
    bodies: Iterable[CelestialBody],
    indexes: Iterable[str],
    drawVectors: bool,
    drawTrails: bool,
    calculate: bool = True
):
    frame = Image.new('RGB', (610, 610), 'black')
    pencil = ImageDraw.Draw(frame)
    if drawTrails:
        for body in bodies:
            prevPos = body.position + body.speed
            #prevPos.stretch(10)

            pencil.line(
                xy=(
                    (prevPos.x, prevPos.y),
                    (body.position.x, body.position.y)
                ),
                fill='gray'
            )

    if calculate:
        calculate_step(bodies)

    for i in range(len(bodies)):
        body = bodies[i]
        topLeftX = body.position.x - body.radius
        topLeftY = body.position.y - body.radius
        bottomRightX = body.position.x + body.radius
        bottomRightY = body.position.y + body.radius
        print(f'''Body {i+1}
             Pos: [{body.position.x}, {body.position.y}],
             Vel: [{body.speed.x}, {body.speed.y}]''')
        pencil.ellipse(
            xy=[
                (topLeftX, topLeftY),
                (bottomRightX, bottomRightY)
            ],
            fill='green'
        )
        pencil.text(
            xy=(body.position.x, body.position.y),
            text=indexes[i],
            stroke_fill='black'
        )

        if drawVectors:
            nextPos = (body.position + body.speed)
            #nextPos.stretch(10)
            

            pencil.line(
                xy=(
                    (nextPos.x, nextPos.y),
                    (body.position.x, body.position.y)
                ),
                fill='red'
            )
    frame.save('frame.jpg')
