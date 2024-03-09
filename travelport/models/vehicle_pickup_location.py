from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.vehicle_modifier import VehicleModifier
from travelport.models.vendor import Vendor

__NAMESPACE__ = "http://www.travelport.com/schema/vehicle_v52_0"


@dataclass
class VehiclePickupLocation:
    """
    A container for Vehicle Location ,Vendor and Vehicle Modifier.

    Parameters
    ----------
    vendor
    vehicle_modifier
    pick_up_location
        The location (city or airport code) at which the vehicle will be
        picked up.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/vehicle_v52_0"

    vendor: None | Vendor = field(
        default=None,
        metadata={
            "name": "Vendor",
            "type": "Element",
            "required": True,
        },
    )
    vehicle_modifier: list[VehicleModifier] = field(
        default_factory=list,
        metadata={
            "name": "VehicleModifier",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    pick_up_location: None | str = field(
        default=None,
        metadata={
            "name": "PickUpLocation",
            "type": "Attribute",
            "required": True,
            "length": 3,
            "white_space": "collapse",
        },
    )
