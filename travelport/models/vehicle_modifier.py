from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_door_count import TypeDoorCount
from travelport.models.type_fuel import TypeFuel
from travelport.models.type_vehicle_category import TypeVehicleCategory
from travelport.models.type_vehicle_class import TypeVehicleClass
from travelport.models.type_vehicle_transmission import TypeVehicleTransmission

__NAMESPACE__ = "http://www.travelport.com/schema/vehicle_v52_0"


@dataclass
class VehicleModifier:
    """
    Parameters
    ----------
    air_conditioning
        Request vehicles with Air Conditioning Valid values: true, false.
    transmission_type
        Requested Transmission Type. Valid Values:  Automatic, Automatic4WD,
        ManualAWD, AutomaticAWD, Manual, Manual4WD.
    vehicle_class
        Class of vehicle
    category
        Category of vehicle. Each supplier decides how these categories map
        to a vehicle class.
    door_count
        The number of doors on vehicle.  Ex: TwoToThreeDoors,
        TwoToFourDoors, FourToFiveDoors
    fuel_type
        The fuel type of vehicle
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/vehicle_v52_0"

    air_conditioning: None | bool = field(
        default=None,
        metadata={
            "name": "AirConditioning",
            "type": "Attribute",
        }
    )
    transmission_type: None | TypeVehicleTransmission = field(
        default=None,
        metadata={
            "name": "TransmissionType",
            "type": "Attribute",
        }
    )
    vehicle_class: None | TypeVehicleClass = field(
        default=None,
        metadata={
            "name": "VehicleClass",
            "type": "Attribute",
        }
    )
    category: None | TypeVehicleCategory = field(
        default=None,
        metadata={
            "name": "Category",
            "type": "Attribute",
        }
    )
    door_count: None | TypeDoorCount = field(
        default=None,
        metadata={
            "name": "DoorCount",
            "type": "Attribute",
        }
    )
    fuel_type: None | TypeFuel = field(
        default=None,
        metadata={
            "name": "FuelType",
            "type": "Attribute",
        }
    )
