from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_distance import TypeDistance

__NAMESPACE__ = "http://www.travelport.com/schema/vehicle_v52_0"


@dataclass
class TypeVehicleSearchDistance:
    """
    Parameters
    ----------
    units
        MI or KM. Defaults to miles
    direction
        Valid values: N, S, E, W, NE, NW, SE, SW.  Default:  direction will
        not be specified.
    min_distance
        Minimum distance.  Defaults to 0.
    max_distance
        Maximum distance
    """

    class Meta:
        name = "typeVehicleSearchDistance"

    units: None | TypeDistance = field(
        default=None,
        metadata={
            "name": "Units",
            "type": "Attribute",
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
    min_distance: None | int = field(
        default=None,
        metadata={
            "name": "MinDistance",
            "type": "Attribute",
            "min_inclusive": 0,
            "max_inclusive": 999,
        },
    )
    max_distance: None | int = field(
        default=None,
        metadata={
            "name": "MaxDistance",
            "type": "Attribute",
            "required": True,
            "max_inclusive": 999,
        },
    )
