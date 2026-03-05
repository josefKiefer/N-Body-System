import numpy as np
from models import VectorizedBody, Body

G = 6.67430e-11

def get_force_non_vectorized(body1: Body, body2: Body) -> float:
    separation_vector = body1.position_vector() - body2.position_vector()
    magnitude = np.linalg.norm(separation_vector)

    if magnitude == 0:
        raise ValueError("The 2 masses occupy the same position.")

    return -G*separation_vector*((body1.mass * body2.mass)/magnitude**3)

def get_accelerations_non_vectorized(body1: Body, body2: Body):
    force_on_1 = get_force_non_vectorized(body1, body2)
    force_on_2 = -force_on_1
    return force_on_1 / body1.mass, force_on_2 / body2.mass


def get_force(body1: VectorizedBody, body2: VectorizedBody) -> float:
    separation_vector = body1.pos - body2.pos
    magnitude = np.linalg.norm(separation_vector)

    if magnitude == 0:
        raise ValueError("The 2 masses occupy the same position.")

    return -G*separation_vector*((body1.mass * body2.mass)/magnitude**3)

def get_accelerations(body1: VectorizedBody, body2: VectorizedBody):
    force_on_1 = get_force(body1, body2)
    force_on_2 = -force_on_1
    return force_on_1 / body1.mass, force_on_2 / body2.mass