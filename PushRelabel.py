class PushRelabel:
    def __init__(self, network, source, sink):
        self.network = network
        self.source = source
        self.sink = sink
        # raise an exception if either the source or the sink is not in the network
        if (self.source not in self.network.vertices.keys()) or (self.sink not in self.network.vertices.keys()):
            raise RuntimeError("Requested source or sink do not exist!")
