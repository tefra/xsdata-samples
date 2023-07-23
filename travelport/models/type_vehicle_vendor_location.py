from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_vehicle_location import TypeVehicleLocation
from travelport.models.type_vehicle_vendor_location_type import TypeVehicleVendorLocationType
from travelport.models.type_vendor_location_1 import TypeVendorLocation1

__NAMESPACE__ = "http://www.travelport.com/schema/vehicle_v52_0"


@dataclass
class TypeVehicleVendorLocation(TypeVendorLocation1):
    """
    Parameters
    ----------
    location_type
        Rental counter location such as Terminal, CityCenterDowntown,
    location_code
        Airport or City Code
    type_value
        Pickup or Return
    """
    class Meta:
        name = "typeVehicleVendorLocation"

    location_type: None | TypeVehicleLocation = field(
        default=None,
        metadata={
            "name": "LocationType",
            "type": "Attribute",
        }
    )
    location_code: None | str = field(
        default=None,
        metadata={
            "name": "LocationCode",
            "type": "Attribute",
            "length": 3,
            "white_space": "collapse",
        }
    )
    type_value: None | TypeVehicleVendorLocationType = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        }
    )
