from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.distance_units_1 import DistanceUnits1

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


@dataclass
class Distance1:
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
        namespace = "http://www.travelport.com/schema/common_v52_0"

    units: DistanceUnits1 = field(
        default=DistanceUnits1.MI,
        metadata={
            "name": "Units",
            "type": "Attribute",
            "length": 2,
        },
    )
    value: None | int = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Attribute",
            "required": True,
        },
    )
    direction: None | str = field(
        default=None,
        metadata={
            "name": "Direction",
            "type": "Attribute",
            "max_length": 2,
        },
    )
