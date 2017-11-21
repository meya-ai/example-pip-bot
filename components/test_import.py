import requests
from meya import Component
import scapy


class TestImport(Component):
    def start(self):
        print dir(scapy)
        return self.respond()
