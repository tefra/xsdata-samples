from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_passenger_type_1 import TypePassengerType1

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


@dataclass
class SearchPassenger1(TypePassengerType1):
    """
    Passenger type with code and optional age information.
    """

    class Meta:
        name = "SearchPassenger"
        namespace = "http://www.travelport.com/schema/common_v52_0"

    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        },
    )
