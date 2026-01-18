from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_fuel import TypeFuel
from travelport.models.type_vehicle_category import TypeVehicleCategory
from travelport.models.type_vehicle_class import TypeVehicleClass
from travelport.models.type_vehicle_transmission import TypeVehicleTransmission

__NAMESPACE__ = "http://www.travelport.com/schema/vehicle_v52_0"


@dataclass(kw_only=True)
class VehicleDetail:
    """
    Make, model, etc information about the available vehicles.

    Parameters
    ----------
    code
        The industry standard code for this vehicle
    supplier_code
        The supplier specific code for this vehicle.
    passenger_count
        Number of passengers this car can hold (e.g. 4-5)
    number_of_doors
        The number of doors on vehicle.  Ex: TwoToThreeDoors,
        TwoToFourDoors, FourToFiveDoors
    bag_count
        The number of bags
    class_value
    category
    air_conditioning
        True or False.
    transmission
        Automatic, Manual
    make_model
        The Make and Model description of this vehicle
    fuel_type
        The fuel type of vehicle
    acriss_vehicle_code
        The Association of Car Rental Industry System Standards (ACRISS),
        develops standards to avoid misleading information when making a car
        rental booking online or via any electronic means. ACRISS provides
        an industry standard vehicle matrix to define car models ensuring a
        like to like comparison of vehicle. Each ACRISS code defining a car
        model consists of four characters as defined. 1st character denotes
        the vehicle category – based on size, cost, power and luxury
        factor.2nd character defines the vehicle type – chassis type (van,
        SUV, wagon, convertible).3rd character defines the transmission and
        drive – automatic / manual and 2WD / 4WD / AWD. 4th character
        defines the fuel type (petrol / diesel / hybrid…) and whether air
        conditioned.Examples are ICAR,ECAR,etc.
    preferred_option
        Preferred Option marker for Location
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/vehicle_v52_0"

    code: str = field(
        metadata={
            "name": "Code",
            "type": "Attribute",
            "required": True,
        }
    )
    supplier_code: None | str = field(
        default=None,
        metadata={
            "name": "SupplierCode",
            "type": "Attribute",
        },
    )
    passenger_count: None | str = field(
        default=None,
        metadata={
            "name": "PassengerCount",
            "type": "Attribute",
        },
    )
    number_of_doors: None | str = field(
        default=None,
        metadata={
            "name": "NumberOfDoors",
            "type": "Attribute",
        },
    )
    bag_count: None | str = field(
        default=None,
        metadata={
            "name": "BagCount",
            "type": "Attribute",
        },
    )
    class_value: TypeVehicleClass = field(
        metadata={
            "name": "Class",
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
    air_conditioning: bool = field(
        metadata={
            "name": "AirConditioning",
            "type": "Attribute",
            "required": True,
        }
    )
    transmission: TypeVehicleTransmission = field(
        metadata={
            "name": "Transmission",
            "type": "Attribute",
            "required": True,
        }
    )
    make_model: str = field(
        metadata={
            "name": "MakeModel",
            "type": "Attribute",
            "required": True,
        }
    )
    fuel_type: None | TypeFuel = field(
        default=None,
        metadata={
            "name": "FuelType",
            "type": "Attribute",
        },
    )
    acriss_vehicle_code: None | str = field(
        default=None,
        metadata={
            "name": "AcrissVehicleCode",
            "type": "Attribute",
            "max_length": 4,
        },
    )
    preferred_option: None | bool = field(
        default=None,
        metadata={
            "name": "PreferredOption",
            "type": "Attribute",
        },
    )
