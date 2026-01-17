from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate

from travelport.models.applied_profile_3 import AppliedProfile3
from travelport.models.booking_traveler_name_3 import BookingTravelerName3
from travelport.models.customized_name_data_3 import CustomizedNameData3
from travelport.models.delivery_info_3 import DeliveryInfo3
from travelport.models.email_3 import Email3
from travelport.models.name_remark_3 import NameRemark3
from travelport.models.phone_number_4 import PhoneNumber4
from travelport.models.travel_info_3 import TravelInfo3
from travelport.models.type_structured_address_4 import TypeStructuredAddress4

__NAMESPACE__ = "http://www.travelport.com/schema/common_v33_0"


@dataclass
class BookingTravelerInfo3:
    """
    Container that will allow modifying Universal record data that is not
    product specific.

    Parameters
    ----------
    booking_traveler_name
    name_remark
    dob
        Traveler Date of Birth
    travel_info
    email
    phone_number
    address
    emergency_info
    delivery_info
    age
    customized_name_data
    applied_profile
    key
    traveler_type
    gender
    """

    class Meta:
        name = "BookingTravelerInfo"
        namespace = "http://www.travelport.com/schema/common_v33_0"

    booking_traveler_name: None | BookingTravelerName3 = field(
        default=None,
        metadata={
            "name": "BookingTravelerName",
            "type": "Element",
        },
    )
    name_remark: None | NameRemark3 = field(
        default=None,
        metadata={
            "name": "NameRemark",
            "type": "Element",
        },
    )
    dob: None | XmlDate = field(
        default=None,
        metadata={
            "name": "DOB",
            "type": "Element",
        },
    )
    travel_info: None | TravelInfo3 = field(
        default=None,
        metadata={
            "name": "TravelInfo",
            "type": "Element",
        },
    )
    email: None | Email3 = field(
        default=None,
        metadata={
            "name": "Email",
            "type": "Element",
        },
    )
    phone_number: None | PhoneNumber4 = field(
        default=None,
        metadata={
            "name": "PhoneNumber",
            "type": "Element",
        },
    )
    address: None | TypeStructuredAddress4 = field(
        default=None,
        metadata={
            "name": "Address",
            "type": "Element",
        },
    )
    emergency_info: None | str = field(
        default=None,
        metadata={
            "name": "EmergencyInfo",
            "type": "Element",
        },
    )
    delivery_info: None | DeliveryInfo3 = field(
        default=None,
        metadata={
            "name": "DeliveryInfo",
            "type": "Element",
        },
    )
    age: None | int = field(
        default=None,
        metadata={
            "name": "Age",
            "type": "Element",
        },
    )
    customized_name_data: None | CustomizedNameData3 = field(
        default=None,
        metadata={
            "name": "CustomizedNameData",
            "type": "Element",
        },
    )
    applied_profile: None | AppliedProfile3 = field(
        default=None,
        metadata={
            "name": "AppliedProfile",
            "type": "Element",
        },
    )
    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        },
    )
    traveler_type: None | str = field(
        default=None,
        metadata={
            "name": "TravelerType",
            "type": "Attribute",
            "min_length": 3,
            "max_length": 5,
        },
    )
    gender: None | str = field(
        default=None,
        metadata={
            "name": "Gender",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 2,
        },
    )
