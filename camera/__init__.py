

from camera.mount import CameraMount
from camera.sensor import CameraSensor
from camera.viewer import CameraViewer
from entity import Entity
import math
import pygame


class Camera(Entity):
  """
  A collection of components designed to capture an image as a result of making
  observations of an enviornment in which it participates.
  """
  
  def __init__(self, sensor):
    if not isinstance(sensor, CameraSensor):
      raise TypeError("A CameraSensor instance is required.")

    Entity.__init__(self)

    # What viewer is on the camera body?
    self.viewer = None
    # What sensor is in the camera body?
    self.sensor = sensor
    # What lens mount is on the camera body?
    self.mount = None

    # TODO: [Temporary] The default dimensions of the camera.
    #       Would rather use the CameraViewer instance to get
    #       the dimensions of the camera.
    self.dimensions = self.sensor.dimensions

  def compatible(self, component):
    # Not really digging into the meat and potatoes of compatibility, but the
    # ::use method will handle the default component compatibility.
    return True

  def use(self, component):
    if self.compatible(component):
      if isinstance(component, CameraViewer):
        # print(f"CameraViewer instance: {component}")
        self.viewer = component
      elif isinstance(component, CameraSensor):
        # print(f"CameraSensor instance: {component}")
        self.sensor = component
      elif isinstance(component, CameraMount):
        self.mount = component

  def attach(self, lens):
    if self.mount is None:
      raise ValueError("A mount is required to attach a lens to the camera.")
    else:
      # For now, forward the lens to the mount, and let it do perform the
      # instance-of check.
      self.mount.attach(lens)

  def capture(self):
    snapshot = self.sensor.capture()
    self.sensor.clear()
    return snapshot

  def update(self):
    """
    Displays a snapshot captured from the sensor on the viewer.
    """
    snapshot = self.capture()

    if snapshot is not None and self.viewer is not None:
      self.viewer.show(snapshot)

