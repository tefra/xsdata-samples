from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDateTime

from travelport.models.type_vehicle_location import TypeVehicleLocation

__NAMESPACE__ = "http://www.travelport.com/schema/vehicle_v52_0"


@dataclass(kw_only=True)
class VehiclePickupDateLocation:
    """
    Used to update PickupDateTime and location of an existing Vehicle
    Booking. 1g/1v only supports modification of PickupDateTime.

    PickupDateTime cannot be deleted.

    Parameters
    ----------
    pickup_date_time
        Providers: 1g/1v/1p
    pickup_location
        Providers: 1p
    pickup_location_type
        Providers: 1p
    pickup_location_number
        Providers: 1p
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/vehicle_v52_0"

    pickup_date_time: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "PickupDateTime",
            "type": "Attribute",
        },
    )
    pickup_location: None | str = field(
        default=None,
        metadata={
            "name": "PickupLocation",
            "type": "Attribute",
            "length": 3,
            "white_space": "collapse",
        },
    )
    pickup_location_type: None | TypeVehicleLocation = field(
        default=None,
        metadata={
            "name": "PickupLocationType",
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
