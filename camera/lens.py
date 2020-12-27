

# from camera.mount import CameraMount


# This might get a bit complicated, if a lens is to have multiple optics:
# https://en.wikipedia.org/wiki/Photographic_lens_design

# And possibly some processing power... maybe need to have threading here?

# TODO: Add positional information. Thinking that the "positional index" of an
#       optic in the lens will start with the '0' being the optical piece at
#       the farthest away from the camera body - or in other words, the first
#       to process an incoming light ray, and as the 0'th processes the light,
#       any applicable forwarded light rays will hit the 1st, 2nd, et cetera,
#       until the last optic processes any rays that would pass through it.
#       Then we'd have to figure out how to foward it through the lens mount to
#       the sensor to be processed (absorbed).

class CameraLens:
  def __init__(self, mount):
    # Store a reference to the mount to send any incoming rays of light towards
    # the camera's sensor.
    # TODO: Figure out why this would introduce a circular reference that
    #       Python just simply can't resolve.
    # if not isinstance(mount, CameraMount):
    #   raise TypeError("A CameraMount instance is required.")

    self.mount = mount
    self.optics = list()

  def use(self, optic):
    if isinstance(optic, CameraOptic):
      self.optics.append(optic)

  def absorb(self, light, position):
    # For now, we're ignoring any optics, and going straight through towards
    # the sensor.
    # TODO: Factor in any optics in the lens.
    self.mount.expose(light, position)

