from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.operation_time import OperationTime
from travelport.models.phone_number_1 import PhoneNumber1
from travelport.models.type_structured_address_1 import TypeStructuredAddress1
from travelport.models.type_vehicle_location import TypeVehicleLocation

__NAMESPACE__ = "http://www.travelport.com/schema/vehicle_v52_0"


@dataclass
class TypeVehicleLocationInformation:
    """
    Valid for VehicleRulesRsp 1P only.

    Parameters
    ----------
    address
        Pickup/Return Location Address.Data is not always returned by the
        vendor.
    phone_number
        Pickup location phone numbers.Data is not always returned by the
        vendor.
    operation_time
        Pickup/Return Location Hours of operation. Data is not always
        returned by the vendor.
    location_name
        Pickup/Return Location Name.
    counter_location
        Pickup CounterLocation Name .
    vendor_code
        Pickup/Return Location Vendor Code.
    location_code
        Pickup/Return Location City/Airport  Code .
    location_type
        Pickup/Return Location .
    location_number
        Pickup/Return Location Number.
    """

    class Meta:
        name = "typeVehicleLocationInformation"

    address: None | TypeStructuredAddress1 = field(
        default=None,
        metadata={
            "name": "Address",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/vehicle_v52_0",
        },
    )
    phone_number: list[PhoneNumber1] = field(
        default_factory=list,
        metadata={
            "name": "PhoneNumber",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 3,
        },
    )
    operation_time: list[OperationTime] = field(
        default_factory=list,
        metadata={
            "name": "OperationTime",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/vehicle_v52_0",
            "max_occurs": 100,
        },
    )
    location_name: None | str = field(
        default=None,
        metadata={
            "name": "LocationName",
            "type": "Attribute",
        },
    )
    counter_location: None | str = field(
        default=None,
        metadata={
            "name": "CounterLocation",
            "type": "Attribute",
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
    location_code: None | str = field(
        default=None,
        metadata={
            "name": "LocationCode",
            "type": "Attribute",
            "length": 3,
            "white_space": "collapse",
        },
    )
    location_type: None | TypeVehicleLocation = field(
        default=None,
        metadata={
            "name": "LocationType",
            "type": "Attribute",
        },
    )
    location_number: None | str = field(
        default=None,
        metadata={
            "name": "LocationNumber",
            "type": "Attribute",
            "min_length": 3,
            "max_length": 3,
        },
    )
