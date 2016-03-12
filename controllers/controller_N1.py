def control_robot(robot):
    from nav import Gps
    from virus import Vps
    import paradigms
    driver = Gps(robot)
    vdriver = Vps(robot, driver)
    vdriver.update_viruses()
    driver.check_scan()
    driver.turn_to("S")
    driver.turn_to("N")
    while True:
        path = paradigms.find_viruses(vdriver, driver)
        if len(path) > 1:
            print repr(path[len(path)-1])
            print('Following Path: ' + '\n' + repr(path))
            print('virus list: '+ '\n'+ repr(vdriver.virus_list))
            driver.follow_path(path)
            if path[len(path)-1] in vdriver.virus_list:
                vdriver.remove_virus(path[len(path)-1])
                print('found virus at' + '\n' + repr(path[len(path)-1]))

    """ Control robot.

    Keyword arguments:
    robot -- Robot object that must be controlled through the maze.

    """
    print("reached the end of code")
    pass