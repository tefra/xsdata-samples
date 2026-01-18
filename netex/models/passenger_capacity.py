from __future__ import annotations

from dataclasses import dataclass, field

from .passenger_capacity_structure import PassengerCapacityStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PassengerCapacity(PassengerCapacityStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
