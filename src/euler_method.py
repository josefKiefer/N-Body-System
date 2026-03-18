from models import VectorizedBody, BodyStepState
from physics_equations import get_accelerations
import math
from helpers import append_result

def euler(step_size: float, total_time: float, body1: VectorizedBody, body2: VectorizedBody):
  results: list[BodyStepState] = []

  num_steps =  int(math.ceil(total_time / step_size))
  
  append_result(results, body1, body2)

  for _ in range(num_steps):
    body1.acc, body2.acc = get_accelerations(body1, body2)

    body1.vel += step_size * body1.acc
    body2.vel += step_size * body2.acc

    body1.pos += step_size * body1.vel
    body2.pos += step_size * body2.vel

    append_result(results, body1, body2)

  return results

