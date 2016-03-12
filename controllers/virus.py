import functions


class Vps: #virus positional system
    #TODO convert virus_list to set

    def __init__(self, bot, gdriver):  # bot is the default robot object provided
        self.robot = bot  # Extend the default robot functions into virus.py
        self.gdriver=gdriver  # Driver for nav/Gps
        self.virus_list=[]
        self.black_list=[]
        self.total_number=self.robot.num_viruses_left()
        self.squares_sensed=set() #no literal for set, so define it as set()
        #squares_sensed will contain a simple unordered list of keys which have been sensed for viruses
        #it will be used to determine whether the robot needs to virus_sense
        self.vector_circle=[] #the set of points used to define the relative sense_virus() sweep area
        #and its used to update the set squares_sensed. Only calculated once, used every time we sense.
        self.populate_circle()

    def update_viruses(self):
        naive_virus_additions = self.robot.sense_viruses()  # grab the relative coordinates from robot
                                                            # n_v_a is a list of list-points
        self.update_squares_sensed()  #update the squares we've sensed. includes all the virus additions
        for n in xrange(0,len(naive_virus_additions)):
            naive_virus_additions[n]= (int(naive_virus_additions[n][0]),
                                       int(naive_virus_additions[n][1])) # convert each inner list-point to a 2-tuple
            # naive_virus_additions.append( (n[0], n[1]) )  # convert each inner list-point to a 2-tuple
            # naive_virus_additions.remove(n)  #remove the inner list-points
        aligned_virus_additions=functions.rotate_list_north(self.gdriver, naive_virus_additions) #rotate the coordinates to true north
        additions=functions.translate_list(self.gdriver, aligned_virus_additions)  #translate the coordinates to align with map

        for v in additions:  #take the list of additions one at a time
            if v not in self.virus_list and v not in self.black_list:  #check if we already have them covered
                self.virus_list.append(v)  #if not, add them to the list
    # def update_squares_sensed(self):

    def remove_virus(self, to_remove):
        self.virus_list.remove(to_remove)
        if self.total_number==self.robot.num_viruses_left()-len(self.black_list):
            self.black_list.append(to_remove)
        self.total_number=self.robot.num_viruses_left()-len(self.black_list)

    def populate_circle(self): #populate_circle generates a quarter circle manually and then rotates it to populate vector_circle
    #  populate_circle will only be called at startup: as the vector_circle doesn't change, only how it is translated
        q_circle=[] #the quarter circle as a list of tuples
        for x in xrange(1,8): #generate the largest part of the quarter circle as a rectangle of 7*8 (1 to 7 by 0 to 7)
            for y in xrange(0,8):
                q_circle.append((x,y))
        #don't include the slice of x where x=0, because the slice where y=0 will rotate to include it later (hence x for 1 to 7)
        #manually generate the slices of the quarter circle which are not part of the square
        for y in xrange(0,7): #add vertical slice to the right of the rectangle @ x=8
            q_circle.append((8,y))
        for y in xrange(0,5): #add vertical slice to the right @ x=9
            q_circle.append((9,y))
        q_circle.append((10,0)) #add vertical slice to the right @ x=10. Only one value
        for x in xrange(1,7): #
            q_circle.append((x,8))
        for x in xrange(1,5):
            q_circle.append((x,9))
        #after these opperations, we have a quarter circle of radius 10 inclusive of the 0 functions.
        self.vector_circle += q_circle
        self.vector_circle += functions.rotate_list(90,q_circle)
        self.vector_circle += functions.rotate_list(180, q_circle)
        self.vector_circle += functions.rotate_list(270, q_circle)
        self.vector_circle.append((0,0))
        #the quarter circle has been rotated and added to vector_circle so v_circle is now a full vector circle with no repetitions

    def update_squares_sensed(self): #use functions to translate vector_circle to the actual map values we've just sensed
                                     #and add them to the set of all squares sensed for viruses.
        self.squares_sensed.update(functions.translate_list(self.gdriver, self.vector_circle))
        #this one liner will update squares_sensed with the absolute map locations of each sensed point
        #even when the circle overlaps with previously sensed squares (should always be the case), sensed_squares will
        #only update new values, as sets will do that for you with the set.update() call

    def check_if_in_squares_sensed(self, point):
        if point not in self.squares_sensed:
            self.update_viruses()




