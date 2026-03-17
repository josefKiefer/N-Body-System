from models import VectorizedBody
import math
from physics_equations import get_accelerations
import copy

def runge_kutta_4(step_size: float, total_time: float, body1: VectorizedBody, body2: VectorizedBody):
  body1_positions = []
  body2_positions = []

  num_steps =  int(math.ceil(total_time / step_size))


  for _ in range(num_steps):
      body1_positions.append(body1.pos.copy())
      body2_positions.append(body2.pos.copy())

      body1_acceleration, body2_acceleration = get_accelerations(body1, body2)

      b1_k2_body = copy.deepcopy(body1)
      b2_k2_body = copy.deepcopy(body2)

      b1_k2_body.pos = body1.pos + (step_size * body1.vel)/2
      b2_k2_body.pos = body2.pos + (step_size * body2.vel)/2

      b1_k2_body.vel = body1.vel + (step_size * body1_acceleration) / 2
      b2_k2_body.vel = body2.vel + (step_size * body2_acceleration) / 2

      b1_k2_body.acc, b2_k2_body.acc = get_accelerations(b1_k2_body, b2_k2_body)

      b1_k3_body = copy.deepcopy(body1)
      b2_k3_body = copy.deepcopy(body2)

      b1_k3_body.pos = body1.pos + (step_size * b1_k2_body.vel) / 2
      b2_k3_body.pos = body2.pos + (step_size * b2_k2_body.vel) / 2

      b1_k3_body.vel = body1.vel + (step_size * b1_k2_body.acc) / 2
      b2_k3_body.vel = body2.vel + (step_size * b2_k2_body.acc) / 2

      b1_k3_body.acc , b2_k3_body.acc = get_accelerations(b1_k3_body, b2_k3_body)

      b1_k4_body = copy.deepcopy(body1)
      b2_k4_body = copy.deepcopy(body2)

      b1_k4_body.pos = body1.pos + step_size * b1_k3_body.vel
      b2_k4_body.pos = body2.pos + step_size * b2_k3_body.vel

      b1_k4_body.vel = body1.vel + step_size * b1_k3_body.acc
      b2_k4_body.vel = body2.vel + step_size * b2_k3_body.acc

      b1_k4_body.acc, b2_k4_body.acc = get_accelerations(b1_k4_body, b2_k4_body)

      body1.pos = body1.pos + (1 / 6) * step_size * (body1.vel + 2 * b1_k2_body.vel + 2 * b1_k3_body.vel + b1_k4_body.vel)
      body2.pos = body2.pos + (1 / 6) * step_size * (body2.vel + 2 * b2_k2_body.vel + 2 * b2_k3_body.vel + b2_k4_body.vel)
      
      body1.vel = body1.vel + (1 / 6) * step_size * (body1_acceleration + 2 * b1_k2_body.acc + 2 * b1_k3_body.acc + b1_k4_body.acc)
      body2.vel = body2.vel + (1 / 6) * step_size * (body2_acceleration + 2 * b2_k2_body.acc + 2 * b2_k3_body.acc + b2_k4_body.acc)
      
  
  return body1_positions, body2_positions