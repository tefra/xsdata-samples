from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/vehicle_v52_0"


@dataclass
class TypeVehicleRateDescription:
    """
    Parameters
    ----------
    text
    name
        Optional context name of the text block being returned i.e. Room
        details
    """

    class Meta:
        name = "typeVehicleRateDescription"

    text: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Text",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/vehicle_v52_0",
            "min_occurs": 1,
            "max_occurs": 999,
        },
    )
    name: None | str = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
        },
    )
