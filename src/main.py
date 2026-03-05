import json
from models import VectorizedBody
from euler_method import euler
from plotter import plot_points
from verlet_method import verlet

file_name = "../input_data/sun_earth.json"

one_year = 60 * 60 * 24 * 365;

def main():
    bodies = []
    with open(file_name, "r") as f:
        bodies_as_json = json.load(f)
        bodies = [VectorizedBody.from_dict(body) for body in bodies_as_json]

    body1_positions, body2_positions = euler(60 * 60, one_year, bodies[0], bodies[1])

    plot_points(body1_positions, body2_positions, bodies[0].name, bodies[1].name)

if __name__ == "__main__":
    main()