from Network import Network
from Trivial import Trivial

if __name__ == '__main__':
    network = Network()
    network.loadGraph('ExampleGraph.txt')
    trivial = Trivial(network, 0, 4)
    trivial.trivialSolution()
    print(network.maxFlow)

