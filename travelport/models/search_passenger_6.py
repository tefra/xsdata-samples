from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_passenger_type_6 import TypePassengerType6

__NAMESPACE__ = "http://www.travelport.com/schema/common_v38_0"


@dataclass
class SearchPassenger6(TypePassengerType6):
    """
    Passenger type with code and optional age information.
    """

    class Meta:
        name = "SearchPassenger"
        namespace = "http://www.travelport.com/schema/common_v38_0"

    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        },
    )
