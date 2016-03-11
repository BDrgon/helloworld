def control_robot(robot):
    from nav import Gps
    import paradigms
    driver = Gps(robot)
    driver.check_scan()
    driver.turn_to("S")
    driver.turn_to("N")
    while True:
        path = paradigms.find_packets(driver)
        if len(path) > 1:
            print repr(path[len(path)-1])
            print('Following Path: ' + '\n' + repr(path))
            driver.follow_path(path)
            driver.robot.jump()
    """ Control robot.

    Keyword arguments:
    robot -- Robot object that must be controlled through the maze.

    """
    print("reached the end of code")
    pass
