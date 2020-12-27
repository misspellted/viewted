

import math


class Rectangle:
  def __init__(self, length, height):
    self.length = length
    self.height = height

  def tupled(self):
    return (self.length, self.height)

  def scale(self, factor):
    return Rectangle(self.length * float(factor), self.height * float(factor))

  def circumscribe(self):
    # We want to calculate the diameter of the minimal circle that contains the
    # rectangle.
    #
    # So.. something like..
    #
    # 
    #   /
    #  /|                           |
    # / |                           |
    # | |                           |
    # | |                           |
    # | |                           |
    # \ |                           |
    #  \|___________________________|/
    #   \
    # 
    # ----
    # Yeah... that... ain't.. gonna be pretty.
    #
    # Borrowing an ANSI/ASCII circle from https://ascii.co.uk/art/circle:
    #
    #                                 (0, +R)
    #
    #                             ooo OOO OOO ooo
    #                         oOO                 OOo
    #                     oOO                         OOo
    #                  oOO                               OOo
    #                oOO                                   OOo
    #              oOO+-------------------------------------+OOo
    #             oOO |                                     | OOo
    #            oOO  |                                     |  OOo
    #           oOO   |                                     |   OOo
    #           oOO   |                                     |   OOo
    #  (-R, 0)  oOO   |                                     |   OOo  (+R, 0)
    #           oOO   |                                     |   OOo
    #           oOO   |                                     |   OOo
    #            oOO  |                                     |  OOo
    #             oOO |                                     | OOo
    #              oOO+-------------------------------------+OOo
    #                oOO                                   OOo
    #                  oO0                               OOo
    #                     oOO                         OOo
    #                         oOO                 OOo
    #                             ooo OOO OOO ooo
    #
    #                                  (0, -R)
    #
    #
    # Turns out, this has a name: a circumscribed cirlce of a rectangle:
    #   https://www-formula.com/geometry/radius-circumcircle/radius-circumcircle-rectangle.
    #
    # Basically, the diagonals of the rectangle are the diameter of the circle. The diameter
    #   can be calculated as the hypotenuse of a triangle in the rectangle, since both sides
    #   are known (length, height):
    #
    #     diameter = squareRoot(square(length) + square(height))
    #
    # And then the radius is just half of that:
    #
    #     radius = half(diameter)
    #
    # Although, actually, we just need to know the diameter, so...
    return math.sqrt(self.length ** 2 + self.height ** 2)

  def padding(self, rectangle):
    """
    Calculates the padding offset between this and the other rectangle. Which
    rectangle is inside or outside is not considered. Just the dimensions are
    considered for calculations.
    """
    delta = None

    # First, calculate the difference in dimensions.
    if isinstance(rectangle, Rectangle):
      delta = Rectangle(abs(self.length - rectangle.length), abs(self.height - rectangle.height))
    elif isinstance(rectangle, tuple) and 2 <= len(rectangle):
      delta = Rectangle(abs(self.length - rectangle[0]), abs(self.height - rectangle[1]))
    else:
      raise TypeError(f"Provided rectangle data type ({type(rectangle)}) not recognized.")

    # Then halve the deltas to arrive at a centered padding.
    return delta.scale(0.5)

  def __repr__(self):
    return f"Rectangle({self.length}, {self.height})"


class Square(Rectangle):
  def __init__(self, side):
    Rectangle.__init__(self, side, side)

