#TODO every function has a place - nav.py, paradigms, or a controller. Rename this to something that fits the fact that
#literally the only thing in here is DJK, maybe "pathfinders" for when we never make a differeny pathfinder from DJK
class bag:
    map =  \
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
                    [(0, 1), (0, 3)],
                    [],
                    [(1, 2), (-1, 2)]
                ],
                (0, 3): [
                    [(0, 2)], [(0, 4)], []
                ],
                (1, 0): [
                    [(0, 0)], [], []
                ],
                (0, 4): [
                    [[], [(0, 3)], []]
                ]
            }
    """
    Dijkstra's algorithm acts over a connected graph: assume a path between location node and target node exists
    path will be represented as a series of nodes in an ordered list: each node is connected to the next in the list
    via an edge. The algorithm finds the shortest list of said nodes that accurately lead to the target node.
    """
    @staticmethod
    def djk(location, map, target):  # full implementation of Dijkstra's algorithm over a dictionary object map
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
        # TODO make this code more readable, maybe change some names, add more comments
        # TODO eventually make djk work if graph is not connected
        # this is a test map for display purposes only

        infinity = 10e3000000   # this is a number which is too big for python to handle: becomes 1.#INF
        # and is therefore considered > all other comparable numbers and basically infinity
        # nodes will be added to explored when the shortest path from location to node is found. It's a list of solved nodes
        # and djk will stop when the target node is in explored
        explored = {}
        # frontier will contain a node in which connections are followed through: all nodes in explored go through
        # frontier, one at a time.
        frontier = {}
        # All nodes but the source 'location' node start in unvisited: these are nodes we don't yet have an optimal path
        # for yet. But we will. I promise
        unvisited = {}
        for t in map:
            unvisited[t] = [[], infinity]  # in the beginning, all found connections regardless of distance are better
            # than nothing, so distance of connection is initially set to 'infinity' to be overriden by any possible
            # path regardless of length
        frontier[location] = unvisited.pop(location)
        # distance from start to start is obv. 0, and we know the path from location to location (location)
        frontier[location] = [[location], 0]
        # basic comparison with an actual connection regardless of size of found connection
        # setup complete
        # now use all connections from location node to others to start exploring the unvisited

        loc = location  # this looks confusing, but it isn't. loc is the node of interest (always in frontier), location
        # is the source node.
        while True:  # This means we will visit all unvisitables or loop forever
            if len(map[loc][0]) > 0:  # if there are nodes adjacent and connected to location
                for n in map[loc][0]:  # iterate through these nodes
                    if n in unvisited:  # select the node if it is unvisited
                        if unvisited[n][1] > frontier[loc][1] + 1:
                            # if its tentative distance is smaller than its assigned distance
                            unvisited[n][1] = frontier[loc][1] + 1  # replace assigned with tentative
                            unvisited[n][0] = []
                            for i in frontier[loc][0]:
                                unvisited[n][0].append(i)    # copy over path to frontier to the new node
                            unvisited[n][0].append(n)           # add the final step of travel to path
                explored[loc] = frontier.pop(loc)
                # print(explored[location])
            if target in explored:
                return explored[target]  # when target is reached, end DJk
            else:
                minimum = infinity
                for m in unvisited:
                    if unvisited[m][1] < minimum:
                        loc = m
                        minimum = unvisited[m][1]
                if minimum == infinity and len(unvisited) > 0:  # if its still infinity after finding
                    #  true minimum value in unvisited
                    print("Ben is an unfun dog")  # woof #thisIsForYouBen #noFilter #camelCase
                    return []   # this will occur if all of unvisited is unfindable
                # hopefully this means that we have explored everything we can,
                # and we can return no path for target because if there was one,
                # we'd have found it
                frontier[loc] = unvisited.pop(loc)
    print djk((0, 0), map, (0, 3))  # holy moly it worked first* try
    # *was at least second