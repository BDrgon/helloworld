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
        point = (self.location[0], self.location[1])
        if self.location[2] == "N":
            # check left
            x = False
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
                point = (point(0), point(1)+1)
            self.map[point][1].append((point[0], point[1]+1))
        if cardinal == "S":
            for x in range(steps):
                self.map[point][0].append((point[0], point[1]-1))
                point = (point(0), point(1)+1)
            self.map[point][1].append((point[0], point[1]-1))
        if cardinal == "E":
            for x in range(steps):
                self.map[point][0].append((point[0], point[1]-1))
                point = (point(0), point(1)+1)
            self.map[point][1].append((point[0], point[1]-1))
        if cardinal == "W":
            for x in range(steps):
                self.map[point][0].append((point[0], point[1]-1))
                point = (point(0), point(1)+1)
            self.map[point][1].append((point[0], point[1]-1))

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
        return

    def step_backward(self, steps):
        self.step_forward(-steps)

    def turn_left(self, degree):  # Encapsulation for the default turn_left function
        if degree % 4 == 0:
            return  # if you turn four times you should not turn at all.
        elif degree % 4 == 1 or 2:
            self.robot.turn_left(degree % 4)  # turn left or right depending on which turn is more efficient
        elif degree % 4 == 3:
            self.robot.turn_right(-degree % 4)

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

    def turn_right(self, degree):  # Turning right is just turning left in the other direction!
        self.turn_left(-degree)
