class bag_o_functions:
    map = \
        {
            (0, 0): [
                [(0, 1), (1, 0)],
                [(-1, 0), (0, -1)],
                []
            ],
            (0, 1): [
                [(0, 0), (0, 2)],
                [(-1, 1), (1, 1)],
                []
            ],
            (0, 2): [
                [(0, 1),(0, 3)],
                [],
                [(1, 2), (-1, 2)]
            ],
            (0, 3): [
                [(0, 2)],[],[]
            ]
        }
    """
    Dijkstra's algorithm acts over a connected graph: assume a path between location node and target node exists
    path will be represented as a series of nodes in an ordered list: each node is connected to the next in the list
    via an edge. The algorithm finds the shortest list of said nodes that accurately lead to the target node.
    """
    def DJK(location, map, target):  # full implementation of Dijkstra's algorithm over a dictionary object map
                        # The keys of the dictionary are nodes, and the entries nodes connected to key by an edge
                        # output is a list of instructions that define the shortest path from location to target
        # let's implement Dijkstra's algo:
        # TODO object that represents each node, number of edges, and a shortest path
        # TODO list of nodes to explore
        # TODO list of nodes explored
        # TODO end when target is explored
        # TODO for each explored node, a path list that is how it got there
        # TODO allow unvisited node distances to start at infinity
        # TODO make a frontier list which contains all partially explored nodes
        infinity = 10  # this is a cheat number > all others in comparisons
        explored = {}
        # distance from start to start is obv. 0
        frontier = {}
        # nodes will be added to explored when the minimum distance from loc to node is found
        unvisited = {}
        for t in map:
            unvisited[t] = [[], infinity]  # in the beginning, all found connections regardless of distance are better
            # than nothing, so distance of connection is initially set to 'infinity' to fail
        frontier[location] = unvisited.pop(location)
        frontier[location] = [[location], 0]
        # basic comparison with an actual connection regardless of size of found connection
        # setup complete
        # now use all connections from location node to others to start exploring the unvisited

        loc = location
        while True:
            if len(map[loc][0]) > 0:  # there are nodes adjacent and connected to location
                for t in map[loc][0]:  # iterate through these nodes
                    if t in unvisited:  # select the node if it is unvisited
                        if unvisited[t][1] > frontier[loc][1] + 1:
                            # if its tentative distance is smaller than its assigned distance
                            unvisited[t][1] = frontier[loc][1] + 1  # replace assigned with tentative
                            unvisited[t][0] = frontier[loc][0]    # copy over path to frontier to the new node
                            unvisited[t][0].append(t)           # add the final step of travel to path
                explored[loc] = frontier.pop(loc)

            if target in explored:
                return explored[target][0]
            else:
                minimum = infinity
                for t in unvisited:
                    if unvisited[t][1] < minimum:
                        loc = t
                        minimum = unvisited[t][1]
                frontier[loc] = unvisited.pop(loc)
        return "fuck"  # return something likely to cause an error if for some reason we escape "while true:"
    print(DJK((0, 0), map, (0, 1)))
