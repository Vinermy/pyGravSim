from threading import Condition, Thread
from time import sleep
from typing import Iterable
from drawer import drawframe
from celestialBody import CelestialBody

simGoing = None
drawReady = Condition()


def simStart(
    delay: int,
    bodies: Iterable[CelestialBody],
    indexes: Iterable[str],
    drawVectors: bool,
    drawTrails: bool,
    calculate: bool = True
):

    global simGoing

    delayThread = Thread(
        target=delayCycle(),
        args=(delay, )
    )

    drawThread = Thread(
        target=drawCycle(),
        args=(
            bodies,
            indexes,
            drawVectors,
            drawTrails,
            calculate,
        )
    )

    simGoing = True

    delayThread.start()
    drawThread.start()


def delayCycle(delay):
    global simGoing
    while simGoing:
        drawReady.notify_all()
        sleep(delay)


def drawCycle(
    bodies: Iterable[CelestialBody],
    indexes: Iterable[str],
    drawVectors: bool,
    drawTrails: bool,
    calculate: bool = True
):
    global simGoing
    while simGoing:
        drawReady.wait()
        drawframe(bodies=bodies, indexes=indexes, drawvectors=drawVectors, drawtrails=drawTrails, frame_number=,
                  calculate=calculate)
