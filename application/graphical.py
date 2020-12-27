

from application import Application
from camera.viewer import CameraViewer
import pygame


class PyGameViewer(CameraViewer):
  def __init__(self, length, height, bits=24):
    CameraViewer.__init__(self)
    self.output = pygame.display.set_mode((length, height), depth=bits)

  def show(self, snapshot):
    """
    Displays a snapshot captured from the sensor of the camera.
    """

    # FIXME: For now, we assume the snapshot taken from the sensor is the same
    #        size as the output area accessible to the viewer.
    self.output.blit(snapshot, (0, 0))

    # And it won't be shown until the output area is refreshed.
    pygame.display.flip()


class PyGameApp(Application):
  """
  A basic pygame application, managing the output area.
  """

  def __init__(self):
    Application.__init__(self)

  def caption(self, text):
    """
    Updates the caption of the window.
    """

    # TODO: Ignore changing the caption if in full-screen mode?
    pygame.display.set_caption(text)

  def handle(self, event):
    """
    Handles an event pulled from the event queue.
    """

    pass

  def process(self):
    """
    Processes the pygame event queue.

    The QUIT event is handled internally by calling the ::stop method, setting
    up the termination sequence.

    Any other event (for now) is forwarded to ::handle(event) for further
    processing.
    """

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self.stop()
        break
      else:
        self.handle(event)

  def terminate(self):
    """
    Thanks pygame for it's services.
    """

    pygame.quit()

