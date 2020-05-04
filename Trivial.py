from Network import Network


# Trivial solution
class Trivial:
    def __init__(self, network, source, sink):
        self.network = network
        self.source = source
        self.sink = sink

    def getMaxFlow(self):
        # DFS returns a path of edges
        path = self.DFS(self.source, self.sink)
        # return from the recursive function if the only edge in the path is the source
        if len(path) <= 1:
            return
        # find bottle neck of the path
        # get the minimum of the edges based on the capacity to find the minimum capacity of the path (bottle neck)
        bottleNeck = min(path, key=lambda currEdge: currEdge.currentCapacity).currentCapacity
        self.network.maxFlow += bottleNeck
        # print(path, bottleNeck)
        # add flow for the current edges
        for edge in path:
            self.network.addFlow(edge, bottleNeck)
        self.getMaxFlow()

    def DFS(self, source, sink):
        # make all the vertices false as far as visited
        visited = dict.fromkeys(self.network.vertices.keys(), False)
        path = []
        self.DFSUntil(source, sink, visited, path)
        # return a list of vertices if they were visited
        return path

    def DFSUntil(self, currVertex, sink, visited, path):
        # for each neighbor of the current vertex
        for neighbor in self.network.vertices[currVertex]:
            # if the sink was visited, return
            if visited[sink]:
                return
            # move on to the next vertex if the edge's current capacity is less than or equal to 0 (the edge has no
            # capacity left)
            currEdge = self.network.getEdge(currVertex, neighbor)
            currEdgeCapacity = currEdge.currentCapacity
            if currEdgeCapacity <= 0:
                continue
            # if the neighbor hasn't been visited
            if not visited[neighbor]:
                # mark the current vertex as True because we're visiting it
                visited[currVertex] = True
                # add the current edge to path
                path += [currEdge]
                # if the neighbor is the sink
                if neighbor == sink:
                    # mark sink as visited and return
                    visited[sink] = True
                    return
                # visit the neighbor
                self.DFSUntil(neighbor, sink, visited, path)
