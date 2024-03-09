from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_vehicle_disclaimer import TypeVehicleDisclaimer

__NAMESPACE__ = "http://www.travelport.com/schema/vehicle_v52_0"


@dataclass
class VehicleDisclaimer:
    """
    Textual information related to this rental location.

    Parameters
    ----------
    value
    type_value
        The disclaimer category
    sub_type
        Extra information about this category of disclaimer
    description
        A verbal description of this disclaimer
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/vehicle_v52_0"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    type_value: None | TypeVehicleDisclaimer = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        },
    )
    sub_type: None | str = field(
        default=None,
        metadata={
            "name": "SubType",
            "type": "Attribute",
        },
    )
    description: None | str = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Attribute",
        },
    )
