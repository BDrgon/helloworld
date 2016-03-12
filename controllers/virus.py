import functions


class Vps: #virus positional system
    #TODO perhaps merge this class with nav
    #TODO add another list to map to store local virus/packet locations? right now they're stored as lists of keys

    def __init__(self, bot, gdriver):  # bot is the default robot object provided
        self.robot = bot  # Extend the default robot functions into virus.py
        self.gdriver=gdriver  # Driver for nav/Gps
        self.virus_list=[]
        self.total_number=self.robot.num_viruses_left()
        self.squares_sensed=[]
        self.black_list=[]

    def update_viruses(self):
        naive_virus_additions = self.robot.sense_viruses()  # grab the relative coordinates from robot
                                                            # n_v_a is a list of list-points
        for n in xrange(0,len(naive_virus_additions)):
            naive_virus_additions[n]= (naive_virus_additions[n][0], naive_virus_additions[n][1]) # convert each inner list-point to a 2-tuple
            # naive_virus_additions.append( (n[0], n[1]) )  # convert each inner list-point to a 2-tuple
            # naive_virus_additions.remove(n)  #remove the inner list-points
        aligned_virus_additions=functions.rotate_list(self.gdriver, naive_virus_additions) #rotate the coordinates to true north
        additions=functions.translate_list(self.gdriver, aligned_virus_additions)  #translate the coordinates to align with map

        for v in additions:  #take the list of additions one at a time
            if v not in self.virus_list and v not in self.black_list:  #check if we already have them covered
                self.virus_list.append(v)  #if not, add them to the list
    # def update_squares_sensed(self):

    def remove_virus(self, to_remove):
        self.virus_list.remove(to_remove)
        if self.total_number==self.robot.num_viruses_left():
            self.black_list.append(to_remove)
        self.total_number=self.robot.num_viruses_left()



