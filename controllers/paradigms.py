# here we will put the various paradigms, which will use different rules to decide target points
# These target points will be passed to DJK
import random
def random_motion(robot):
    choices = robot.map.keys()
    return random.choice(choices) #Return a random key from the map