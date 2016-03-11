import functions


class Vps:
    #TODO perhaps merge this class with nav
    #TODO add another list to map to store local virus/packet locations? right now they're stored as lists of keys

    def __init__(self, bot, gdriver):  # bot is the default robot object provided by MESA
        self.robot = bot  # Extend the default robot functions into nav.
        self.gdriver=gdriver
        self.virus_list=[]
        self.total_number=bot.num_viruses_left()

    def update_viruses(self):
        naive_virus_additions = self.robot.sense_viruses()  # grab the relative coordinates from robot
                                                      # n_v_a is a list of lists
        for n in naive_virus_additions:
            naive_virus_additions.append((n[0],n[1]))  # convert each inner point to a tuple
            naive_virus_additions.remove(n)  #clean up the inner lists
        aligned_virus_additions=functions.rotate_list(self.gdriver, naive_virus_additions) #rotate the coordinates to true north
        additions=functions.translate_list(self.gdriver, aligned_virus_additions)  #translate the coordinates to align with map

        for v in additions:  #take the list of additions one at a time
            if v not in self.virus_list:  #check if we already have them covered
                self.virus_list.append(v)  #if not, add them to the list

    def decrement_virus(self, to_remove):
        self.virus_list.remove(to_remove)
        self.total_number-=1


