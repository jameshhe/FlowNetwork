from Network import Network
from Trivial import Trivial
from EdmondsCarp import EdmondsCarp
from PushRelabel import PushRelabel

if __name__ == '__main__':
    network = Network('Example4.txt', 0, 5)
    # Trivial
    trivial = Trivial(network)
    print("Max Flow:", trivial.getMaxFlow())
    network.reset()
    print('------------------------------------')
    network.initializeResidualGraph()
    # Edmonds-Carp
    ec = EdmondsCarp(network)
    print("Max Flow:", ec.getMaxFlow())
    network.reset()
    print('------------------------------------')
    # push relabel
    prl = PushRelabel(network)
    print("Max Flow:", prl.getMaxFlow())






