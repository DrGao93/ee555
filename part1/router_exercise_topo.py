'''
    EE 555 Project - Router Exercise

        PART I

    Name:   Hao Zhang
    Email:  zhan849@usc.edu
    USC ID: 5211-2727-12

    The topology file for part 1.
    To run:
    $ sudo mn --custom router_exercise_topo.py --topo RouterExercise --mac --controller=remote,ip=127.0.0.1

'''
from mininet.topo import Topo

class RouterExercise( Topo ):

    def __init__( self ):
        "Create custom topo."
        # Initialize topology
        Topo.__init__( self )
        self._hosts = [self.addHost( 'h%d' % hid, ip="10.0.%d.100/24" % hid, defaultRoute = "via 10.0.%d.1" % hid )
                for hid in range(1, 4) ]

        self._switch = self.addSwitch('s1')

        self._links = [self.addLink( 'h%d' % hid, 's1')
                for hid in range(1, 4) ]


    @classmethod
    def create(cls): return cls()

topos = { 'RouterExercise': RouterExercise.create }

