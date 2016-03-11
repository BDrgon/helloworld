def control_robot(robot):

    from nav import Gps

    driver=Gps(robot)

    driver.turn_to("S")
    driver.turn_to("N")
    driver.go_north()
    """ Control robot.

    Keyword arguments:
    robot -- Robot object that must be controlled through the maze.

    """
    pass
