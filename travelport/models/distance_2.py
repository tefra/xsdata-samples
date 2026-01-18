from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.distance_units_2 import DistanceUnits2

__NAMESPACE__ = "http://www.travelport.com/schema/common_v32_0"


@dataclass(kw_only=True)
class Distance2:
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
        namespace = "http://www.travelport.com/schema/common_v32_0"

    units: DistanceUnits2 = field(
        default=DistanceUnits2.MI,
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
