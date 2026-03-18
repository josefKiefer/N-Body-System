from models import VectorizedBody, BodyStepState
from physics_equations import get_accelerations
import math
from helpers import append_result

def verlet(step_size: float, total_time: float, body1: VectorizedBody, body2: VectorizedBody):
  results = []

  num_steps =  int(math.ceil(total_time / step_size))

  body1_acceleration, body2_acceleration = get_accelerations(body1, body2)

  append_result(results, body1, body2)

  for _ in range(num_steps):
    # Calulate new position
    body1.pos = body1.pos + body1.vel * step_size + 0.5 * body1_acceleration * step_size **2
    body2.pos = body2.pos + body2.vel * step_size + 0.5 * body2_acceleration * step_size **2
    
    # Calculate velocity at half step
    body1_vhalf = body1.vel + 0.5 * body1_acceleration * step_size
    body2_vhalf = body2.vel + 0.5 * body2_acceleration * step_size

    # Update acceleration using new position
    body1_acceleration, body2_acceleration = get_accelerations(body1, body2)

    # Finish velocity
    body1.vel = body1_vhalf + 0.5 * body1_acceleration * step_size
    body2.vel = body2_vhalf + 0.5 * body2_acceleration * step_size

    append_result(results, body1, body2)

  return results

