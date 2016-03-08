class Gps:
    def __init__(self, bot):  # bot is the default robot object provided by MESA
        self.location = [0, 0, "N"]  # The robot starts at the origin, facing north
        self.map = \
            {
                (0, 0): [  # The key is a tuple of the coordinates of a square
                    []  # The first list is the spaces that can be moved to from the key
                    , []  # The spaces that cannot be moved to from the key
                    , [(0, 1), (0, -1), (1, 0), (-1, 0)]  # The spaces whose relation to the key is unknown
                ]
            }

        self.robot = bot  # Extend the default robot functions into nav.

    def check_scan(self):
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
                    self.scan("N", self.robot.sense_steps(self.robot.SENSOR_FRONT))
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
                    self.scan("E", self.robot.sense_steps(self.robot.SENSOR_FRONT))
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
                    self.scan("S", self.robot.sense_steps(self.robot.SENSOR_FRONT))
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
                    self.scan("W", self.robot.sense_steps(self.robot.SENSOR_FRONT))
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

    def step_forward(self, steps):  # Encapsulating function for the default step_forward function
        if steps == 0:
            return
        elif steps > 0:
            self.robot.step_forward(steps)  # Step step forward like the default function would
        elif steps < 0:
            self.robot.step_backward(abs(steps))

        if self.location[2] == "N":  # if facing north, add steps to Y-coord
            self.location[1] += steps
        elif self.location[2] == "S":  # if facing south, subtract from Y-coord
            self.location[1] -= steps
        elif self.location[2] == "E":  # if facing east, add to X-coord
            self.location[0] += steps
        elif self.location[2] == "W":  # if facing west, subtract from X-coord
            self.location[0] -= steps
        self.check_scan()
        return

    def step_backward(self, steps):
        self.step_forward(-steps)

    def turn_left(self, degree):  # Encapsulation for the default turn_left function
        if degree == 0 or degree == 4:
            return  # if you turn four times you should not turn at all.
        elif degree == 1 or degree == 2:
            self.robot.turn_left(degree)  # turn left or right depending on which turn is more efficient
        elif degree == 3:
            self.robot.turn_right(4-degree)
        degree = -degree #the code below was done wrong but its easier to
            # check orientation and update the position based on the turn.
        if self.location[2] == "N" and degree % 4 == 1 or \
                                self.location[2] == "W" and degree % 4 == 2 or \
                                self.location[2] == "S" and degree % 4 == 3:
            self.location[2] = "E"
        elif self.location[2] == "E" and degree % 4 == 1 or \
                                self.location[2] == "N" and degree % 4 == 2 or \
                                self.location[2] == "W" and degree % 4 == 3:
            self.location[2] = "S"
        elif self.location[2] == "S" and degree % 4 == 1 or \
                                self.location[2] == "E" and degree % 4 == 2 or \
                                self.location[2] == "N" and degree % 4 == 3:
            self.location[2] = "W"
        elif self.location[2] == "W" and degree % 4 == 1 or \
                                self.location[2] == "S" and degree % 4 == 2 or \
                                self.location[2] == "E" and degree % 4 == 3:
            self.location[2] = "N"
        self.check_scan()

    def turn_right(self, degree):  # Turning right is just turning left in the other direction!
        self.turn_left(4-degree)

    def go_north(self):
        if self.location[2] == "N":
            self.step_forward(1)
        elif self.location[2] == "E":
            self.turn_left(1)
            self.step_forward(1)
        elif self.location[2] == "S":
            self.turn_left(2)
            self.step_forward(1)
        elif self.location[2] == "W":
            self.turn_right(1)
            self.step_forward(1)
        print "I went North"

    def go_east(self):
        if self.location[2] == "N":
            self.turn_left(3)
            self.step_forward(1)
        elif self.location[2] == "E":
            self.step_forward(1)
        elif self.location[2] == "S":
            self.turn_left(1)
            self.step_forward(1)
        elif self.location[2] == "W":
            self.turn_left(2)
            self.step_forward(1)
        print "I went East"

    def go_south(self):
        if self.location[2] == "N":
            self.turn_left(2)
            self.step_forward(1)
        elif self.location[2] == "E":
            self.turn_left(3)
            self.step_forward(1)
        elif self.location[2] == "S":
            self.step_forward(1)
        elif self.location[2] == "W":
            self.turn_left(1)
            self.step_forward(1)
        print "I went South"

    def go_west(self):
        if self.location[2] == "N":
            self.turn_left(1)
            self.step_forward(1)
        elif self.location[2] == "E":
            self.turn_left(2)
            self.step_forward(1)
        elif self.location[2] == "S":
            self.turn_left(3)
            self.step_forward(1)
        elif self.location[2] == "W":
            self.step_forward(1)
        print "I went West"

    def follow_path(self, path):  # This is not complete its just pseudocode-ish and we need to define cardinal moves
        for x in path[0]:
            print x
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

naver = Gps(123)
path = [[(0, 0), (-1, 0), (-1, 1), (-2, 1)], 3]
print naver.follow_path(path)
