class Vertex:
    def __init__(self, value, height=0, excess=0):
        self.value = value
        self.height = height
        self.excess = excess

    def __hash__(self):
        return hash(self.value)

    def __eq__(self, other):
        return self.value == other.value

    def __repr__(self):
        return '{}'.format(self.value)

    def reset(self):
        self.height = 0
        self.excess = 0


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
        return '{} {}'.format(self.startVertex, self.endVertex)

    # get the backward edge of this edge
    def getResidual(self):
        return Edge(self.endVertex, self.startVertex)

    def addFlow(self, value):
        self.forwardFlow += value
        self.currentCapacity = self.capacity - self.forwardFlow

    def reset(self):
        self.forwardFlow = 0
        self.currentCapacity = self.capacity - self.forwardFlow


class Network:
    def __init__(self, file, source, sink):
        # dictionary of vertices and their adjacent vertices
        self.vertices = {}
        # list of edges
        self.edges = []
        self.loadGraph(file)
        self.source = self.getVertex(source)
        self.sink = self.getVertex(sink)

    # add a vertex and set its neighbors to an empty list
    def addVertex(self, v):
        if v not in self.vertices:
            self.vertices.setdefault(v, list())

    # add an edge
    def addEdge(self, start, end, capacity):
        start = self.getVertex(start)
        end = self.getVertex(end)
        edge = Edge(start, end, capacity)
        self.edges.append(edge)
        # append end to start's neighbor
        self.vertices[start].append(end)

    # load graph from an input file
    def loadGraph(self, file):
        for row in open(file, 'r'):
            start, end, capacity = map(int, row.split())
            self.addVertex(Vertex(start))
            self.addVertex(Vertex(end))
            self.addEdge(start, end, capacity)

    # get all the vertices
    def getVertices(self):
        return self.vertices.keys()

    # get all the edges
    def getEdges(self):
        return [edge for edge in self.edges]

    # get one vertex
    def getVertex(self, vertexVal):
        for vertex in self.vertices:
            if vertexVal == vertex.value:
                return vertex
        raise RuntimeError("Requested vertex {} does not exist!".format(vertexVal))

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

    def addFlow(self, targetEdge, value, residual=False):
        forwardEdge = self.getEdge(targetEdge.startVertex, targetEdge.endVertex)
        forwardEdge.addFlow(value)
        # if residual is enabled, get the backward edges as well
        if residual:
            backwardEdge = self.getEdge(targetEdge.endVertex, targetEdge.startVertex)
            backwardEdge.addFlow(-value)

    # add all the residual edges to the network
    def initializeResidualGraph(self):
        residuals = [edge.getResidual() for edge in self.edges]
        self.edges += residuals
        # add the newly connected edges to the vertices dictionary
        for edge in residuals:
            self.vertices[edge.startVertex] += [edge.endVertex]

    # reset after each use
    def reset(self):
        # reset all the edges
        for edge in self.edges:
            edge.reset()
        for vertex, neighbors in self.vertices.items():
            vertex.reset()
            for neighbor in neighbors:
                neighbor.reset()
