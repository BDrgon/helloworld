# here are the various paradigms, which use different rules to decide target points
# which are passed to djk. The gps navigates the resultant path.
import random
from nav import Gps
import virus
import functions

"""
random_motion works
find_unknowns works
find_packets works
find_viruses worksish
"""
#TODO get the viruses
#got the packets
def random_motion(Gps):
    choices = Gps.map.keys()
    choice = random.choice(choices)
    # print("choice is:"+"\n"+repr(choice)) not sure why it hates this line
    return functions.djk(Gps, choice) #Return a random key from the map


def find_unknowns(Gps): #return the closest key with an unknown
    unk=[]
    for key in Gps.map:
        if len(Gps.map[key][2]) != 0:
            unk.append(key)
    if len(unk) > 0:
        return functions.find_shortest_path(Gps, unk)
    else:
        return random_motion(Gps) #if no key has an unknown, revert to random motion paradigm


def find_packets(Gps):
    if Gps.packet_num <= len(Gps.packets):
        if Gps.packets[Gps.packet_num] in Gps.map:
            return functions.djk(Gps, Gps.packets[Gps.packet_num])
    return find_unknowns(Gps)



def find_viruses(Vps, Gps):  #return the closest reachable virus and resense for viruses when necessary
    reachable_v=[]
    for v in Vps.virus_list:
        if v in Gps.map:
            reachable_v.append(v)
    if len(reachable_v)>0:
        path= functions.find_shortest_path(Gps, reachable_v)
        Vps.remove_virus(path[len(path) - 1])
        if len(reachable_v)==0:
            Vps.update_viruses()
        return path
    else:
        Vps.update_viruses()
        return find_unknowns(Gps)


