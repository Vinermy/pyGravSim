from typing import Iterable
from celestialBody import CelestialBody
from vector2d import Vector2D
# from multiprocessing import Pool


def calculate_forces(body: CelestialBody, others: Iterable[CelestialBody]):
    body.affected_by = []
    for other_body in others:
        try:
            force = (other_body.mass / max(
                (other_body.position - body.position).length() ** 2,
                (other_body.radius + body.radius) ** 2
                ))
            vector = other_body.position - body.position
            vector.stretch(force)
            body.affected_by.append(vector)
        except ZeroDivisionError:
            continue


def apply_forces(body: CelestialBody):
    for force in body.affected_by:  # Summ all the accelerations that body is affected by
        body.speed += force
    body.position += body.speed  # Move the body accordinly


def calculate_step(body: CelestialBody, other_bodies: Iterable[CelestialBody]):  # Update the simulation
    calculate_forces(body=body, others=other_bodies)
    # with Pool(len(bodies)) as p:
    #     p.starmap(calculate_forces, [[x, bodies] for x in bodies])

    apply_forces(body)
    # with Pool(len(bodies)) as p:
    #     p.map(apply_forces, bodies)
