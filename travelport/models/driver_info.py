from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/vehicle_v52_0"


@dataclass
class DriverInfo:
    """
    Parameters
    ----------
    age
        This is used to specify Primary Driver’s age in years. 1P only.
        Required.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/vehicle_v52_0"

    age: None | int = field(
        default=None,
        metadata={
            "name": "Age",
            "type": "Attribute",
            "min_inclusive": 0,
            "max_inclusive": 99,
        }
    )
