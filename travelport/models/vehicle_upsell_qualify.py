from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_door_count import TypeDoorCount
from travelport.models.type_element_status_1 import TypeElementStatus1
from travelport.models.type_rate_category import TypeRateCategory
from travelport.models.type_vehicle_category import TypeVehicleCategory
from travelport.models.type_vehicle_class import TypeVehicleClass
from travelport.models.type_vehicle_location import TypeVehicleLocation
from travelport.models.type_vehicle_transmission import TypeVehicleTransmission

__NAMESPACE__ = "http://www.travelport.com/schema/util_v52_0"


@dataclass
class VehicleUpsellQualify:
    """Qualify data of Vehicle against which Vehicle Availability search is matched
    to get an upsell Offer.

    Each qualify should have an offer.

    Parameters
    ----------
    key
    vendor_code
    effective_date
    expiration_date
    provider_code
    pickup_date_time
    pickup_location
    return_date_time
    return_location
    pickup_location_type
    return_location_type
    pickup_location_number
    return_location_number
    air_conditioning
    transmission_type
    vehicle_class
    category
    door_count
    rate_code
    rate_category
    discount_number
    offer_ref
    el_stat
        This attribute is used to show the action results of an element.
        Possible values are "A" (when elements have been added to the UR)
        and "M" (when existing elements have been modified). Response only.
    key_override
        If a duplicate key is found where we are adding elements in some
        cases like URAdd, then instead of erroring out set this attribute to
        true.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        },
    )
    vendor_code: None | str = field(
        default=None,
        metadata={
            "name": "VendorCode",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 5,
        },
    )
    effective_date: None | str = field(
        default=None,
        metadata={
            "name": "EffectiveDate",
            "type": "Attribute",
            "required": True,
            "pattern": r"[^:Z].*",
        },
    )
    expiration_date: None | str = field(
        default=None,
        metadata={
            "name": "ExpirationDate",
            "type": "Attribute",
            "required": True,
            "pattern": r"[^:Z].*",
        },
    )
    provider_code: None | str = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 5,
        },
    )
    pickup_date_time: None | str = field(
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
    air_conditioning: None | bool = field(
        default=None,
        metadata={
            "name": "AirConditioning",
            "type": "Attribute",
        },
    )
    transmission_type: None | TypeVehicleTransmission = field(
        default=None,
        metadata={
            "name": "TransmissionType",
            "type": "Attribute",
        },
    )
    vehicle_class: None | TypeVehicleClass = field(
        default=None,
        metadata={
            "name": "VehicleClass",
            "type": "Attribute",
        },
    )
    category: None | TypeVehicleCategory = field(
        default=None,
        metadata={
            "name": "Category",
            "type": "Attribute",
        },
    )
    door_count: None | TypeDoorCount = field(
        default=None,
        metadata={
            "name": "DoorCount",
            "type": "Attribute",
        },
    )
    rate_code: None | str = field(
        default=None,
        metadata={
            "name": "RateCode",
            "type": "Attribute",
            "max_length": 10,
        },
    )
    rate_category: None | TypeRateCategory = field(
        default=None,
        metadata={
            "name": "RateCategory",
            "type": "Attribute",
        },
    )
    discount_number: None | str = field(
        default=None,
        metadata={
            "name": "DiscountNumber",
            "type": "Attribute",
            "max_length": 25,
        },
    )
    offer_ref: None | str = field(
        default=None,
        metadata={
            "name": "OfferRef",
            "type": "Attribute",
        },
    )
    el_stat: None | TypeElementStatus1 = field(
        default=None,
        metadata={
            "name": "ElStat",
            "type": "Attribute",
        },
    )
    key_override: None | bool = field(
        default=None,
        metadata={
            "name": "KeyOverride",
            "type": "Attribute",
        },
    )
