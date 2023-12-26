from __future__ import annotations
from dataclasses import dataclass, field
from xsdata.models.datatype import XmlDate
from travelport.models.type_vehicle_location import TypeVehicleLocation

__NAMESPACE__ = "http://www.travelport.com/schema/vehicle_v52_0"


@dataclass
class TypePickupDateLocation:
    """
    A complexType for the pickup date, location, and location type.

    Parameters
    ----------
    date
        The start date for the vehicle rental.
    location
        The location (airport code) at which the vehicle will be picked up.
    location_type
        The type of location requested, such as resort, city center.
    pickup_location_number
        Unique identifier for vehicle location
    """

    class Meta:
        name = "typePickupDateLocation"

    date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "Date",
            "type": "Attribute",
            "required": True,
        },
    )
    location: None | str = field(
        default=None,
        metadata={
            "name": "Location",
            "type": "Attribute",
            "length": 3,
            "white_space": "collapse",
        },
    )
    location_type: None | TypeVehicleLocation = field(
        default=None,
        metadata={
            "name": "LocationType",
            "type": "Attribute",
        },
    )
    pickup_location_number: None | str = field(
        default=None,
        metadata={
            "name": "PickupLocationNumber",
            "type": "Attribute",
        },
    )
