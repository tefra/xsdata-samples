from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_door_count import TypeDoorCount
from travelport.models.type_vehicle_category import TypeVehicleCategory
from travelport.models.type_vehicle_class import TypeVehicleClass
from travelport.models.type_vehicle_transmission import TypeVehicleTransmission

__NAMESPACE__ = "http://www.travelport.com/schema/util_v52_0"


@dataclass
class VehicleUpsellOfferSearchCriteria:
    """
    Search criteria for VehicleUpsellOffers.

    Parameters
    ----------
    vehicle_class
        Class of vehicle
    category
        Category of vehicle. Each supplier decides how these categories map
        to a vehicle class.
    air_conditioning
    transmission_type
    door_count
        The number of doors on the vehicle. Could be a range like '2-4'
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    vehicle_class: None | TypeVehicleClass = field(
        default=None,
        metadata={
            "name": "VehicleClass",
            "type": "Attribute",
            "required": True,
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
