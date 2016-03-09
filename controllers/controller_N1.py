def control_robot(robot):
    from __future__ import absolute_import
    from nav import Gps
    from paradigms import random_motion
    from bag_o_functions import bag_o_functions

    driver = Gps(robot)
    navigator = bag_o_functions()


    """ Control robot.

    Keyword arguments:
    robot -- Robot object that must be controlled through the maze.

    """
    pass
