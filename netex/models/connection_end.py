from dataclasses import dataclass

from .connection_end_structure import ConnectionEndStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ConnectionEnd(ConnectionEndStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
