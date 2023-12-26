from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_door_count import TypeDoorCount
from travelport.models.type_fuel import TypeFuel
from travelport.models.type_policy_codes_list_1 import TypePolicyCodesList1
from travelport.models.type_vehicle_category import TypeVehicleCategory
from travelport.models.type_vehicle_class import TypeVehicleClass
from travelport.models.type_vehicle_transmission import TypeVehicleTransmission
from travelport.models.vehicle_rate import VehicleRate

__NAMESPACE__ = "http://www.travelport.com/schema/vehicle_v52_0"


@dataclass
class Vehicle:
    """
    Information related to single vehicle.

    Parameters
    ----------
    policy_codes_list
        A list of codes that indicate why an item was determined to be ‘out
        of policy’.
    vehicle_rate
    vendor_code
    air_conditioning
        True or False.
    transmission_type
        Automatic, Manual
    vehicle_class
        Class of vehicle
    category
        Category of vehicle. Each supplier decides how these categories map
        to a vehicle class.
    description
        Car type Description such as 'CHRYSLER SEBRING OR SIMILAR'
    door_count
        The number of doors on vehicle.  Ex: TwoToThreeDoors,
        TwoToFourDoors, FourToFiveDoors
    location
        Location of the Vehicle or Counter
    counter_location_code
        Four character Code to identify the Location of the Rental Counter,
        e.g. OMSO, PHON.
    vendor_location_key
        Identifies the specific vendor location
    vendor_name
        The vendor's name
    alternate_vendor
        A vendor renting the vehicle on behalf of another company
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
    key
    return_at_pickup
        Indicates whether vehicle can be returned at any location or pickup
        point only. If ReturnAtPickup = false then vehicle can be returned
        at any location else if ReturnAtPickup = true, vehicle should be
        returned in Pickup point only. Supported Providers : 1G/1V
    in_policy
        This attribute will be used to indicate if a fare or rate has been
        determined to be ‘in policy’ based on the associated policy
        settings.
    policy_code
        This attribute is used to provide a code that can be used to
        determine why an item was determined to be ‘out of policy’.
    preferred_option
        This attribute is used to indicate if the vendors responsible for
        the fare or rate being returned have been determined to be
        ‘preferred’ based on the associated policy settings.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/vehicle_v52_0"

    policy_codes_list: None | TypePolicyCodesList1 = field(
        default=None,
        metadata={
            "name": "PolicyCodesList",
            "type": "Element",
        },
    )
    vehicle_rate: None | VehicleRate = field(
        default=None,
        metadata={
            "name": "VehicleRate",
            "type": "Element",
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
    air_conditioning: None | bool = field(
        default=None,
        metadata={
            "name": "AirConditioning",
            "type": "Attribute",
            "required": True,
        },
    )
    transmission_type: None | TypeVehicleTransmission = field(
        default=None,
        metadata={
            "name": "TransmissionType",
            "type": "Attribute",
            "required": True,
        },
    )
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
            "required": True,
        },
    )
    description: None | str = field(
        default=None,
        metadata={
            "name": "Description",
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
    location: None | str = field(
        default=None,
        metadata={
            "name": "Location",
            "type": "Attribute",
        },
    )
    counter_location_code: None | str = field(
        default=None,
        metadata={
            "name": "CounterLocationCode",
            "type": "Attribute",
            "min_length": 4,
            "max_length": 4,
        },
    )
    vendor_location_key: None | str = field(
        default=None,
        metadata={
            "name": "VendorLocationKey",
            "type": "Attribute",
        },
    )
    vendor_name: None | str = field(
        default=None,
        metadata={
            "name": "VendorName",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 20,
        },
    )
    alternate_vendor: None | str = field(
        default=None,
        metadata={
            "name": "AlternateVendor",
            "type": "Attribute",
        },
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
    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        },
    )
    return_at_pickup: None | bool = field(
        default=None,
        metadata={
            "name": "ReturnAtPickup",
            "type": "Attribute",
        },
    )
    in_policy: None | bool = field(
        default=None,
        metadata={
            "name": "InPolicy",
            "type": "Attribute",
        },
    )
    policy_code: None | int = field(
        default=None,
        metadata={
            "name": "PolicyCode",
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 9999,
        },
    )
    preferred_option: None | bool = field(
        default=None,
        metadata={
            "name": "PreferredOption",
            "type": "Attribute",
        },
    )
