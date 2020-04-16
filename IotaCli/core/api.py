from iota.crypto.types import Seed
from iota.crypto.addresses import AddressGenerator
from iota import Iota
from datetime import datetime
import requests, json, zmq

class Node:
    
    def __init__(self, seed=None):
        if seed != None:
            self.seed = seed
        else:
            self.seed = str(Seed.random())

    def __repr__(self):
        return self.seed

    # Connects to IRI 
    def api(self):
        api = Iota(url(), self.seed)
        return api

    @staticmethod
    def url():
        # Grabs available IOTA nodes urls
        r = requests.get('https://api.iota-nodes.net/').json()

        # Filters nodes that are at 100% health and are on the latest version of IRI
        nodes = [r[node]['hostname'] for node in range(len(r))\
            if (r[node]['health'] == 5)\
                and (r[node]['version'] == '1.8.5-RELEASE')\
                    and (r[node]['hasZMQ'] == 1)]

        # Returns first node url in list   
        return nodes[0]

    # Gets 1st index address from designated seed
    def address(self):
        addresses = AddressGenerator(seed=self.seed, checksum=False, security_level=3)
        main_address = addresses.get_addresses(0,1)
        main = str(main_address[0])
        return main

    @staticmethod
    def gen_seed():
        return Seed.random()

# Create a RTC to the Tangle and listen for the ricipient address
class Tangle:

    def __init__(self, connect, address=None):
        config = Node()
        self.node = config.url()
        self.connect_status = connect
        self.rec_address = config.address()

    def connect(self):
        if self.connect_status == False:
            pass
        else:
            recipient = bytes(self.rec_address, 'utf-8')
            context = zmq.Context()
            socket = context.socket(zmq.SUB)
            # Prepares socket to istens to 1st indexed address
            # of seed for tx information
            zmq_node = f'tcp://zmq.{self.node}'
            socket.setsockopt(zmq.SUBSCRIBE, recipient)
            # Initates connections
            socket.connect(zmq_node)
            print(socket)
            connected = True
            while connected:
                address, data = socket.recv().decode().split(' ', 1)
                
                if address:

                    hash_data = dict.fromkeys([
                        tx_hash,
                        address,
                        value,
                        obs_tag,
                        ts,
                        index,
                        last_index,
                        bundle_hash,
                        trunk_hash,
                        branch_hash,
                        received_ts,
                        tag,
                    ])

                    for i, j in data.items():
                        hash_data[i] = j

                    if hash_data:
                        print(hash_data)
                        connected = False
                        return connected
                
test = Tangle(True, None)
test.connect()