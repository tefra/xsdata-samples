from dataclasses import dataclass, field
from typing import Optional

from .access_equipment_version_structure import AccessEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class QueueingEquipmentVersionStructure(AccessEquipmentVersionStructure):
    class Meta:
        name = "QueueingEquipment_VersionStructure"

    number_of_servers: int | None = field(
        default=None,
        metadata={
            "name": "NumberOfServers",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    railed_queue: bool | None = field(
        default=None,
        metadata={
            "name": "RailedQueue",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    ticketed_queue: bool | None = field(
        default=None,
        metadata={
            "name": "TicketedQueue",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    disabled_priority: bool | None = field(
        default=None,
        metadata={
            "name": "DisabledPriority",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    queuing_seated_possible: bool | None = field(
        default=None,
        metadata={
            "name": "QueuingSeatedPossible",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
