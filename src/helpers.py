from models import BodyStepState, VectorizedBody
from physics_equations import get_kinetic_energy, get_potential_energy

def append_result(results: list[BodyStepState], body1: VectorizedBody, body2: VectorizedBody):
  results.append(BodyStepState(
    body1.pos.copy(),
    body2.pos.copy(),
    get_kinetic_energy(body1),
    get_kinetic_energy(body2),
    get_potential_energy(body1, body2)
  ))