"""
This module lets you practice  ** using objects **, including:
  -- CONSTRUCTING objects,
  -- applying METHODS to them, and
  -- accessing their DATA via INSTANCE VARIABLES

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Hannah Levine.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to demonstrate and/or test them. """
    # Test your functions by putting calls to them here:
    two_circles()
    circle_and_rectangle()
    lines()


def two_circles():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws two rg.Circle objects on the window
         such that:
           -- They fit in the window and are easily visible.
           -- They have different radii.
           -- One is filled with some color and one is not filled.
    -- Waits for the user to press the mouse, then closes the window.
    """
    width = 700
    height = 400
    window = rg.RoseWindow(width, height)


    center_point = rg.Point(300, 100)
    radius = 53
    circle = rg.Circle(center_point, radius)
    circle.fill_color = 'orange'
    circle.attach_to(window)

    center_point = rg.Point(100, 50)
    radius = 23
    circle = rg.Circle(center_point, radius)
    circle.attach_to(window)


    window.render()

    window.close_on_mouse_click()

    # ------------------------------------------------------------------
    # DONE: 2. Implement this function, per its doc-string above.
    #    -- ANY two rg.Circle objects that meet the criteria are fine.
    #    -- File  COLORS.txt  lists all legal color-names.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    # ------------------------------------------------------------------


def circle_and_rectangle():
    width = 600
    height = 400
    window = rg.RoseWindow(width, height)

    center_point = rg.Point(200, 160)
    radius = 30
    circle = rg.Circle(center_point, radius)
    circle.fill_color = 'blue'
    circle.outline_thickness = 6
    circle.attach_to(window)
    print(circle.outline_thickness)
    print(circle.fill_color)
    print(center_point)
    print(center_point.x)
    print(center_point.y)

    point1 = rg.Point(50, 150)
    point2 = rg.Point(100, 50)
    rectangle = rg.Rectangle(point1, point2)
    rectangle.outline_thickness = 7

    print(rectangle.outline_thickness)
    print(rectangle.fill_color)
    print(rectangle.get_center())
    print(rectangle.get_center().x)
    print(rectangle.get_center().y)
    rectangle.attach_to(window)

    window.render()

    window.close_on_mouse_click()

    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws a rg.Circle and rg.Rectangle
       on the window such that:
          -- They fit in the window and are easily visible.
          -- The rg.Circle is filled with 'blue'
    -- Prints (on the console, on SEPARATE lines) the following data
         associated with your rg.Circle:
          -- Its outline thickness.
          -- Its fill color.
          -- Its center.
          -- Its center's x coordinate.
          -- Its center's y coordinate.
    -- Prints (on the console, on SEPARATE lines) the same data
         but for your rg.Rectangle.
    -- Waits for the user to press the mouse, then closes the window.

    Here is an example of the output on the console,
    for one particular circle and rectangle:
           1
           blue
           Point(180.0, 115.0)
           180
           115
           1
           None
           Point(75.0, 150.0)
           75.0
           150.0
    """
    # ------------------------------------------------------------------
    # DONE: 3. Implement this function, per its doc-string above.
    #   -- ANY objects that meet the criteria are fine.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    #
    # IMPORTANT: Use the DOT TRICK to guess the names of the relevant
    #       instance variables for outline thickness, etc.
    # ------------------------------------------------------------------


def lines():
    width = 500
    height = 500
    window = rg.RoseWindow(width, height)
    lone = rg.Line(rg.Point(200,84),rg.Point(300,48))
    ltwo = rg.Line(rg.Point(70, 100), rg.Point(90,450))
    ltwo.thickness = 17
    lone.attach_to(window)
    ltwo.attach_to(window)
    print(ltwo.get_midpoint())
    print(ltwo.get_midpoint().x)
    print(ltwo.get_midpoint().y)
    window.render()
    window.close_on_mouse_click()


    """
    -- Constructs a rg.RoseWindow.
    -- Constructs and draws on the window two rg.Lines such that:
          -- They both fit in the window and are easily visible.
          -- One rg.Line has the default thickness.
          -- The other rg.Line is thicker (i.e., has a bigger width).
    -- Uses a rg.Line method to get the midpoint (center) of the
         thicker rg.Line.
    -- Then prints (on the console, on SEPARATE lines):
         -- the midpoint itself
         -- the x-coordinate of the midpoint
         -- the y-coordinate of the midpoint

       Here is an example of the output on the console, if the two
       endpoints of the thicker line are at (100, 100) and (121, 200):
            Point(110.5, 150.0)
            110.5
            150.0

    -- Waits for the user to press the mouse, then closes the window.
    """
    # ------------------------------------------------------------------
    # DONE: 4. Implement and test this function.
    # ------------------------------------------------------------------


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
