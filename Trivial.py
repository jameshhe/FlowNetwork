from Network import Network


# Trivial solution
class Trivial:
    def __init__(self, network, source, sink):
        self.network = network
        self.source = source
        self.sink = sink

    def trivialSolution(self):
        # while a path from s-t exists
        path = self.DFS(self.source, self.sink)
        # return from the recursive function if the only edge in the path is the source
        if len(path) <= 1:
            return
        # find bottle neck of the path
        # first find all the edges in the path
        pathEdges = [self.network.getEdge(path[i], path[i + 1]) for i in range(len(path) - 1)]
        # sort the edges based on the capacity to find the minimum capacity of the path (bottle neck)
        bottleNeck = sorted(pathEdges, key=lambda currEdge: currEdge.currentCapacity)[0].currentCapacity
        self.network.maxFlow += bottleNeck
        # add flow for the current edges
        for edge in pathEdges:
            self.network.addFlow(edge, bottleNeck)
        self.trivialSolution()

    def DFS(self, source, sink):
        # make all the vertices false as far as visited
        visited = dict.fromkeys(self.network.vertices.keys(), False)
        self.DFSUntil(source, sink, visited)
        # return a list of vertices if they were visited
        return [vertex for vertex in visited.keys() if visited[vertex]]

    def DFSUntil(self, currVertex, sink, visited):
        # for each neighbor of the current vertex
        for neighbor in self.network.vertices[currVertex]:
            # if the sink was visited, return
            if visited[sink]:
                return
            # move on to the next vertex if the edge's current capacity is less than or equal to 0 (the edge has no
            # capacity left)
            if self.network.getEdge(currVertex, neighbor).currentCapacity <= 0:
                continue
            # if the neighbor hasn't been visited
            if not visited[neighbor]:
                # mark the current vertex as True because we're visiting it
                visited[currVertex] = True
                # if the neighbor is the sink
                if neighbor == sink:
                    # mark sink as visited and return
                    visited[sink] = True
                    return
                # visit the neighbor
                self.DFSUntil(neighbor, sink, visited)
