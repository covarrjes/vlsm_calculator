# subnet class
# Goals:
class Subnet:

    def __init__(self, count, network):
        self.host_count = count
        self.network = network
        self.first_host = network[3] + 1
        self.last_host = network[3] + count - 1
        self.broadcast = network[3] + count

    def get_count(self):
        return self.host_count

    def get_network_address(self):
        return self.network

    def get_first_host(self):
        return self.first_host

    def get_last_host(self):
        return self.last_host

    def get_broadcast(self):
        return self.broadcast

