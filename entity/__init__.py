

class Entity:
  """
  An entity that can update its state when prompted.
  """

  def update(self):
    """
    Prompts the entity to update itself.

    The default reaction is to do nothing.
    """

    pass


class EntityManager:
  """
  Manages the entities involved with the application.
  """

  def __init__(self):
    self.entities = list()

  def add(self, entity):
    """
    Adds an entity to be prompted on updates from the application.
    """
    if isinstance(entity, Entity):
      self.entities.append(entity)

  def update(self):
    """
    Prompts all the entities to issue updates.
    """

    # TODO: Possibly set this up as a `with`-capable context.. thing?
    for entity in self.entities:
      entity.update()

