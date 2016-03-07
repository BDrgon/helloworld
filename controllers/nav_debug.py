from __future__ import absolute_import
from controllers import nav
#fake robot class for debugging literally everything


class FakeRobot:
    def __init__(self):
        pass
        # bitch where?
    SENSOR_LEFT = "left sensor"
    SENSOR_FRONT = "front sensor"
    SENSOR_RIGHT = "right sensor"

    @staticmethod
    def step_forward(steps):
        print("I have just stepped forward " + str(steps))
        return

    @staticmethod
    def step_backward(steps):
        print("I have just stepped backward " + str(steps))
        return

    @staticmethod
    def turn_left(amount):
        print("I have just turned left " + str(amount))

    @staticmethod
    def turn_right(amount):
        print("I have just turned right " + str(amount))

    @staticmethod
    def sense_steps(sensor):
        steps = raw_input("enter distance to closest wall seens by " + sensor)
        return int(steps)

robot = FakeRobot()
navigator = nav.Gps(robot)