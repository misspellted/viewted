

from light import Light, LightSource
from scene import Scene


class PXScene(Scene, LightSource):
  def __init__(self, length, height):
    """
    Creates a scene having the specified dimensions of pixels.

    The center of the scene is considered the origin, as opposed to what a
      camera sensor considers the origin, which is the top-left corner. The
      adjustment is made at the camera lens mount, so the scene can remain
      focused on the scene.
    """
    Scene.__init__(self)
    LightSource.__init__(self)

  def project(self, target):
    """
    Projects the scene into the camera lens via the optic elements.

    The projection starts "in" the outermost optic element in the lens.
    """

    # Would it be accurate to say that the target should be the last optic
    #   element in the lens? Or maybe, the PXScene *is* an optic element..?
    #   TODO: Thoughts to ponder more... later.

    # For now, just project a light ray coincident with the optic axis.
    target.absorb(self)

    pass

