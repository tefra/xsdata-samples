from dataclasses import dataclass, field

from ipxact.models.port_packet_type import PortPacketType

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class PortPacketsType:
    class Meta:
        name = "portPacketsType"

    packet: list[PortPacketType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            "min_occurs": 1,
        },
    )