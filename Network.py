class Edge:

    def __init__(self, start, end, capacity=0):
        # an edge has a starting vertex
        self.startVertex = start
        # an ending vertex
        self.endVertex = end
        # the capacity of the edge
        self.capacity = capacity
        # the current forward flow value
        self.forwardFlow = 0
        # capacity - forward flow indicates how much capacity the edge currently has
        self.currentCapacity = self.capacity - self.forwardFlow

    # overloading equality operator
    def __eq__(self, other):
        return self.startVertex == other.startVertex and self.endVertex == other.endVertex

    def __repr__(self):
        return '{} {} {}'.format(self.startVertex, self.endVertex, self.currentCapacity)

    # get the backward edge of this edge
    def getResidual(self):
        return Edge(self.endVertex, self.startVertex)

    def addFlow(self, value):
        self.forwardFlow += value
        self.currentCapacity = self.capacity - self.forwardFlow

class Network:
    def __init__(self):
        # dictionary of vertices and their adjacent vertices
        self.vertices = {}
        # list of edges
        self.edges = []
        self.maxFlow = 0

    # add a vertex and set its neighbors to an empty list
    def addVertex(self, v):
        if v not in self.vertices:
            self.vertices.setdefault(v, list())

    # add an edge
    def addEdge(self, start, end, capacity):
        edge = Edge(start, end, capacity)
        self.edges.append(edge)
        # append end to start's neighbor
        self.vertices[start].append(end)

    # load graph from an input file
    def loadGraph(self, file):
        for row in open(file, 'r'):
            start, end, capacity = map(int, row.split())
            self.addVertex(start)
            self.addVertex(end)
            self.addEdge(start, end, capacity)

    # get all the vertices
    def getVertices(self):
        return self.vertices.keys()

    # get all the edges
    def getEdges(self):
        return [edge for edge in self.edges]

    # get one edge
    def getEdge(self, start, end):
        targetEdge = Edge(start, end)
        for edge in self.edges:
            if targetEdge == edge:
                return edge
        raise RuntimeError("Requested edge {} does not exist!".format(targetEdge))

    # get flow across network
    def getFlow(self):
        return sum(edge.forwardFlow for edge in self.edges)

    def addFlow(self, targetEdge, value):
        forwardEdge = self.getEdge(targetEdge.startVertex, targetEdge.endVertex)
        backwardEdge = self.getEdge(targetEdge.endVertex, targetEdge.startVertex)
        forwardEdge.addFlow(value)
        backwardEdge.addFlow(-value)