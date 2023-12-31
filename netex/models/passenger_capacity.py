from dataclasses import dataclass, field
from typing import Optional
from .passenger_capacity_structure import PassengerCapacityStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PassengerCapacity(PassengerCapacityStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
