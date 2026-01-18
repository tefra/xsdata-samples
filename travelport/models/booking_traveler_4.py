from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate

from travelport.models.air_seat_assignment_4 import AirSeatAssignment4
from travelport.models.applied_profile_4 import AppliedProfile4
from travelport.models.booking_traveler_name_4 import BookingTravelerName4
from travelport.models.customized_name_data_4 import CustomizedNameData4
from travelport.models.delivery_info_4 import DeliveryInfo4
from travelport.models.discount_card_4 import DiscountCard4
from travelport.models.drivers_license_4 import DriversLicense4
from travelport.models.email_4 import Email4
from travelport.models.loyalty_card_4 import LoyaltyCard4
from travelport.models.name_remark_4 import NameRemark4
from travelport.models.phone_number_5 import PhoneNumber5
from travelport.models.rail_seat_assignment_4 import RailSeatAssignment4
from travelport.models.ssr_4 import Ssr4
from travelport.models.travel_compliance_data_4 import TravelComplianceData4
from travelport.models.travel_info_4 import TravelInfo4
from travelport.models.type_element_status_5 import TypeElementStatus5
from travelport.models.type_structured_address_5 import TypeStructuredAddress5

__NAMESPACE__ = "http://www.travelport.com/schema/common_v37_0"


@dataclass(kw_only=True)
class BookingTraveler4:
    """
    A traveler and all their accompanying data.

    Parameters
    ----------
    booking_traveler_name
    delivery_info
    phone_number
    email
    loyalty_card
    discount_card
    ssr
    name_remark
    air_seat_assignment
    rail_seat_assignment
    emergency_info
    address
    drivers_license
    applied_profile
    customized_name_data
    travel_compliance_data
        Travel Compliance and Preferred Supplier information of the booking
        traveler specific to a segment. Not applicable to Saved Trip.
    travel_info
    key
    traveler_type
        Defines the type of traveler used for booking which could be a non-
        defining type (Companion, Web-fare, etc), or a standard type (Adult,
        Child, etc).
    age
        BookingTraveler age
    vip
        When set to True indicates that the Booking Traveler is a VIP based
        on agency/customer criteria
    dob
        Traveler Date of Birth
    gender
        The BookingTraveler gender type
    nationality
        Specify ISO country code for nationality of the Booking Traveler
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
        name = "BookingTraveler"
        namespace = "http://www.travelport.com/schema/common_v37_0"

    booking_traveler_name: BookingTravelerName4 = field(
        metadata={
            "name": "BookingTravelerName",
            "type": "Element",
            "required": True,
        }
    )
    delivery_info: list[DeliveryInfo4] = field(
        default_factory=list,
        metadata={
            "name": "DeliveryInfo",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    phone_number: list[PhoneNumber5] = field(
        default_factory=list,
        metadata={
            "name": "PhoneNumber",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    email: list[Email4] = field(
        default_factory=list,
        metadata={
            "name": "Email",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    loyalty_card: list[LoyaltyCard4] = field(
        default_factory=list,
        metadata={
            "name": "LoyaltyCard",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    discount_card: list[DiscountCard4] = field(
        default_factory=list,
        metadata={
            "name": "DiscountCard",
            "type": "Element",
            "max_occurs": 9,
        },
    )
    ssr: list[Ssr4] = field(
        default_factory=list,
        metadata={
            "name": "SSR",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    name_remark: list[NameRemark4] = field(
        default_factory=list,
        metadata={
            "name": "NameRemark",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    air_seat_assignment: list[AirSeatAssignment4] = field(
        default_factory=list,
        metadata={
            "name": "AirSeatAssignment",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    rail_seat_assignment: list[RailSeatAssignment4] = field(
        default_factory=list,
        metadata={
            "name": "RailSeatAssignment",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    emergency_info: None | str = field(
        default=None,
        metadata={
            "name": "EmergencyInfo",
            "type": "Element",
        },
    )
    address: list[TypeStructuredAddress5] = field(
        default_factory=list,
        metadata={
            "name": "Address",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    drivers_license: list[DriversLicense4] = field(
        default_factory=list,
        metadata={
            "name": "DriversLicense",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    applied_profile: list[AppliedProfile4] = field(
        default_factory=list,
        metadata={
            "name": "AppliedProfile",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    customized_name_data: list[CustomizedNameData4] = field(
        default_factory=list,
        metadata={
            "name": "CustomizedNameData",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    travel_compliance_data: list[TravelComplianceData4] = field(
        default_factory=list,
        metadata={
            "name": "TravelComplianceData",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    travel_info: None | TravelInfo4 = field(
        default=None,
        metadata={
            "name": "TravelInfo",
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
    age: None | int = field(
        default=None,
        metadata={
            "name": "Age",
            "type": "Attribute",
        },
    )
    vip: bool = field(
        default=False,
        metadata={
            "name": "VIP",
            "type": "Attribute",
        },
    )
    dob: None | XmlDate = field(
        default=None,
        metadata={
            "name": "DOB",
            "type": "Attribute",
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
    nationality: None | str = field(
        default=None,
        metadata={
            "name": "Nationality",
            "type": "Attribute",
            "length": 2,
        },
    )
    el_stat: None | TypeElementStatus5 = field(
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
