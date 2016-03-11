# Dijkstra's algorithm acts over a connected graph: assume a path between location node and target node exists
# path will be represented as a series of nodes in an ordered list: each node is connected to the next in the list
# via an edge. The algorithm finds the shortest list of said nodes that accurately lead to the target node.
import random

def djk(gps, target):  # pass the robot class and the target location
    map = gps.map  # easier access to the current map of the level
    location = gps.location # this is the starting location
    location = (location[0], location[1]) # location needs to be a tuple of (x, y) to work as a key for the dicts.
    infinity = 10e300000  # this is how you make infinity in python
    unvisited = {}  # all points start in unvisited. as djk works over to them they are moved out of unvisited and into frontier
    frontier = {}  # Frontier grabs the closest (shortest path length) point from unvisited and explores its options
    explored = {}  # Points guaranteed to have an optimal path after they have been through frontier
    for point in map:  # add all the key in the map to the unvisited list
        unvisited[point] = [[], infinity]
    unvisited.pop(location)  # remove the starting location from list of unvisited points
    frontier[location] = [[location], 0]

    loc = location  # loc is the current node. It start out on the current position
    while True:  # inifinite loops are ok because we will return out of it
        if len(map[loc][0]) > 0:  # if there are spaces we know we can move to from the current node
            for n in map[loc][0]:  # iterate through the spaces we can move to
                if n in unvisited:  # filter for unvisited nodes only
                    if unvisited[n][1] > frontier[loc][1] + 1:  # If the tenative distance is smaller that the current
                        unvisited[n][1] = frontier[loc][1] + 1  # replace current with tentative
                        unvisited[n][0] = frontier[loc][0]  # take the path to loc
                        unvisited[n][0].append(n)  # add the final step of travel
            explored[loc] = frontier.pop(loc) # move the finalized path to the explored dictionary
        if target in explored:  # if the target location has has a path found to it
            return explored[target][0]  # return the path to target, end djk
        else:
            minimum = infinity
            for m in unvisited:
                if unvisited[m] < minimum:  #
                    loc = m
                    minimum = unvisited[m][1]
            # this is a test


            # if minimum == infinity and len(unvisited) > 0:
            #     return []  # if no path is found return an empty string. This should never happen in practice
            if unvisited.has_key(loc):
                frontier[loc] = unvisited.pop(loc) # This is a vital line of code: it pulls a location
                                                # from unvisited with an optimal path length and begins to explore from it
            else:
                print('unvisited: '+repr(unvisited))
                print('frontier: '+repr(frontier))
                print('explored: '+repr(explored))


#TODO find a better home for these very useful functions
#TODO use these functions to clean up nav considerably (option)
def relative_to_cardinal(robot_direction,left_or_right_or_forward): #input cardinal facing (usually robot)
                                                                    #and left,right, or forward
                                                                    #outputs resulting cardinal direction
    orderedDirectionList= ['E','N','W','S']
    robot_num_direction = orderedDirectionList.index(robot_direction)
    if left_or_right_or_forward == 'forward':
        return orderedDirectionList[robot_num_direction]
    elif left_or_right_or_forward == 'right':
        return orderedDirectionList[(robot_num_direction+1)%4]
    elif left_or_right_or_forward == 'left':
        return orderedDirectionList[(robot_num_direction+3)%4]

def something(Gps):

     if direction == 'E':
            delta =  (1, 0)
        elif direction == 'N':
            delta =  (0, 1)
        elif direction == 'W':
            delta = (-1, 0)
        elif direction == 'S':
            delta = (0, -1)
def rotate(degree, point): #uses rotation matrices to rotate cartesian points about the origin
    #all rotation matrices used are counterclockwise and at intervals of 90 degrees
    if degree==0:
        return point
    elif degree==90: #choose the right rotation matrix if rotation is needed
        R= [[0 ,-1],
            [1 , 0]]
    elif degree==180:
        R= [[-1, 0],
            [0 ,-1]]
    elif degree==270:
        R= [[0 , 1],
            [-1, 0]]
    modifiable_point=[]
    modifiable_point.append(point[0]*R[0][0]+point[1]*R[0][1])
    modifiable_point.append(point[0]*R[1][0]+point[1]*R[1][1])
    new_point=(modifiable_point[0],modifiable_point[0])
    return new_point


def rotate_list(Gps,points): #please please please use this technique in nav
    location=Gps.location
    rdirection=location[2]
    from_north= \
        {
            'N':0,
            'W':90,
            'S':180,
            'E':270
        }
    new_list=[]
    for point in points:
        new_list.append(rotate(from_north[rdirection], points))
    return new_list


def translate(vector,point):
    new_point=(point[0]+vector[0],point[1]+vector[1])
    return new_point


def translate_list(robot,points):
    location=robot.location
    vector=(location[0],location[1])
    new_list=[]
    for point in points:
        new_list.append(translate(vector,point))
    return new_list
