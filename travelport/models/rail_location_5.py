from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.location_5 import Location5

__NAMESPACE__ = "http://www.travelport.com/schema/common_v34_0"


@dataclass(kw_only=True)
class RailLocation5(Location5):
    """
    RCH specific location code (a.k.a UCodes) which uniquely identifies a
    train station.
    """

    class Meta:
        name = "RailLocation"
        namespace = "http://www.travelport.com/schema/common_v34_0"

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
