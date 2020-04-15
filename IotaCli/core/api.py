from iota.crypto.types import Seed
from iota.crypto.addresses import AddressGenerator
from iota import Iota
from datetime import datetime
import requests, json

class Node(object):
    def __init__(self, seed=None):
        self.seed = str(Seed.random()) 
        if seed != None:
            self.seed = seed

    def __repr__(self):
        return self.seed

    def api(self):
        # Grabs available IOTA nodes
        r = requests.get('https://nodes.iota.works/api').json()

        # Filters nodes that are at 100% health and are on the latest version of IRI
        nodes = [r[node]['node'] for node in range(len(r)) if (r[node]['health'] == 10) and (r[node]['version'] == '1.8.5-RELEASE')]

        #Establishes connection    
        apis= Iota(nodes[0], self.seed)
        return apis.get_node_info()

    def address(self):
        addresses = AddressGenerator(seed=self.seed, checksum=False, security_level=3)
        main_address = addresses.get_addresses(0,1)
        return main_address[0]

    def 

    @staticmethod
    def gen_seed():
        return str(Seed.random())
