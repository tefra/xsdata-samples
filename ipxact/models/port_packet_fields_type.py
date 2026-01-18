from __future__ import annotations

from dataclasses import dataclass, field

from ipxact.models.port_packet_field_type import PortPacketFieldType

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass(kw_only=True)
class PortPacketFieldsType:
    class Meta:
        name = "portPacketFieldsType"

    packet_field: list[PortPacketFieldType] = field(
        default_factory=list,
        metadata={
            "name": "packetField",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            "min_occurs": 1,
        },
    )
