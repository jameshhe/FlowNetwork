from Network import Network
from Trivial import Trivial
from EdmondsCarp import EdmondsCarp

if __name__ == '__main__':
    network = Network()
    network.loadGraph('Example4.txt')
    # trivial = Trivial(network, 0, 5)
    # trivial.getMaxFlow()

    ec = EdmondsCarp(network, 0, 5)
    ec.getMaxFlow()
    print(network.maxFlow)


