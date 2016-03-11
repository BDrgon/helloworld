# here we will put the various paradigms, which will use different rules to decide target points
# These target points will be passed to djk and ultimately the gps will navigate to them
import random
from nav import Gps
import virus
import functions

"""
random_motion works
find_unknowns works
find_viruses works
"""
#got the viruses
#TODO get packets
def random_motion(Gps):
    choices = Gps.map.keys()
    choice = random.choice(choices)
    # print("choices is:"+"\n"+repr(choice)) not sure why it hates this line
    return functions.djk(Gps, choice) #Return a random key from the map


def find_unknowns(Gps): #return an essentially random key with an unknown adjacent to it
    unk=[]
    for key in Gps.map:
        if len(Gps.map[key][2]) != 0:
            unk.append(key)
    if len(unk) > 0:
        return functions.find_shortest_path(Gps, unk)
    else:
        return random_motion(Gps) #if no key has an unknown, revert to random motion paradigm

def find_packets(Gps):
    """
    :rtype: list
    """
    if Gps.packets[Gps.packet_num] in Gps.map and not (Gps.packet_num>=len(Gps.packets)):
        return functions.djk(Gps, Gps.packets[Gps.packet_num])
    else:
        return find_unknowns(Gps)



def find_viruses(Vps, Gps):  #return the closest reachable virus and resense for viruses when necessary
    reachable_v=[]
    if len(Vps.virus_list)>0:
        for v in Vps.virus_list:
            if v in Gps.map:
                reachable_v.append(v)
    if len(reachable_v)>0:
        path= functions.find_shortest_path(Gps, reachable_v)
        Vps.decrement_virus(path[len(path)-1])
        return path
    else:
        return find_unknowns(Gps)


