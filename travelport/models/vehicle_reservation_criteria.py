from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_date_spec import TypeDateSpec

__NAMESPACE__ = "http://www.travelport.com/schema/universal_v52_0"


@dataclass(kw_only=True)
class VehicleReservationCriteria:
    """
    Criteria for searching the Vehicle reservations.

    Parameters
    ----------
    pick_up_date
        Vehicle PickUp Date or Date Range
    vehicle_confirmation
    location
    vendor_code
        Vehicle Vendor Code
    location_number
    passive_only
        Search for Passives Only
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    pick_up_date: None | TypeDateSpec = field(
        default=None,
        metadata={
            "name": "PickUpDate",
            "type": "Element",
        },
    )
    vehicle_confirmation: None | str = field(
        default=None,
        metadata={
            "name": "VehicleConfirmation",
            "type": "Attribute",
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
    vendor_code: None | str = field(
        default=None,
        metadata={
            "name": "VendorCode",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 5,
        },
    )
    location_number: None | str = field(
        default=None,
        metadata={
            "name": "LocationNumber",
            "type": "Attribute",
        },
    )
    passive_only: bool = field(
        default=False,
        metadata={
            "name": "PassiveOnly",
            "type": "Attribute",
        },
    )
