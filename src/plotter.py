import matplotlib.pyplot as plt
from enum import StrEnum

class Integrator(StrEnum):
  EULER = "Euler"
  VERLET = "Verlet"

class Plotter_2_Body:
  def __init__(self, body1_name: str, body2_name: str):
    self.fig, self.ax = plt.subplots()
    self.ax.axis("equal")
    self.body1_name = body1_name
    self.body2_name = body2_name

  def plot_points(self, body1_history, body2_history, integrator: Integrator):
    x1_history, y1_history = list(zip(*body1_history))
    x2_history, y2_history = list(zip(*body2_history))

    self.ax.plot(x1_history, y1_history, label=f"{self.body1_name} ({integrator})")
    self.ax.plot(x2_history, y2_history, label=f"{self.body2_name} ({integrator})")
    self.ax.scatter(x1_history[0], y1_history[0], marker="o")
    self.ax.scatter(x2_history[0], y2_history[0], marker="o")


  def save_figure(self):
    file_path = f"./output_models/{self.body1_name}-{self.body2_name}.png"
    
    self.ax.legend()
    self.fig.savefig(file_path)

    print(f"Figure saved to {file_path}")
