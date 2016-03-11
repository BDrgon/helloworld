##this will be the highest level controller:
# it first looks for the relevant number packet, then the closest unknown, then viruses
#if it can't find the highest priority, it will default to the next lower state
#Most likely, it will spend most of its time finding unknowns: but when it reveals the next packet
#It will run to it and eat it immediately
#Once all the packets are eaten, perhaps it goes for viruses next?
#TODO figure out how to replace packets with viruses at highest priority once their are no packets left
#TODO figure out a sensible way to continue to sense and store viruses
#anyways, the idea is that the packets are the most valuable thing the robot can find
#And mapping the place is integral to getting the packets: hence unknowns over viruses in the beginning


def control_robot(robot):
    from nav import Gps
    import paradigms
    driver = Gps(robot)
    driver.check_scan()
    driver.turn_to("S") #why?
    driver.turn_to("N")
    while True:
        path = paradigms.find_unknowns(driver)
        if len(path) > 1:
            print repr(path[len(path)-1])
            print('Following Path: ' + '\n' + repr(path))
            driver.follow_path(path)
    """ Control robot.

    Keyword arguments:
    robot -- Robot object that must be controlled through the maze.

    """
    print("reached the end of code")
    pass


