class PushRelabel:
    def __init__(self, network, source, sink):
        self.network = network
        self.source = self.network.getVertex(source)
        self.sink = self.network.getVertex(sink)
        # raise an exception if either the source or the sink is not in the network
        if (self.source not in self.network.vertices.keys()) or (self.sink not in self.network.vertices.keys()):
            raise RuntimeError("Requested source or sink do not exist!")
        self.network.initializeResidualGraph()
        self.preflow()

    def preflow(self):
        # set the source height to the number of vertices in the graph
        vertices = self.network.vertices
        self.source.height = len(vertices)
        # set all the heights to 0 except for the source
        for vertex, neighbors in vertices.items():
            if vertex == self.source:
                # set the flow of the edge adjacent to source equal to the capacity
                for neighbor in neighbors:
                    currEdge = self.network.getEdge(vertex, neighbor)
                    self.network.addFlow(currEdge, currEdge.capacity, True)
            else:
                vertex.height = 0
