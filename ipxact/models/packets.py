from dataclasses import dataclass

from ipxact.models.port_packets_type import PortPacketsType

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class Packets(PortPacketsType):
    class Meta:
        name = "packets"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"
