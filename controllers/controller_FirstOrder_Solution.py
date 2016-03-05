def control_robot(robot):
    """ Control robot.

    Keyword arguments:
    robot -- Robot object that must be controlled through the maze.

    """

    path = []                               # Previous locations
    location = [0, 0, "N"]                  # Current Location (X, Y, Orientation) start position of robot is (0, 0 "N")
    dictionary_map = \
        {                       # Dictionary with keys for each seen location
            (0, 0): [[],                        # First item in list: list of spots you can move to from key
                     [],                        # Second item in list: list of spots you cannot move to from key
                     [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Third item in list: list of spots you do not know if you can
                     ]                          # move to from key.
        }                                   # Only defines relationship between key and four adjacent spots.

    def sense():                            # New sense function
        adjacencies = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        def check_sense(direction):         # Function to check if you need to sense
            robot_orientation = location[2]  # Robot orientation
            robot_location = (location[0], location[1])  # Robot location
            numeric_direction = []            # Two coordinates that act as a numeric direction
            td_number = 0                   # Integer initially is orientation then becomes absolute numeric direction
            if robot_orientation == "N":    # Numbers are 0-3 for each direction
                td_number = 3
            elif robot_orientation == "E":
                td_number = 2
            elif robot_orientation == "S":
                td_number = 1
            elif robot_orientation == "W":
                td_number = 0
            if direction == "Forward":      # The direction it senses causes the td_number to change so that
                td_number = td_number       # It takes into account orientation and direction
            elif direction == "Left":
                td_number = (td_number + 3) % 4
            elif direction == "Right":
                td_number = (td_number + 1) % 4
            if td_number == 3:
                numeric_direction = adjacencies[0]
            elif td_number == 2:
                numeric_direction = adjacencies[1]
            elif td_number == 1:
                numeric_direction = adjacencies[2]
            elif td_number == 0:
                numeric_direction = adjacencies[3]
                #preconditions: robot_location=(0,0), numeric_direction=(0,1),
            def recursive_sense_function(robot_location, numeric_direction):
                """
                :type robot_location: tuple
                :type numeric_direction: tuple
                :rtype: str
                """
                new_location = (robot_location[0] + numeric_direction[0], robot_location[1] + numeric_direction[1])
                dict_contents = dictionary_map[robot_location]
                i = 0
                while i < len(dict_contents):
                    j = 0
                    while j < len(dict_contents[i]):
                        if dict_contents[i][j] == new_location:
                            if i == 1:
                                return "Don't Check"
                            elif i == 2:
                                return "Check"
                            elif i == 0:
                                return recursive_sense_function(numeric_direction, new_location)
                        j += 1
                    i += 1
            return recursive_sense_function(robot_location, numeric_direction)
        # if check_sense("Forward") == "Check":
        #     for step in
        # if elifs for f, r, l, need to iterate through all steps in sense steps with unknowns and knowns

    def step_forward(steps):                # New function for robot.step_forward so that it changes current Location
        robot.step_forward(steps)
        if location[2] == "N":              # Location changes based on steps and orientation
            location[1] += steps
        elif location[2] == "S":
            location[1] -= steps
        elif location[2] == "E":
            location[0] += steps
        elif location[2] == "W":
            location[0] -= steps
        path.append(location)

    def turn_left(degree):                  # New Function for robot.turn_left so that it changes current location
        robot.turn_left(degree)
        if location[2] == "N":              # Orientation changes based on current location
            location[2] = "W"
        elif location[2] == "S":
            location[2] = "E"
        elif location[2] == "E":
            location[2] = "N"
        elif location[2] == "W":
            location[2] = "S"
        path.append(location)

    def turn_right(degree):                 # New Function for robot.turn_right so that it changes current location
        robot.turn_right(degree)
        if location[2] == "N":              # Orientation changes based on current location
            location[2] = "E"
        elif location[2] == "S":
            location[2] = "W"
        elif location[2] == "E":
            location[2] = "S"
        elif location[2] == "W":
            location[2] = "N"
        path.append(location)

    def step_backward(steps):               # New Function for robot.step_backwards so that it changes current location
        robot.step_backward(steps)
        if location[2] == "N":              # Coordinates change based on steps and orientation.
            location[1] -= steps
        elif location[2] == "S":
            location[1] += steps
        elif location[2] == "E":
            location[0] -= steps
        elif location[2] == "W":
            location[0] += steps
        path.append(location)
    if sense():
        robot.step_backward()
    else:
        robot.step_forward()
"""
    directions = [                          # List with steps in each direction, updated according to need
        robot.sense_steps(robot.SENSOR_FORWARD),
        robot.sense_steps(robot.SENSOR_LEFT),
        robot.sense_steps(robot.SENSOR_RIGHT)
    ]

    if directions[1] == 0:                  # If/Else to find steps behind start position
        turn_right(1)
        directions.append(robot.sense_steps(robot.SENSOR_RIGHT))
        turn_left(1)
    else:                                   # Makes it so that robot does not turn its back on a pathway
        turn_left(1)
        directions.append(robot.sense_steps(robot.SENSOR_LEFT))
        turn_right(1)

    while True:                             # Start of continuous path finding code

        if directions[0] != 0:              # Finds the order of importance is forward, left, right, backwards.
            n = directions[0]               # The first in the order of importance that is not 0 is the direction
        elif directions[1] != 0:             # The robot goes
            n = directions[1]
            turn_left(1)
        elif directions[2] != 0:
            n = directions[2]
            turn_right(1)
        else:
            n = directions[3]
            turn_right(2)

        while n > 0:                        # After the robot chooses which way it is going, every step it checks
            step_forward(1)                 # Its surrounding
            n -= 1
            directions[0] = robot.sense_steps(robot.SENSOR_FORWARD)     # Update directions forward, left, and right
            directions[1] = robot.sense_steps(robot.SENSOR_LEFT)
            directions[2] = robot.sense_steps(robot.SENSOR_RIGHT)
            if directions[1] != 0:                                      # If can go left
                turn_left(1)                                            # Turn left and step once
                step_forward(1)
                if robot.sense_steps(robot.SENSOR_RIGHT) > 0 and directions[0] != 0:    # If looks like a room
                    step_forward(directions[1] - 1)                                     # Walk to edge
                    turn_right(2)                                                       # Turn around
                    x = robot.sense_steps(robot.SENSOR_LEFT)                            # Dimensions of room
                    y = robot.sense_steps(robot.SENSOR_FORWARD)
                    while x >= 0:                                       # Loop for exploring room
                        if x > 1:                                       # If the far wall from start is greater
                            step_forward(y)                             # Than one step away, walk two rows at a time
                            turn_left(1)
                            step_forward(1)
                            turn_left(1)
                            step_forward(y)
                            turn_right(1)
                            step_forward(1)
                            turn_right(1)
                        elif x == 1:                                    # If far wall from start is one step away
                            step_forward(y)                             # Continue until in top left corner
                            turn_left(1)
                            step_forward(1)
                            turn_left(1)
                            step_forward(y)
                            step_backward(y)
                            turn_right(2)                                # Go to upper right and turn around
                        elif x == 0 and robot.sense_steps(robot.SENSOR_LEFT) == 0:
                            step_forward(y)
                        x -= 2

                n = directions[1] - 1

            elif directions[2] != 0:
                turn_right(1)
                step_forward(1)
                if robot.sense_steps(robot.SENSOR_LEFT) > 0 and directions[0] != 0:
                    step_forward(directions[2] - 1)
                    turn_right(2)
                    x = robot.sense_steps(robot.SENSOR_RIGHT)
                    y = robot.sense_steps(robot.SENSOR_FORWARD)
                    while x >= 0:
                        if x > 1:
                            step_forward(y)
                            turn_right(1)
                            step_forward(1)
                            turn_right(1)
                            step_forward(y)
                            turn_left(1)
                            step_forward(1)
                            turn_left(1)
                        elif x == 1:
                            step_forward(y)
                            turn_right(1)
                            step_forward(1)
                            turn_right(1)
                            step_forward(y)
                        elif x == 0 and robot.sense_steps(robot.SENSOR_RIGHT) == 0:
                            step_forward(y)
                            step_backward(y)
                            turn_right(2)
                n = directions[2] - 1

        directions[0] = 0
        directions[1] = robot.sense_steps(robot.SENSOR_LEFT)
        directions[2] = robot.sense_steps(robot.SENSOR_RIGHT)
        turn_right(1)
        directions[3] = robot.sense_steps(robot.SENSOR_RIGHT)
        turn_left(1)
"""