# TODO: store locations of packets and viruses and such
# TODO: make sure importing this module works in practice
import sys



class Gps:
    def __init__(self, bot):  # bot is the default robot object provided by MESA
        self.location = [0, 0, "N"]  # The robot starts at the origin, facing north
        self.map = \
            {
                (0, 0): [  # The key is a tuple of the coordinates of a square
                    [],  # The first list is the spaces that can be moved to from the key
                    [],  # The spaces that cannot be moved to from the key
                    [(0, 1), (0, -1), (1, 0), (-1, 0)]  # The spaces whose relation to the key is unknown
                ]
            }
        self.robot = bot  # Extend the default robot functions into nav.

    def cleanup(self):  # This function will run on every map update in order to clean up inconsistencies in the map
        # if a known point of a key is also a key, add the first key as a point to the second key
        for key in self.map.keys():
            for hall in self.map[key][0]:
                if key not in self.map[hall][0]:
                    self.map[hall][0].append(key)
            for wall in self.map[key][1]:
                if wall in self.map.keys():
                    if key not in self.map[wall][1]:
                        self.map[wall][1].append(key)

        # remove known points from the list of unknown points
        for key in self.map.keys():
            for point in self.map[key][2]:
                if point in self.map[key][0] + self.map[key][1]:
                    self.map[key][2].remove(point)

    def check_scan(self):  # Check if it is necessary to scan in each direction. If so, scan in those directions
        pos = (self.location[0], self.location[1])
        if self.location[2] == "N":
            # check left
            x = False
            point = pos
            while not x:
                left_point = (point[0] - 1, point[1])

                if left_point in self.map[point][0]:
                    point = left_point
                elif left_point in self.map[point][1]:
                    x = True
                elif left_point in self.map[point][2]:
                    x = True  # scanleft
                    self.scan("W", self.robot.sense_steps(self.robot.SENSOR_LEFT))
            x = False
            point = pos
            while not x:
                front_point = (point[0], point[1] + 1)

                if front_point in self.map[point][0]:
                    point = front_point
                elif front_point in self.map[point][1]:
                    x = True
                elif front_point in self.map[point][2]:
                    x = True  # scanfront
                    self.scan("N", self.robot.sense_steps(self.robot.SENSOR_FORWARD))
            x = False
            point = pos
            while not x:
                right_point = (point[0] + 1, point[1])

                if right_point in self.map[point][0]:
                    point = right_point
                elif right_point in self.map[point][1]:
                    x = True
                elif right_point in self.map[point][2]:
                    x = True  # scanright
                    self.scan("E", self.robot.sense_steps(self.robot.SENSOR_RIGHT))
        elif self.location[2] == "E":
            # check left
            x = False
            point = pos
            while not x:
                left_point = (point[0], point[1] + 1)

                if left_point in self.map[point][0]:
                    point = left_point
                elif left_point in self.map[point][1]:
                    x = True
                elif left_point in self.map[point][2]:
                    x = True  # scanleft
                    self.scan("N", self.robot.sense_steps(self.robot.SENSOR_LEFT))
            # check front
            x = False
            point = pos
            while not x:
                front_point = (point[0] + 1, point[1])

                if front_point in self.map[point][0]:
                    point = front_point
                elif front_point in self.map[point][1]:
                    x = True
                elif front_point in self.map[point][2]:
                    x = True  # scanfront
                    self.scan("E", self.robot.sense_steps(self.robot.SENSOR_FORWARD))
            # check right
            x = False
            point = pos
            while not x:
                right_point = (point[0], point[1] - 1)

                if right_point in self.map[point][0]:
                    point = right_point
                elif right_point in self.map[point][1]:
                    x = True
                elif right_point in self.map[point][2]:
                    x = True  # scanright
                    self.scan("S", self.robot.sense_steps(self.robot.SENSOR_RIGHT))
        elif self.location[2] == "S":
            # check left
            x = False
            point = pos
            while not x:
                left_point = (point[0] + 1, point[1])

                if left_point in self.map[point][0]:
                    point = left_point
                elif left_point in self.map[point][1]:
                    x = True
                elif left_point in self.map[point][2]:
                    x = True  # scanleft
                    self.scan("E", self.robot.sense_steps(self.robot.SENSOR_LEFT))
            # check front
            x = False
            point = pos
            while not x:
                front_point = (point[0], point[1] - 1)

                if front_point in self.map[point][0]:
                    point = front_point
                elif front_point in self.map[point][1]:
                    x = True
                elif front_point in self.map[point][2]:
                    x = True  # scanfront
                    self.scan("S", self.robot.sense_steps(self.robot.SENSOR_FORWARD))
            # check right
            x = False
            point = pos
            while not x:
                right_point = (point[0] - 1, point[1])

                if right_point in self.map[point][0]:
                    point = right_point
                elif right_point in self.map[point][1]:
                    x = True
                elif right_point in self.map[point][2]:
                    x = True  # scanright
                    self.scan("W", self.robot.sense_steps(self.robot.SENSOR_RIGHT))

        elif self.location[2] == "W":
            # check left
            x = False
            point = pos
            while not x:
                left_point = (point[0], point[1] - 1)

                if left_point in self.map[point][0]:
                    point = left_point
                elif left_point in self.map[point][1]:
                    x = True
                elif left_point in self.map[point][2]:
                    x = True  # scanleft
                    self.scan("S", self.robot.sense_steps(self.robot.SENSOR_LEFT))
            # check front
            x = False
            point = pos
            while not x:
                front_point = (point[0] - 1, point[1])

                if front_point in self.map[point][0]:
                    point = front_point
                elif front_point in self.map[point][1]:
                    x = True
                elif front_point in self.map[point][2]:
                    x = True  # scanfront
                    self.scan("W", self.robot.sense_steps(self.robot.SENSOR_FORWARD))
            # check right
            x = False
            point = pos
            while not x:
                right_point = (point[0], point[1] + 1)

                if right_point in self.map[point][0]:
                    point = right_point
                elif right_point in self.map[point][1]:
                    x = True
                elif right_point in self.map[point][2]:
                    x = True  # scanright
                    self.scan("N", self.robot.sense_steps(self.robot.SENSOR_RIGHT))

    def scan(self, cardinal, steps):
        point = (self.location[0], self.location[1])
        steps = int(steps)
        if cardinal == "N":
            for x in range(steps):
                self.map[point][0].append((point[0], point[1]+1))
                point = (point[0], point[1]+1)
                newentry = {point:[[], [], [(point[0], point[1]+1), (point[0], point[1]-1), (point[0]+1, point[1]), (point[0]-1, point[1])]]}
                self.map.update(newentry)
            self.map[point][1].append((point[0], point[1]+1))
        if cardinal == "S":
            for x in range(steps):
                self.map[point][0].append((point[0], point[1]-1))
                point = (point[0], point[1]-1)
                newentry = {point:[[], [], [(point[0], point[1]+1), (point[0], point[1]-1), (point[0]+1, point[1]), (point[0]-1, point[1])]]}
                self.map.update(newentry)
            self.map[point][1].append((point[0], point[1]-1))
        if cardinal == "E":
            for x in range(steps):
                self.map[point][0].append((point[0]+1, point[1]))
                point = (point[0]+1, point[1])
                newentry = {point:[[], [], [(point[0], point[1]+1), (point[0], point[1]-1), (point[0]+1, point[1]), (point[0]-1, point[1])]]}
                self.map.update(newentry)
            self.map[point][1].append((point[0]+1, point[1]))
        if cardinal == "W":
            for x in range(int(steps)):
                self.map[point][0].append((point[0]-1, point[1]))
                point = (point[0]-1, point[1])
                newentry = {point:[[], [], [(point[0], point[1]+1), (point[0], point[1]-1), (point[0]+1, point[1]), (point[0]-1, point[1])]]}
                self.map.update(newentry)
            self.map[point][1].append((point[0]-1, point[1]))
        self.cleanup()

    def step_forward(self, steps):  # Encapsulating function for the default step_forward function
        self.robot.step_forward(steps)
        self.check_scan()
        return

    def step_backward(self, steps):
        self.robot.step_backward(steps)
        self.check_scan

    def turn_left(self, degree):
        self.robot.turn_left(degree)

    def turn_right(self, degree):  # Turning right is just turning left in the other direction!
        self.robot.turn_right(degree)

    def turn_to(self, bearing):
        sys.stdout("turn_to(" + bearing + ")\n" )
        current = self.location[2]
        if bearing == current:
            return # do nothing
        # conditions that result in turning left
        if (current == "N" and bearing == "W") or (current == "W" and bearing == "S") or current == "S" and bearing == "E" or current == "E" and bearing == "N":
            self.turn_left(1)
        #conditions that result in turning right
        if current == "N" and bearing == "E" or current == "W" and bearing == "N" or current == "S" and bearing == "W" or current == "E" and bearing == "S":
            self.turn_right(1)
        #conditions that result in a U-turn
        if current == "N" and bearing == "S" or current == "W" and bearing == "E" or current == "S" and bearing == "N" or current == "E" and bearing == "W":
            self.turn_left(2)
        self.location[2] = bearing

    def go_north(self):
        self.turn_to("N")
        self.step_forward(1)
        self.location[1] += 1

    def go_east(self):
        self.turn_to("E")
        self.step_forward(1)
        self.location[0] += 1

    def go_south(self):
        self.turn_to("S")
        self.step_forward(1)
        self.location[1] -= 1

    def go_west(self):
        self.turn_to("W")
        self.step_forward(1)
        self.location[0] -= 1

    def turn_to(self, bearing):
        current = self.location[2]
        if bearing == current:
            return # do nothing
        # conditions that result in turning left
        if (current == "N" and bearing == "W") or (current == "W" and bearing == "S") or current == "S" and bearing == "E" or current == "E" and bearing == "N":
            self.turn_left(1)
        #conditions that result in turning right
        if current == "N" and bearing == "E" or current == "W" and bearing == "N" or current == "S" and bearing == "W" or current == "E" and bearing == "S":
            self.turn_right(1)
        #conditions that result in a U-turn
        if current == "N" and bearing == "S" or current == "W" and bearing == "E" or current == "S" and bearing == "N" or current == "E" and bearing == "W":
            self.turn_left(2)
        self.location[2] = bearing
        self.check_scan()

    def follow_path(self, path):  # This is not complete its just pseudocode-ish and we need to define cardinal moves
        for x in path[0]:
            if x[0] == self.location[0] and x[1] == self.location[1]:
                print "I did not move"
            elif x[0] == self.location[0] + 1:
                self.go_east()
            elif x[0] == self.location[0] - 1:
                self.go_west()
            elif x[1] == self.location[1] + 1:
                self.go_north()
            elif x[1] == self.location[1] - 1:
                self.go_south()
