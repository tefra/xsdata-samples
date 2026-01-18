from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.distance_units_3 import DistanceUnits3

__NAMESPACE__ = "http://www.travelport.com/schema/common_v33_0"


@dataclass(kw_only=True)
class Distance3:
    """
    Container to encapsulate the a distance value with its unit of measure.

    Parameters
    ----------
    units
    value
    direction
        Directions: S, N, E, W, SE, NW, ...
    """

    class Meta:
        name = "Distance"
        namespace = "http://www.travelport.com/schema/common_v33_0"

    units: DistanceUnits3 = field(
        default=DistanceUnits3.MI,
        metadata={
            "name": "Units",
            "type": "Attribute",
            "length": 2,
        },
    )
    value: int = field(
        metadata={
            "name": "Value",
            "type": "Attribute",
            "required": True,
        }
    )
    direction: None | str = field(
        default=None,
        metadata={
            "name": "Direction",
            "type": "Attribute",
            "max_length": 2,
        },
    )
