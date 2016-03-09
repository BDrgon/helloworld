from __future__ import absolute_import
def control_robot(robot):
    from nav import Gps
    from paradigms import random_motion
    from bag_o_functions import bag_o_functions

    driver = Gps(robot)
    navigator = bag_o_functions()
    bag_o_functions.djk(driver.location, driver.map, random_motion(driver))

    """ Control robot.

    Keyword arguments:
    robot -- Robot object that must be controlled through the maze.

    """
    pass
