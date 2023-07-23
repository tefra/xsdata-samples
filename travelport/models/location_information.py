from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_area_info import TypeAreaInfo
from travelport.models.type_structured_address_1 import TypeStructuredAddress1
from travelport.models.type_vehicle_location import TypeVehicleLocation

__NAMESPACE__ = "http://www.travelport.com/schema/vehicle_v52_0"


@dataclass
class LocationInformation:
    """
    The type of location and the location address.

    Parameters
    ----------
    address
        The address of the rental location.
    location_type
        Specifies the type of location, such as city center, airport, or
        near resort.
    area_group
        Unique area group code. like A, B etc.
    location
        Location corresponding to the group.
    area_type
        Location type corresponding to the group.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/vehicle_v52_0"

    address: None | TypeStructuredAddress1 = field(
        default=None,
        metadata={
            "name": "Address",
            "type": "Element",
        }
    )
    location_type: None | TypeVehicleLocation = field(
        default=None,
        metadata={
            "name": "LocationType",
            "type": "Attribute",
        }
    )
    area_group: None | str = field(
        default=None,
        metadata={
            "name": "AreaGroup",
            "type": "Attribute",
        }
    )
    location: None | str = field(
        default=None,
        metadata={
            "name": "Location",
            "type": "Attribute",
            "length": 3,
            "white_space": "collapse",
        }
    )
    area_type: None | TypeAreaInfo = field(
        default=None,
        metadata={
            "name": "AreaType",
            "type": "Attribute",
        }
    )
