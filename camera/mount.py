

from camera.lens import CameraLens
from camera.sensor import CameraSensor


class CameraMount:
  """
  The camera lens mount provides an interface for compatible lenses to be
  attached to the camera.

  For example, we might consider having the following variants:
    P: A lens mount to observe planar (two-dimensional) environments.
    PX: A P-type lens mount to observe pixel-based environments.
    V: A lens mount to observe volumetric (three-dimensional) environments.
  
  TODO: It also functions as the last processing of the incoming light from the
  observed environment, with the areas outside of the sensor array, and
  converting to pixel coordinates of the sensor.
  """

  def __init__(self, sensor):
    if not isinstance(sensor, CameraSensor):
      raise TypeError("A CameraSensor instance is required.")

    # What sensor receives light rays passing through the mount?
    self.sensor = sensor
    # What lens is currently attached to the mount?
    self.lens = None

  def compatible(self, lens):
    return isinstance(lens, CameraLens)

  def attach(self, lens):
    if self.compatible(lens):
      self.lens = lens

  def adapt(self, position):
    """
    Adapts the incoming position of a light ray to the positioning system of
    the sensor.
    """
    pass

  def expose(self, light, position):
    """
    Exposes a single ray of light onto the sensor at the specified position.

    It is expected that the position of the ray to expose upon the sensor is
    centered on the optical axis: https://en.wikipedia.org/wiki/Optical_axis.
    """
    # The sensor performs the final check on the position before absorbing the
    # light ray, so we'll just forward the position after adaptation.
    self.sensor.absorb(self.adapt(position), light)

