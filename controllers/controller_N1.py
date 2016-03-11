# from __future__ import absolute_import
def control_robot(robot):
    from nav import Gps
    import random
    from functions import djk
    from paradigms import random_motion
    driver = Gps(robot)
    driver.check_scan()
    driver.turn_to("S") #why?
    driver.turn_to("N")

    while True:
        target = random.choice()
        path = djk(driver, target)
        if len(path) > 1:
            driver.follow_path(path)
    """ Control robot.

    Keyword arguments:
    robot -- Robot object that must be controlled through the maze.

    """
    print("reached the end of code")
    pass
