from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate

from travelport.models.air_seat_assignment_5 import AirSeatAssignment5
from travelport.models.applied_profile_5 import AppliedProfile5
from travelport.models.booking_traveler_name_5 import BookingTravelerName5
from travelport.models.customized_name_data_5 import CustomizedNameData5
from travelport.models.delivery_info_5 import DeliveryInfo5
from travelport.models.discount_card_5 import DiscountCard5
from travelport.models.drivers_license_5 import DriversLicense5
from travelport.models.email_5 import Email5
from travelport.models.loyalty_card_5 import LoyaltyCard5
from travelport.models.name_remark_5 import NameRemark5
from travelport.models.phone_number_6 import PhoneNumber6
from travelport.models.rail_seat_assignment_5 import RailSeatAssignment5
from travelport.models.ssr_5 import Ssr5
from travelport.models.travel_compliance_data_5 import TravelComplianceData5
from travelport.models.travel_info_5 import TravelInfo5
from travelport.models.type_element_status_6 import TypeElementStatus6
from travelport.models.type_structured_address_6 import TypeStructuredAddress6

__NAMESPACE__ = "http://www.travelport.com/schema/common_v34_0"


@dataclass
class BookingTraveler5:
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
        namespace = "http://www.travelport.com/schema/common_v34_0"

    booking_traveler_name: None | BookingTravelerName5 = field(
        default=None,
        metadata={
            "name": "BookingTravelerName",
            "type": "Element",
            "required": True,
        },
    )
    delivery_info: list[DeliveryInfo5] = field(
        default_factory=list,
        metadata={
            "name": "DeliveryInfo",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    phone_number: list[PhoneNumber6] = field(
        default_factory=list,
        metadata={
            "name": "PhoneNumber",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    email: list[Email5] = field(
        default_factory=list,
        metadata={
            "name": "Email",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    loyalty_card: list[LoyaltyCard5] = field(
        default_factory=list,
        metadata={
            "name": "LoyaltyCard",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    discount_card: list[DiscountCard5] = field(
        default_factory=list,
        metadata={
            "name": "DiscountCard",
            "type": "Element",
            "max_occurs": 9,
        },
    )
    ssr: list[Ssr5] = field(
        default_factory=list,
        metadata={
            "name": "SSR",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    name_remark: list[NameRemark5] = field(
        default_factory=list,
        metadata={
            "name": "NameRemark",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    air_seat_assignment: list[AirSeatAssignment5] = field(
        default_factory=list,
        metadata={
            "name": "AirSeatAssignment",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    rail_seat_assignment: list[RailSeatAssignment5] = field(
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
    address: list[TypeStructuredAddress6] = field(
        default_factory=list,
        metadata={
            "name": "Address",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    drivers_license: list[DriversLicense5] = field(
        default_factory=list,
        metadata={
            "name": "DriversLicense",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    applied_profile: list[AppliedProfile5] = field(
        default_factory=list,
        metadata={
            "name": "AppliedProfile",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    customized_name_data: list[CustomizedNameData5] = field(
        default_factory=list,
        metadata={
            "name": "CustomizedNameData",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    travel_compliance_data: list[TravelComplianceData5] = field(
        default_factory=list,
        metadata={
            "name": "TravelComplianceData",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    travel_info: None | TravelInfo5 = field(
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
    el_stat: None | TypeElementStatus6 = field(
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
