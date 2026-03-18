from dataclasses import dataclass, field
import numpy as np

@dataclass
class Body:
  name: str
  x: float
  y: float
  vx: float
  vy: float
  mass: float

  def position_vector(self):
    return np.array([self.x, self.y])
  
  def velocity_vector(self):
    return np.array([self.vx, self.vy])
  
  def to_dict(self) -> dict:
    return {
      "name": self.name,
      "x": self.x,
      "y": self.y,
      "vx": self.vx,
      "vy": self.vy,
      "mass": self.mass
    }
  
  @staticmethod
  def from_dict(data: dict):
    return Body(
      name=data["name"],
      x=data["x"],
      y=data["y"],
      vx=data["vx"],
      vy=data["vy"],
      mass=data["mass"]
    )
  
@dataclass
class VectorizedBody:
  """This will allow for better performance because we can update pos/vel/acc directly instead of having to
  unpack and repack data which leads to creating and destorying python objects. This will allow numpy's internal
  C libraries to do all of the math."""
  name: str
  mass: float

  pos: np.ndarray = field(default_factory=lambda: np.zeros(2))
  vel: np.ndarray = field(default_factory=lambda: np.zeros(2))
  acc: np.ndarray = field(default_factory=lambda: np.zeros(2))

  @property
  def x(self): return self.pos[0]

  @property
  def y(self): return self.pos[1]
  
  @property
  def vx(self): return self.vel[0]

  @property
  def vy(self): return self.vel[1]

  
  def to_dict(self) -> dict:
    return {
      "name": self.name,
      "x": float(self.pos[0]),
      "y": float(self.pos[1]),
      "vx": float(self.vel[0]),
      "vy": float(self.vel[1]),
      "mass": self.mass
    }
  
  @staticmethod
  def from_dict(data: dict):
    return VectorizedBody(
      name=data["name"],
      mass=data["mass"],
      pos=np.array([data["x"], data["y"]], dtype=float),
      vel=np.array([data["vx"], data["vy"]])
    )
  
@dataclass
class BodyStepState:
  body1_pos: np.ndarray
  body2_pos: np.ndarray

  body1_ke: float
  body2_ke: float

  pot_energy: float