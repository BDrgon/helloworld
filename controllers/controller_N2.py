def control_robot(robot):

    from nav import Gps

    driver=Gps(robot)

    def print_stuff():
        print "map: \n" + repr(driver.map) + "\nlocation:\n" + repr(driver.location)
    print "initial map:"
    print driver.map
    print "initial location:"
    print driver.location
    driver.turn_to("S")
    print "faced south"
    print_stuff()
    driver.turn_to("N")
    print "faced north"
    print_stuff()
    """ Control robot.

    Keyword arguments:
    robot -- Robot object that must be controlled through the maze.

    """
    pass
