

from entity import EntityManager


class Application(EntityManager):
  """
  An abstract application based on a simple loop.
  """

  def __init__(self):
    EntityManager.__init__(self)
    self.running = False

  def process(self):
    """
    Processes events, such as user input or platform notifications.
    """
    pass

  def terminate(self):
    """
    Provides the application a chance to clean up resources after the simple
    loop exits, prior to process termination.
    """
    pass

  def stop(self):
    """
    Sets the flag to stop the simple loop.
    """
    self.running = False

  def start(self):
    """
    Starts the simple loop.
    """
    self.running = True

    while self.running:
      self.process()

      if self.running:
        self.update()

    self.terminate()

