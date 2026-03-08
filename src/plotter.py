import matplotlib.pyplot as plt

def plot_points(body1_history, body2_history, body1_name: str, body2_name: str):
  x1_history, y1_history = list(zip(*body1_history))
  x2_history, y2_history = list(zip(*body2_history))

  fig, ax = plt.subplots()
  ax.plot(x1_history, y1_history, label=body1_name)
  ax.plot(x2_history, y2_history, label=body2_name)
  ax.legend()
  ax.scatter(x1_history[0], y1_history[0], marker="o")
  ax.scatter(x2_history[0], y2_history[0], marker="o")
  ax.axis("equal")

  fig.savefig(f"./output_models/{body1_name}-{body2_name}.png")