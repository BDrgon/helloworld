def control_robot(robot):
    from nav import Gps
    import paradigms
    driver = Gps(robot)
    driver.check_scan()
    driver.turn_to("S") #why?
    driver.turn_to("N")
    while True:
        path = paradigms.find_packets(driver)
        print "wtf+ "+repr(path)
        if len(path) > 1:
            print repr(path[len(path)-1])
            print('Following Path: ' + '\n' + repr(path))
            driver.follow_path(path)
            if driver.packet_num<=len(driver.packets):
                if path[len(path)-1] == driver.packets[driver.packet_num]:
                    driver.robot.jump()
                    driver.packet_num+=1
    """ Control robot.
    Keyword arguments:
    robot -- Robot object that must be controlled through the maze.
    """
    print("reached the end of code")
    pass
