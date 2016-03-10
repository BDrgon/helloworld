import functions


class virus:
    #TODO perhaps merge this class with nav
    #TODO add another list to map to store local virus/packet locations? right now they're stored as lists of keys

    def __init__(self, bot):  # bot is the default robot object provided by MESA
        self.virus_list = [] #for every virus sensed, place a tuple in a list
        packets = []
        for x in xrange(0,10): #TODO: how many packets are there? How do we find out how many?
            packets.append([]) #TODO: do we get an initial list of packets? that would help
        self.robot = bot  # Extend the default robot functions into nav.

    def updateViruses(self, bot):
        naive_virus_list = self.robot.sense_viruses() #grab the relative coordinates from robot
                                                      #TODO what data structure is sense_viruses returning?
                                                      #I'm assuming for now it's returning a list of tuples
        naive_virus_list=functions.rotate_list(bot, naive_virus_list) #rotate the coordinates to true north
        self.virus_list=functions.translate_list(naive_virus_list)  #translate the coordinates to align with map


