class PushRelabel:
    def __init__(self, network):
        self.network = network
        self.source = self.network.source
        self.sink = self.network.sink
        # raise an exception if either the source or the sink is not in the network
        if (self.source not in self.network.vertices.keys()) or (self.sink not in self.network.vertices.keys()):
            raise RuntimeError("Requested source or sink do not exist!")

    def preflow(self):
        # set the source height to the number of vertices in the graph
        vertices = self.network.vertices
        # set the height of the source to the number of vertices in the network
        self.source.height = len(vertices)
        for neighbor in vertices[self.source]:
            # set the flows of all the edges adjacent to the source equal to their capacity
            currEdge = self.network.getEdge(self.source, neighbor)
            self.network.addFlow(currEdge, currEdge.capacity, True)
            # set the neighbors' excess flow to the incoming flow (because no flow is going out yet)
            neighbor.excess = currEdge.capacity

    # push excess flow from a vertex
    def push(self, vertex):
        # find the neighbor with the greatest height among the neighbors where a push is possible
        available = [neighbor for neighbor in self.network.vertices[vertex]
                     if self.network.getEdge(vertex, neighbor).forwardFlow !=
                     self.network.getEdge(vertex, neighbor).capacity
                     and vertex.height > neighbor.height]
        if available:
            target = max(available, key=lambda x : x.height)
            targetEdge = self.network.getEdge(vertex, target)
            # the flow to be pushed is the minimum of the excess and the capacity of the edge
            flow = min(vertex.excess, targetEdge.currentCapacity)
            # reduce excess flow
            vertex.excess -= flow
            # add flow for the neighbor
            target.excess += flow
            self.network.addFlow(targetEdge, flow, True)
            # print("Pushed flow {} from vertex {} to vertex {}".format(flow, vertex, neighbor))
            # if there's one neighbor that we can push to, return true
            return True
        else:
            # no push is possible if there's no available vertices to push to
            return False

    def relabel(self, vertex):
        # relabel the vertex if it has excess flow but has smaller height than its neighbor
        # find the minimum of the neighbors height
        # the edge between the vertex and the neighbor also has to have more than 0 current capacity
        neighbors = [neighbor for neighbor in self.network.vertices[vertex] if
                     self.network.getEdge(vertex, neighbor).currentCapacity > 0]
        # if the only place to push flow is the source, then don't go through the entire process to do so
        if len(neighbors) == 1 and neighbors[0] == self.source:
            vertex.excess = 0
            return
        minHeight = min([neighbor.height for neighbor in neighbors])
        # relabel the vertex's height to be one more than the min height
        vertex.height = minHeight + 1

    # get the first found vertex with excess flow
    def excessVertex(self):
        for vertex in self.network.vertices:
            if vertex.excess > 0 and (vertex != self.source and vertex != self.sink):
                return vertex
        # return 0 if no vertex is in excess
        return 0

    def getMaxFlow(self):
        self.preflow()
        # loop until no vertex has excess
        while vertex := self.excessVertex():
            # if the vertex is in excess but we can't push, it means that we need to relabel it
            if not self.push(vertex):
                self.relabel(vertex)
        # the excess flow of the sink at this point will be the max flow
        return self.sink.excess
