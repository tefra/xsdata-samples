from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_vehicle_location import TypeVehicleLocation

__NAMESPACE__ = "http://www.travelport.com/schema/vehicle_v52_0"


@dataclass(kw_only=True)
class VehicleReturnDateLocation:
    """
    Used to update Return Location and Return Date of existing Vehicle
    Booking.

    Modify operation : Only modification of ReturnDateTime is supported.
    Deletion of ReturnDateTime is not supported. If values passed in
    ReturnLocation, ReturnLocationType and ReturnLocationNumber are exactly
    same as PickupLocation, PickupLocationType and PickupLocationNumber of
    existing booking then ReturnLocation, ReturnLocationType and
    ReturnLocationNumber will be deleted. If values passed in
    ReturnLocation, ReturnLocationType and ReturnLocationNumber are not
    same as PickupLocation, PickupLocationType and PickupLocationNumber of
    existing booking then ReturnLocation, ReturnLocationType and
    ReturnLocationNumber will be updated.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/vehicle_v52_0"

    return_date_time: None | str = field(
        default=None,
        metadata={
            "name": "ReturnDateTime",
            "type": "Attribute",
        },
    )
    return_location: None | str = field(
        default=None,
        metadata={
            "name": "ReturnLocation",
            "type": "Attribute",
            "length": 3,
            "white_space": "collapse",
        },
    )
    return_location_type: None | TypeVehicleLocation = field(
        default=None,
        metadata={
            "name": "ReturnLocationType",
            "type": "Attribute",
        },
    )
    return_location_number: None | str = field(
        default=None,
        metadata={
            "name": "ReturnLocationNumber",
            "type": "Attribute",
        },
    )
