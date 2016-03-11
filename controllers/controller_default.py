def control_robot(robot):
    from nav import Gps
    from functions import djk
    import paradigms
    driver = Gps(robot)
    driver.check_scan()
    driver.turn_to("S") #why?
    driver.turn_to("N")
    print("is anybody still here")
    for x in xrange(100):
        target = paradigms.find_unknowns(driver)
        print repr(target)
        path = djk(driver, target)
        if len(path) > 1:
            print('Following Path: ' + '\n' + repr(path))
            driver.follow_path(path)
    """ Control robot.

    Keyword arguments:
    robot -- Robot object that must be controlled through the maze.

    """
    print("reached the end of code")
    pass

