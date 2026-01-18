from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_door_count import TypeDoorCount
from travelport.models.type_vehicle_category import TypeVehicleCategory
from travelport.models.type_vehicle_class import TypeVehicleClass
from travelport.models.type_vehicle_transmission import TypeVehicleTransmission
from travelport.models.upsell_search_criteria import UpsellSearchCriteria

__NAMESPACE__ = "http://www.travelport.com/schema/util_v52_0"


@dataclass(kw_only=True)
class VehicleUpsellQualifySearchCriteria(UpsellSearchCriteria):
    """
    Search criteria for VehicleUpsellQualify.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    vendor_code: str = field(
        metadata={
            "name": "VendorCode",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 5,
        }
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
    discount_number: None | str = field(
        default=None,
        metadata={
            "name": "DiscountNumber",
            "type": "Attribute",
            "max_length": 25,
        },
    )
