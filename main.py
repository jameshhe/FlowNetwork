from Network import Network
from Trivial import Trivial
from EdmondsCarp import EdmondsCarp
from PushRelabel import PushRelabel

if __name__ == '__main__':
    network = Network()
    network.loadGraph('Example4.txt')
    trivial = Trivial(network, 0, 5)
    print(trivial.getMaxFlow())
    network.reset()
    print('------------------------------------')
    ec = EdmondsCarp(network, 0, 5)
    print(ec.getMaxFlow())
    network.reset()
    print('------------------------------------')
    # prl = PushRelabel(network, 0, 5)






