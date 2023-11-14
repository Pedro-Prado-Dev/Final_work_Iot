from mininet.topo import Topo
from mininet.util import irange, natural, naturalSeq
from resource import getrlimit, setrlimit, RLIMIT_NPROC, RLIMIT_NOFILE


class MyTopo( Topo ):
    "3 host 2 switch 2 host custom topology"

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')
        h5 = self.addHost('h5')
        h6 = self.addHost('h6')
        h7 = self.addHost('h7') 
        h8 = self.addHost('h8')
        h9 = self.addHost('h9')
        
        s1 = self.addSwitch( 's1' )
        s2 = self.addSwitch( 's2' )
        s3 = self.addSwitch( 's3' )
        s4 = self.addSwitch( 's4' )
        

        # Add links
        self.addLink( h1, s1 )
        self.addLink( h2, s1 )
        self.addLink( h3, s2 )
        self.addLink( h4, s2 )
        self.addLink( h5, s3 )
        self.addLink( h6, s3 )
        self.addLink( h7, s4 )
        self.addLink( h8, s4 )
        self.addLink( h9, s4 )
        self.addLink( s1, s2 )
        self.addLink( s2, s3 )
        self.addLink( s3, s4 )
        
topos = { 'mytopo': ( lambda: MyTopo() ) }
