import matplotlib.pyplot as plt
from enum import StrEnum
from models import BodyStepState
from matplotlib.axes import Axes

class Integrator(StrEnum):
  EULER = "Euler"
  VERLET = "Verlet"
  RK4 = "RK4"

class Plotter_2_Body:
  ax_orbit: Axes
  ax_energy: Axes

  def __init__(self, body1_name: str, body2_name: str):
    self.fig, (self.ax_orbit, self.ax_energy) = plt.subplots(1, 2, figsize=(12, 5))
    self.ax_orbit.axis("equal")
    self.body1_name = body1_name
    self.body2_name = body2_name

  def plot_points(self, results: list[BodyStepState], integrator: Integrator):
    body1_history = [r.body1_pos for r in results]
    body2_history = [r.body2_pos for r in results]
    body1_ke = [r.body1_ke for r in results]
    body2_ke = [r.body2_ke for r in results]
    pe = [r.pot_energy for r in results]
    total_energy = [r.body1_ke + r.body2_ke + r.pot_energy for r in results]


    x1_history, y1_history = list(zip(*body1_history))
    x2_history, y2_history = list(zip(*body2_history))

    self.ax_orbit.plot(x1_history, y1_history, label=f"{self.body1_name} Orbit - ({integrator})")
    self.ax_orbit.plot(x2_history, y2_history, label=f"{self.body2_name} Orbit - ({integrator})")
    self.ax_orbit.scatter(x1_history[0], y1_history[0], marker="o")
    self.ax_orbit.scatter(x2_history[0], y2_history[0], marker="o")

    self.ax_energy.plot(body1_ke, label=f"{self.body1_name} KE - ({integrator})")
    self.ax_energy.plot(body2_ke, label=f"{self.body2_name} KE - ({integrator})")
    self.ax_energy.plot(pe, label=f"PE - ({integrator})")
    self.ax_energy.plot(total_energy, label=f"Total Energy - ({integrator})")


  def save_figure(self):
    file_path = f"./output_models/{self.body1_name}-{self.body2_name}.png"
    
    self.ax_orbit.legend()
    self.ax_energy.legend()
    self.fig.savefig(file_path)

    print(f"Figure saved to {file_path}")
