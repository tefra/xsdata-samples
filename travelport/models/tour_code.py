from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class TourCode:
    """
    Tour Code Fare Basis.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    value: None | str = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Attribute",
            "required": True,
            "max_length": 15,
        },
    )
