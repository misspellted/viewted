

from camera.mount import CameraMount
from camera.px.lens import PXLens


class PXMount(CameraMount):
  def __init__(self, sensor):
    CameraMount.__init__(self, sensor)

  def compatible(self, lens):
    return isinstance(lens, PXLens)

  def adapt(self, position):
    # The incoming position is centered on the optic axis, so we need to shift
    # the reference to the top-left of the sensor. Simply put, we need to add
    # half the dimensions of the sensor to the incoming position.
    x, y = position
    scaled = self.sensor.dimensions.scale(0.5)

    return (x + scaled.length, y + scaled.height)

