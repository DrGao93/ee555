"""Custom topology example

    EE 555 Project - Router Exercise

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo

class RouterExercise( Topo ):

    def __init__( self ):
        "Create custom topo."
        # Initialize topology
        Topo.__init__( self )
#        self._hosts = [self.addHost( 'h%d' % hid, ip='10.0.%d.100/24' % hid ) for hid in range(1,4)]
        self._hosts = [self.addHost( 'h%d' % hid, ip="10.0.%d.100/24" % hid, defaultRoute = "via 10.0.%d.1" % hid )
                for hid in range(1, 4) ]
#        host1 = self.addHost( 'h1', ip="10.0.1.100/24", defaultRoute = "via 10.0.1.1" )
#        host2 = self.addHost( 'h2', ip="10.0.2.100/24", defaultRoute = "via 10.0.2.1" )
#        host3 = self.addHost( 'h3', ip="10.0.3.100/24", defaultRoute = "via 10.0.3.1" )

        self._switch = self.addSwitch('s1')
        self._links = [self.addLink( 'h%d' % hid, 's1')
                for hid in range(1, 4) ]


    @classmethod
    def create(cls): return cls()

topos = { 'RouterExercise': RouterExercise.create }

