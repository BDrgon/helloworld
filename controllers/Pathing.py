# Dijkstra's algorithm acts over a connected graph: assume a path between location node and target node exists
# path will be represented as a series of nodes in an ordered list: each node is connected to the next in the list
# via an edge. The algorithm finds the shortest list of said nodes that accurately lead to the target node.
from nav import Gps

def DJK(robot, target):  # pass the robot class and the target location
    map = robot.map  # easier access to the current map of the level
    location = robot.location  # this is the starting location
    infinity = 10e300000  # this is how you make inifinity in python
    unvisited = {}  # all points start in unvisited. as DJK works over to them they are moved out of unvisited and into frontier
    frontier = {}  # Frontier grabs the closest (shortest path length) point from unvisited and explores its options
    explored = {}  # Points guaranteed to have an optimal path after they have been through frontier
    for point in map:  # add all the key in the map to the unvisited list
        unvisited[point] = [[], infinity]
    unvisited.pop(location)  # remove the starting location from list of unvisited points
    frontier[location] = [[location], 0]

    loc = location  # loc is the current node. It start out on the current position
    while True:  # inifinite loops are ok because we will return out of it
        if len(map[loc][0] > 0):  # if there are spaces we know we can move to from the current node
            for n in map[loc][0]:  # iterate through the spaces we can move to
                if n in unvisited:  # filter for unvisited nodes only
                    if unvisited[n][1] > frontier[loc][1] + 1:  # If the tenative distance is smaller that the current
                        unvisited[n][1] = frontier[loc][1] + 1  # replace current with tentative
                        unvisited[n][0] = frontier[loc][0]  # take the path to loc
                        unvisited[n][0].append(n)  # add the final step of travel
            explored[loc] = frontier.pop(loc)  # move the finalized path to the explored dictionary
        if target in explored:  # if the target location has has a path found to it
            path = explored[target]  # create the path in a variable
            Gps.follow_path(path)  # run the follow path function with the djk
             return explored[target]  # return the path to target, end DJK
        else:
            minimum = infinity
            for m in unvisited:
                if unvisited[m] < minimum:  #
                    loc = m
                    minimum = unvisited[m][1]
            if minimum == infinity and len(unvisited) > 0:
                return []  # if no path is found return an empty string. This should never happen in practice
            frontier[loc] = unvisited.pop[loc]  # This is a vital line of code: it pulls a location
                                                # from unvisited with an optimal path length and begins to explore from it
