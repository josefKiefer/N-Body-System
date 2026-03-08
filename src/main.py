import json
from models import VectorizedBody
from euler_method import euler
from plotter import Plotter_2_Body, Integrator
from verlet_method import verlet
import copy

file_name = "./input_data/sun_earth.json"

one_day = 86400
one_year = 60 * 60 * 24 * 365

def main():
    bodies = []
    with open(file_name, "r") as f:
        bodies_as_json = json.load(f)
        bodies = [VectorizedBody.from_dict(body) for body in bodies_as_json]

    plotter = Plotter_2_Body(bodies[0].name, bodies[1].name)

    body1_positions, body2_positions = euler(one_day * 7, one_year * 5, copy.deepcopy(bodies[0]), copy.deepcopy(bodies[1]))
    plotter.plot_points(body1_positions, body2_positions, Integrator.EULER)

    body1_positions, body2_positions = verlet(one_day * 7, one_year * 5, copy.deepcopy(bodies[0]), copy.deepcopy(bodies[1]))
    plotter.plot_points(body1_positions, body2_positions, Integrator.VERLET)

    plotter.save_figure()

if __name__ == "__main__":
    main()