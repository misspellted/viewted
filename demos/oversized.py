

from application.graphical import PyGameApp, PyGameViewer
from camera import Camera
from camera.sensor import CameraSensor
from demos import Demo
from geometry.shapes import Square
import pygame


ASPECT_RATIO = 8/5


class OversizedCamera(Camera):
  def __init__(self, sensor):
    Camera.__init__(self, sensor)

    # The default dimensions are sensor-based, but may change in the future.
    # For this camera, we're focused on demonstrating how the sensor works, so
    # we need to override how much oversized the dimensions should be.
    # ----------------
    # The incoming light from the camera lens(es) will be based on scene
    #   coordinates, so a translation will need to be derived (it's prolly
    #   not going to be good in the long run, but something to get started).
    #   Currently, planning on using the inner radius of the lens mount
    #   (not the radius of the threading for lenses) as a unit circle, and
    #   therefore, a circle that surrounds the sensor will provide a way to
    #   convert from scene coordinates to sensor coordinates.
    #
    # This can be accomplished by circumscribing the rectangle made from the
    #   dimensions of the sensor. For example, given a sensor having dimensions
    #   of 1280 and 800 (an 8:5 ratio, the correct ratio for computer displays)
    #   and therefore, the radius of the circle of the circumscribed rectangle
    #   would be:
    #
    #     diameter = squareRoot(square(1280) + square(800))
    #              = squareRoot(1638400 + 640000)
    #              = squareRoot(2278400)
    #              ~ 1509.43698112906
    #
    #     radius = half(1509.43698112906)
    #            = 754.71849056453
    # ----------------
    self.dimensions = Square(int(round(self.sensor.dimensions.circumscribe(), 1)))

  def capture(self):
    # print(f"Snapshot dimensions: {self.dimensions}")
    snapshot = pygame.Surface(self.dimensions.tupled(), depth=32)

    # Capture the center of the snapshot.
    center = snapshot.get_rect().center

    # Indicate the blocked area on the snapshot area "imposed" by the lens mount.
    snapshot.fill((15, 15, 15))

    # Indicate the area outside of the sensor.
    pygame.draw.circle(snapshot, (31, 31, 31), center, center[0])

    # Draw in the sensor in the center.
    captured = self.sensor.capture()
    # print(f"Captured dimensions: {captured.get_size()}")
    padding = self.dimensions.padding(captured.get_size())

    self.sensor.clear()

    # print(f"Padding dimensions: {padding}")
    snapshot.blit(captured, (int(padding.length), int(padding.height)))

    return snapshot


class CameraSimulator(PyGameApp):
  def __init__(self, camera):
    if not isinstance(camera, Camera):
      raise TypeError("A Camera instance is required.") # For now...

    PyGameApp.__init__(self)

    # Connect a viewer to the camera.
    camera.use(PyGameViewer(camera.dimensions.length, camera.dimensions.height))

    # Track the camera as an entity.
    self.add(camera)

    # A somewhat descriptive caption would be nice.
    self.caption("Camera Simulator")


class OversizedCameraDemo(Demo):
  def __init__(self, sensor):
    if not isinstance(sensor, CameraSensor):
      raise ValueError("A CameraSensor instance is required.")

    self.sensor = sensor

  def start(self):
    # Camera Simulator 9000
    # --------------------------------
    # For this simulation, we're going to be building a camera, similar to how digital
    # cameras work (or as I think of them) - a sensor captures the light rays passing
    # through the lens(es).

    # For the first part, we want to see what the view would be as if the sensor was
    # viewed straight on ('ey... no optical funny business, ya 'eer?!). While the
    # sensor components are still being translated and implemented, we can at least
    # view the area removed by the lens (the areas outside the 'lens mount' of the
    # camera). We'll use a circle to simulate that restriction.

    # But first, we're going to need a camera!
    # SENSOR_LENGTH = 640
    # SENSOR_HEIGHT = 400
    # SENSOR_LENGTH = 200
    # SENSOR_HEIGHT = 320

    # Huh... wouldn't it be cool to use more photographic jargon, like a "four-thirds"
    # camera? I wonder... which dimension is it referenced from?
    # Oh, it looks to be based on manufacturer, but referenced from 'full-frame':
    # https://en.wikipedia.org/wiki/Image_sensor_format#Common_image_sensor_formats.

    # I guess another cool thought would be to have a scene (cough), in which the
    # camera sensor is 'changing' dimensions, to show how the circumscribing changes.
    # #FutureIdeas?

    CameraSimulator(OversizedCamera(self.sensor)).start()
    # CameraSimulator(Camera(CameraSensor(SENSOR_LENGTH, SENSOR_HEIGHT))).start()

    # New thoughts:
    #
    # * Getting objects projecting reflected light towards the camera.
    #   * How do we track whether an object would project the reflected light towards the camera?
    #   * Actually, why not just start with a light source first? Play around with some orbital movement to see change..
    #   * We will most likely need a way to represent the world.. and it's gotta get those update() notifications..
    #
    # * Processing light rays... might be expensive. Threads? That..'ll be .. fun..
    #   * Also, getting a little detailed here? but a light source would emit light... that could be how it contributes
    #       to the world, each update of the world, a light source emits it's "pattern", and in propogating that pattern,
    #       collisions would be formed/detectable, that would then inform the object collided with that it has light to
    #       reflect (if it doesn't absorb it completely) for part of it's update() invocation, and that would then have the
    #       ability to track how many bounces a ray would have? The number of rays in the emitted pattern would start small,
    #       maybe even be configurable/config-as-performance-level?.. but if the bounce count reaches zero on a collision,
    #       the object would not reflect that particular light (given reflectability due to material, et cetera), and would
    #       not contribute to the information sensed by the camera's sensor.
    #
    # * Simulating what lands on the sensor and what lands outside the sensor.
    #   * Probably use a simple square "light" source, and "move it around" in the camera lens, affecting the captured image.

    # For simulating the light landing on the sensor, we need a scene from which to capture the light source.


class LandscapeOversizedCameraDemo(OversizedCameraDemo):
  def __init__(self, sensorLength):
    # Calculate sensor height from ASPECT_RATIO.
    OversizedCameraDemo.__init__(self, CameraSensor(sensorLength, int(sensorLength * (1 / ASPECT_RATIO))))


class PortraitOversizedCameraDemo(OversizedCameraDemo):
  def __init__(self, sensorHeight):
    # Calculate sensor length from ASPECT_RATIO.
    OversizedCameraDemo.__init__(self, CameraSensor(int(sensorHeight * (1 / ASPECT_RATIO)), sensorHeight))

