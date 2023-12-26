from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.air_seat_assignment_1 import AirSeatAssignment1
from travelport.models.type_passenger_type_1 import TypePassengerType1

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class SearchTraveler(TypePassengerType1):
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    air_seat_assignment: list[AirSeatAssignment1] = field(
        default_factory=list,
        metadata={
            "name": "AirSeatAssignment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        },
    )
