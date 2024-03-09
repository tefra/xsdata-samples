from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.location_4 import Location4

__NAMESPACE__ = "http://www.travelport.com/schema/common_v37_0"


@dataclass
class RailLocation4(Location4):
    """
    RCH specific location code (a.k.a UCodes) which uniquely identifies a train
    station.
    """

    class Meta:
        name = "RailLocation"
        namespace = "http://www.travelport.com/schema/common_v37_0"

    code: None | str = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
            "required": True,
            "min_length": 3,
            "max_length": 8,
            "white_space": "collapse",
        },
    )
