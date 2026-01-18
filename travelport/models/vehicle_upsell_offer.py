from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_door_count import TypeDoorCount
from travelport.models.type_element_status_1 import TypeElementStatus1
from travelport.models.type_fuel import TypeFuel
from travelport.models.type_rate_category import TypeRateCategory
from travelport.models.type_vehicle_category import TypeVehicleCategory
from travelport.models.type_vehicle_class import TypeVehicleClass
from travelport.models.type_vehicle_transmission import TypeVehicleTransmission

__NAMESPACE__ = "http://www.travelport.com/schema/util_v52_0"


@dataclass(kw_only=True)
class VehicleUpsellOffer:
    """
    Offer data of Vehicle which is used to send an upsell request.

    Offer is found for a matching qualify.

    Parameters
    ----------
    air_conditioning
    transmission_type
    vehicle_class
        Class of vehicle
    category
        Category of vehicle. Each supplier decides how these categories map
        to a vehicle class.
    door_count
        The number of doors on the vehicle. Could be a range like '2-4'
    rate_code
    rate_category
        The category of this rate (Best, etc)
    discount_number
    fuel_type
    key
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

    air_conditioning: bool = field(
        metadata={
            "name": "AirConditioning",
            "type": "Attribute",
            "required": True,
        }
    )
    transmission_type: TypeVehicleTransmission = field(
        metadata={
            "name": "TransmissionType",
            "type": "Attribute",
            "required": True,
        }
    )
    vehicle_class: TypeVehicleClass = field(
        metadata={
            "name": "VehicleClass",
            "type": "Attribute",
            "required": True,
        }
    )
    category: TypeVehicleCategory = field(
        metadata={
            "name": "Category",
            "type": "Attribute",
            "required": True,
        }
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
    fuel_type: None | TypeFuel = field(
        default=None,
        metadata={
            "name": "FuelType",
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
