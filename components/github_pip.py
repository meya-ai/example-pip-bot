from meya import Component
from utilities import foo, multiply


class GitHubPip(Component):
    def start(self):
        print foo()
        print multiply(10, 20)
        return self.respond()
