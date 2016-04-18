'''
    EE 555 Project - Router Exercise

        PART II

    Name:   Hao Zhang
    Email:  zhan849@usc.edu
    USC ID: 5211-2727-12

    The topology file for part 2.
    To run:
    $ sudo mn --custom ee555P2.py --topo ee555P2 --mac --controller=remote,ip=127.0.0.1

'''

from mininet.topo import Topo

class ee555P2( Topo ):

    def __init__( self ):
        "Create custom topo."
        # Initialize topology
        Topo.__init__( self )

        self._hosts = []
        self._switches = []
        self._links = []

        self._hosts.append( self.addHost('h1', ip='10.0.1.2/24', defaultRoute = 'via 10.0.1.1') )
        self._hosts.append( self.addHost('h2', ip='10.0.1.3/24', defaultRoute = 'via 10.0.1.1') )
        self._hosts.append( self.addHost('h3', ip='10.0.2.2/24', defaultRoute = 'via 10.0.2.1') )
        self._hosts.append( self.addHost('h4', ip='10.0.2.3/24', defaultRoute = 'via 10.0.2.1') )
        self._hosts.append( self.addHost('h5', ip='10.0.2.4/24', defaultRoute = 'via 10.0.2.1') )

        self._switches.append( self.addSwitch('s1') )
        self._switches.append( self.addSwitch('s2') )

        self._links.append( self.addLink( 's1', 's2', port1=1, port2=1 ) )
        self._links.append( self.addLink( 'h1', 's1', port1=1, port2=2 ) )
        self._links.append( self.addLink( 'h2', 's1', port1=1, port2=3 ) )
        self._links.append( self.addLink( 'h3', 's2', port1=1, port2=2 ) )
        self._links.append( self.addLink( 'h4', 's2', port1=1, port2=3 ) )
        self._links.append( self.addLink( 'h5', 's2', port1=1, port2=4 ) )

    @classmethod
    def create(cls): return cls()

topos = { 'ee555P2': ee555P2.create }

