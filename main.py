from Network import Network
from Trivial import Trivial
from EdmondsCarp import EdmondsCarp
from PushRelabel import PushRelabel

if __name__ == '__main__':
    network = Network('Example2.txt', 0, 5)

    # Trivial
    trivial = Trivial(network)
    print("Trivial Solution Max Flow:", trivial.getMaxFlow())
    network.reset()
    print('------------------------------------')

    network.initializeResidualGraph()

    # Edmonds-Carp
    ec = EdmondsCarp(network)
    print("Edmonds-Carp Max Flow:", ec.getMaxFlow())
    network.reset()
    print('------------------------------------')

    # push relabel
    prl = PushRelabel(network)
    print("Push-Relabel Max Flow:", prl.getMaxFlow())







