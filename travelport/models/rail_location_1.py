from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.location_1 import Location1

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


@dataclass(kw_only=True)
class RailLocation1(Location1):
    """
    RCH specific location code (a.k.a UCodes) which uniquely identifies a
    train station.
    """

    class Meta:
        name = "RailLocation"
        namespace = "http://www.travelport.com/schema/common_v52_0"

    code: str = field(
        metadata={
            "name": "Code",
            "type": "Attribute",
            "required": True,
            "min_length": 3,
            "max_length": 8,
            "white_space": "collapse",
        }
    )
