from models import VectorizedBody
from physics_equations import get_accelerations
import math

def verlet(step_size: float, total_time: float, body1: VectorizedBody, body2: VectorizedBody):
  body1_positions = []
  body2_positions = []

  num_steps =  int(math.ceil(total_time / step_size))

  body1_acceleration, body2_acceleration = get_accelerations(body1, body2)

  for _ in range(num_steps):
    body1_positions.append(body1.pos.copy())
    body2_positions.append(body2.pos.copy())

    # Calulate new position
    body1.pos[0], body1.pos[1] = body1.vel + body1.vel * step_size + 0.5 * body1_acceleration * step_size **2
    body2.pos[0], body2.pos[1] = body2.pos + body2.vel * step_size + 0.5 * body2_acceleration * step_size **2
    
    # Calculate velocity at half step
    body1_vhalf = body1.vel + 0.5 * body1_acceleration * step_size
    body2_vhalf = body2.vel + 0.5 * body2_acceleration * step_size

    # Update acceleration using new position
    body1_acceleration, body2_acceleration = get_accelerations(body1, body2)

    # Finish velocity
    body1.vel[0], body1.vel[1] = body1_vhalf + 0.5 * body1_acceleration * step_size
    body2.vel[0], body2.vel[1] = body2_vhalf + 0.5 * body2_acceleration * step_size


  return body1_positions, body2_positions

