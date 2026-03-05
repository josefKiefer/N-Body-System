from models import VectorizedBody
from physics_equations import get_accelerations
import math

def euler(step_size: float, total_time: float, body1: VectorizedBody, body2: VectorizedBody):
  body1_positions = []
  body2_positions = []

  num_steps =  int(math.ceil(total_time / step_size))

  for _ in range(num_steps):
    body1.acc, body2.acc = get_accelerations(body1, body2)

    body1_positions.append(body1.pos.copy())
    body2_positions.append(body2.pos.copy())

    body1.vel += step_size * body1.acc
    body2.vel += step_size * body2.acc

    body1.pos += step_size * body1.vel
    body2.pos += step_size * body2.vel

  return body1_positions, body2_positions

