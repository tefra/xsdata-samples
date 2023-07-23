from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_passenger_type_3 import TypePassengerType3

__NAMESPACE__ = "http://www.travelport.com/schema/common_v33_0"


@dataclass
class SearchPassenger3(TypePassengerType3):
    """
    Passenger type with code and optional age information.
    """
    class Meta:
        name = "SearchPassenger"
        namespace = "http://www.travelport.com/schema/common_v33_0"

    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        }
    )
