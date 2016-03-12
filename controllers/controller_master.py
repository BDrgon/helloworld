# this will be the highest level controller:
# it first looks for the relevant number packet, then the closest unknown, then viruses
# if it can't find the highest priority, it will default to the next lower state
# Most likely, it will spend most of its time finding unknowns: but when it reveals the next packet
# It will run to it and eat it immediately
# Once all the packets are eaten, perhaps it goes for viruses next?
# TODO figure out how to replace packets with viruses at highest priority once their are no packets left
# TODO figure out how to sense for viruses in a way which makes sense
# anyways, the idea is that the packets need to be found before all the viruses are
# And mapping the place is integral to getting the packets: hence unknowns over viruses in the beginning
# although really, unknowns are the most valuable: they allow us to get the rest, just not priority in search


def control_robot(robot):

    from nav import Gps
    from virus import Vps
    import paradigms
    driver = Gps(robot)
    vdriver = Vps(robot, driver)
    driver.Vps = vdriver
    vdriver.update_viruses()
    driver.check_scan()
    driver.turn_to("S")
    driver.turn_to("N")
    while True:
        if driver.packet_num<=len(driver.packets):
            path = paradigms.find_packets(driver)
        elif driver.robot.num_viruses_left()>0:
            path = paradigms.find_viruses(vdriver, driver)
        else:
            path = paradigms.random_motion(driver)
        if len(path) > 1:
            print repr(path[len(path)-1])
            print('Following Path: ' + '\n' + repr(path))
            print('virus list: '+ '\n'+ repr(vdriver.virus_list))
            driver.follow_path(path)
            if driver.packet_num<=len(driver.packets):
                if path[len(path)-1] == driver.packets[driver.packet_num]:
                    driver.robot.jump()
                    driver.packet_num+=1
            if path[len(path)-1] in vdriver.virus_list:
                vdriver.remove_virus(path[len(path)-1])
                print('found virus at' + '\n' + repr(path[len(path)-1]))
    """ Control robot.

    Keyword arguments:
    robot -- Robot object that must be controlled through the maze.

    """
    print("reached the end of code")
    pass


