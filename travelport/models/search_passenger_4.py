from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_passenger_type_4 import TypePassengerType4

__NAMESPACE__ = "http://www.travelport.com/schema/common_v37_0"


@dataclass
class SearchPassenger4(TypePassengerType4):
    """
    Passenger type with code and optional age information.
    """

    class Meta:
        name = "SearchPassenger"
        namespace = "http://www.travelport.com/schema/common_v37_0"

    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        },
    )
