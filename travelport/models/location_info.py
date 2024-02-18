from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.location_address_1 import LocationAddress1
from travelport.models.operation_time import OperationTime
from travelport.models.phone_number_1 import PhoneNumber1

__NAMESPACE__ = "http://www.travelport.com/schema/vehicle_v52_0"


@dataclass
class LocationInfo:
    """
    Parameters
    ----------
    location_address
    phone_number
    operation_time
    shuttle_info
    name
        A descriptive name (Los Angeles Intl Airport)
    counter_location
        Where is the counter located
    preferred_option
        Preferred Option marker for Location.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/vehicle_v52_0"

    location_address: list[LocationAddress1] = field(
        default_factory=list,
        metadata={
            "name": "LocationAddress",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 5,
        },
    )
    phone_number: list[PhoneNumber1] = field(
        default_factory=list,
        metadata={
            "name": "PhoneNumber",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 5,
        },
    )
    operation_time: list[OperationTime] = field(
        default_factory=list,
        metadata={
            "name": "OperationTime",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    shuttle_info: None | str = field(
        default=None,
        metadata={
            "name": "ShuttleInfo",
            "type": "Element",
        },
    )
    name: None | str = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "required": True,
        },
    )
    counter_location: None | str = field(
        default=None,
        metadata={
            "name": "CounterLocation",
            "type": "Attribute",
        },
    )
    preferred_option: None | bool = field(
        default=None,
        metadata={
            "name": "PreferredOption",
            "type": "Attribute",
        },
    )
