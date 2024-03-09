from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/vehicle_v52_0"


@dataclass
class Equipment:
    """
    Requested Special Equipment Information.

    Parameters
    ----------
    type_value
        The Type of Special Equipment requested
    description
        Special Equipment description
    quantity
        Special Equipment quantity
    status
        Status of the request returned by the supplier. Valid Values KK
        (Confirmed), UC (Unable to Confirm and NN (On request)
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/vehicle_v52_0"

    type_value: None | str = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        },
    )
    description: None | str = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Attribute",
            "required": True,
        },
    )
    quantity: None | int = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Attribute",
        },
    )
    status: None | str = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Attribute",
            "length": 2,
            "white_space": "collapse",
        },
    )
