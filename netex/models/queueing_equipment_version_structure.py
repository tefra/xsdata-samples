from dataclasses import dataclass, field
from typing import Optional
from netex.models.access_equipment_version_structure import AccessEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class QueueingEquipmentVersionStructure(AccessEquipmentVersionStructure):
    class Meta:
        name = "QueueingEquipment_VersionStructure"

    number_of_servers: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfServers",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    railed_queue: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RailedQueue",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    ticketed_queue: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TicketedQueue",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    disabled_priority: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DisabledPriority",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    queuing_seated_possible: Optional[bool] = field(
        default=None,
        metadata={
            "name": "QueuingSeatedPossible",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
