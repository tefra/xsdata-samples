from __future__ import annotations

from dataclasses import dataclass, field

from .access_equipment_version_structure import AccessEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class QueueingEquipmentVersionStructure(AccessEquipmentVersionStructure):
    class Meta:
        name = "QueueingEquipment_VersionStructure"

    number_of_servers: None | int = field(
        default=None,
        metadata={
            "name": "NumberOfServers",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    railed_queue: None | bool = field(
        default=None,
        metadata={
            "name": "RailedQueue",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    ticketed_queue: None | bool = field(
        default=None,
        metadata={
            "name": "TicketedQueue",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    disabled_priority: None | bool = field(
        default=None,
        metadata={
            "name": "DisabledPriority",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    queuing_seated_possible: None | bool = field(
        default=None,
        metadata={
            "name": "QueuingSeatedPossible",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
