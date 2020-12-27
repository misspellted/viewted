

from camera.lens import CameraLens


class PXLens(CameraLens):
  def __init__(self):
    CameraLens.__init__(self)

  def absorb(self, light, position):
    """
    Absorb an incoming ray of light at the position on the lens.

    The position is assumed to be referenced to the optical axis (center of the lens).
    """
    pass

