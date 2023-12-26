from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.distance_1 import Distance1
from travelport.models.type_vehicle_location import TypeVehicleLocation
from travelport.models.type_vehicle_vendor_location import (
    TypeVehicleVendorLocation,
)

__NAMESPACE__ = "http://www.travelport.com/schema/vehicle_v52_0"


@dataclass
class VehicleDateLocation:
    """
    Parameters
    ----------
    vendor_location
        Specific vendor rental locations.  Applicable only for
        VehicleSearchAvailability.
    pickup_date_time
    pickup_location
        PickUpLocation is optional if Reference point is specified
    return_date_time
    return_location
        If not specified, the PickupLocation will be assumed
    pickup_location_type
        Required if use VendorLocationID. Ex: Terminal, ShuttleOnAirport,
        ShuttleOffAirport, RailwayStation, Hotel, CarDealer,
        CityCenterDowntown, EastOfCityCenter, SouthOfCityCenter,
        WestOfCityCenter, NorthOfCityCenter, PortOrFerry, NearResort,
        Airport, Unknown
    return_location_type
        Defaults to Pickup Location. Same options as Pickup Location.
    pickup_location_number
        The value of this attribute should be the same as the value of
        VendorLocationID returned as part of VendorLocation@VendorLocationID
        in a VehicleLocationRsp.
    return_location_number
    key
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/vehicle_v52_0"

    vendor_location: list[VehicleDateLocation.VendorLocation] = field(
        default_factory=list,
        metadata={
            "name": "VendorLocation",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    pickup_date_time: None | str = field(
        default=None,
        metadata={
            "name": "PickupDateTime",
            "type": "Attribute",
            "required": True,
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
    return_date_time: None | str = field(
        default=None,
        metadata={
            "name": "ReturnDateTime",
            "type": "Attribute",
            "required": True,
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
    pickup_location_type: None | TypeVehicleLocation = field(
        default=None,
        metadata={
            "name": "PickupLocationType",
            "type": "Attribute",
        },
    )
    return_location_type: None | TypeVehicleLocation = field(
        default=None,
        metadata={
            "name": "ReturnLocationType",
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
    return_location_number: None | str = field(
        default=None,
        metadata={
            "name": "ReturnLocationNumber",
            "type": "Attribute",
        },
    )
    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        },
    )

    @dataclass
    class VendorLocation(TypeVehicleVendorLocation):
        distance: None | Distance1 = field(
            default=None,
            metadata={
                "name": "Distance",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/common_v52_0",
            },
        )
