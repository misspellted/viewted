

from geometry.shapes import Rectangle
from light import Light
import pygame


class CameraSensor(pygame.Surface):
  """
  A collection of light detecting elements that generate an image of what is
  observed through a camera lens. Effectively, an off-screen buffer.

  Currently, expected to produce a pygame.Surface instance for captures.
  """

  def __init__(self, length, height, bits=24):
    """
    Creates a new instance.

    Parameters
    ----------------
      length: The distance between the left and right edges of the sensor, in pixels.
      height: The distance between the top and bottom edges of the sensor, in pixels.
      bits: The number of bits used to represent the color detected for a pixel; defaults to 24 bits.
    """

    pygame.Surface.__init__(self, (length, height), depth=bits)
    self.dimensions = Rectangle(length, height)
    self.bits = bits

  def absorb(self, position, light):
    """
    Absorbs a ray of light.

    Parameters
    ----------------
      position: The location on the sensor where the ray of light is to be absorbed.
      ray: The ray of light to be absorbed, as intensities of red, green, and blue.
    """

    x, y = position

    if 0 <= x < self.dimensions.length and 0 <= y < self.dimensions.height:
      ray = None
      if isinstance(light, Light):
        ray = light.tupled()
      elif isinstance(light, tuple) and 3 <= len(light) <= 4:
        ray = light

      if ray is not None:
        self.set_at((x, y), ray)
    # Exposing one pixel at a time is going to be ... time consuming.
    # TODO: Definitely want to queue exposures and thread the exposure.
    # Clearing, below, would also clear the queue.

  def clear(self):
    """
    Clears the sensor of previously exposed light rays.
    """

    self.fill((0, 0, 0))

  def capture(self):
    """
    Takes a snapshot of the light rays that have been exposed to the sensor.

    Results
    ----------------
    A pygame.Surface representation of the light rays that have been exposed to the sensor.
    """

    return self.copy()

