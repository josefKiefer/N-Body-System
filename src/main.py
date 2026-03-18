import json
from models import VectorizedBody
from euler_method import euler
from plotter import Plotter_2_Body, Integrator
from verlet_method import verlet
import copy
from rk4_method import runge_kutta_4

file_name = "./input_data/sun_earth.json"

one_day = 86400
one_year = 60 * 60 * 24 * 365

def main():
    bodies = []
    with open(file_name, "r") as f:
        bodies_as_json = json.load(f)
        bodies = [VectorizedBody.from_dict(body) for body in bodies_as_json]

    step_size = one_day
    total_time = one_year

    plotter = Plotter_2_Body(bodies[0].name, bodies[1].name)

    euler_results = euler(step_size, total_time, copy.deepcopy(bodies[0]), copy.deepcopy(bodies[1]))
    plotter.plot_points(euler_results, Integrator.EULER)

    verlet_results = verlet(step_size, total_time, copy.deepcopy(bodies[0]), copy.deepcopy(bodies[1]))
    plotter.plot_points(verlet_results, Integrator.VERLET)

    rk4_results = runge_kutta_4(step_size, total_time, copy.deepcopy(bodies[0]), copy.deepcopy(bodies[1]))
    plotter.plot_points(rk4_results, Integrator.RK4)

    plotter.save_figure()

if __name__ == "__main__":
    main()