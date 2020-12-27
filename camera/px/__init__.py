

from camera import Camera
from camera.px.mount import PXMount


class PXCamera(Camera):
  def __init__(self, sensor):
    Camera.__init__(self, sensor)
    # And configure the camera to use the PX mount.
    self.use(PXMount(sensor))

  def compatible(self, component):
    # Enforce slightly stricter compatibility for the mount.
    compat = False

    if isinstance(component, PXMount):
      compat = True

    return compat

