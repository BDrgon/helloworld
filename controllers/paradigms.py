# here we will put the various paradigms, which will use different rules to decide target points
# These target points will be passed to djk
import random
from nav import Gps
import virus

"""
random_motion works
"""
def random_motion(Gps):
    choices = Gps.map.keys()
    print("choices are" + repr(choices))
    return random.choice(choices) #Return a random key from the map


def find_unknowns(robot): #return an essentially random key with an unknown adjacent to it
    for key in Gps.map:
        if len(key[2]) != 0:
            return key
    return random_motion(robot) #if no key has an unknown, revert to random motion paradigm


def find_viruses(robot):

    return robot

