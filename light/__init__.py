

class Light:
  def __init__(self, red, green, blue):
    self.red = red
    self.green = green
    self.blue = blue

  def tupled(self):
    return (self.red, self.green, self.blue)


class LightTarget:
  """
  A target in the environment that receives light.
  """

  def absorb(self, source):
    """
    Absorbs the light from a source.
    """

    pass


class LightSource:
  """
  A source of light in an environment, such as a scene.
  """

  def project(self, target):
    """
    Projects the light onto a target.
    """

    pass

