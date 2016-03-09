#from __future__ import absolute_import
def control_robot(robot):
    from nav import Gps
    from Pathing import  DJK
    from paradigms import random_motion


    driver = Gps(robot)
    driver.turn_to("S")
    driver.turn_to("N")

    while True:
        print("entered inifinite loop")
        target = random_motion(driver)
        switcher = True
        while switcher:
            path = DJK(driver, target)
            if len(path) != 0:
                switcher = False
        print "path is " + repr(path)
        path = path[0]
        print "path is shortened to " + repr(path)
        for point in path:
            print "point is " + repr(point)
            print "location is" + repr(driver.location)
            if point[0] == driver.location[0]+1 and point[1] == driver.location[1]:
                driver.go_east()
            elif point[0] == driver.location[0]-1 and point[1] == driver.location[1]:
                driver.go_west()
            elif point[0] == driver.location[0] and point[1] == driver.location[1]+1:
                driver.go_north()
            elif point[0] == driver.location[0] and point[1] == driver.location[1]-1:
                driver.go_south()
    """ Control robot.

    Keyword arguments:
    robot -- Robot object that must be controlled through the maze.

    """
    print("reached the end of code")
    pass
