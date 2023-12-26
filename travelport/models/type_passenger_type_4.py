from __future__ import annotations
from dataclasses import dataclass, field
from xsdata.models.datatype import XmlDate
from travelport.models.discount_card_4 import DiscountCard4
from travelport.models.loyalty_card_4 import LoyaltyCard4
from travelport.models.name_4 import Name4
from travelport.models.personal_geography_4 import PersonalGeography4
from travelport.models.type_residency_4 import TypeResidency4

__NAMESPACE__ = "http://www.travelport.com/schema/common_v37_0"


@dataclass
class TypePassengerType4:
    """
    Passenger type code with optional age information.

    Parameters
    ----------
    name
        Optional passenger Name with associated LoyaltyCard may provide
        benefit when pricing itineraries using Low Cost Carriers. In
        general, most carriers do not consider passenger LoyalyCard
        information when initially pricing itineraries.
    loyalty_card
    discount_card
    personal_geography
        Passenger personal geography detail to be sent to Host for accessing
        location specific fares
    code
        The 3-char IATA passenger type code
    age
    dob
        Passenger Date of Birth
    gender
        The passenger gender type
    price_ptconly
    booking_traveler_ref
        This value should be set for Multiple Passengers in the request.
    accompanied_passenger
        Container to identify accompanied passenger. Set true means this
        passenger is accompanied
    residency_type
        The passenger residence type.
    """

    class Meta:
        name = "typePassengerType"

    name: None | Name4 = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v37_0",
        },
    )
    loyalty_card: list[LoyaltyCard4] = field(
        default_factory=list,
        metadata={
            "name": "LoyaltyCard",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v37_0",
            "max_occurs": 999,
        },
    )
    discount_card: list[DiscountCard4] = field(
        default_factory=list,
        metadata={
            "name": "DiscountCard",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v37_0",
            "max_occurs": 9,
        },
    )
    personal_geography: None | PersonalGeography4 = field(
        default=None,
        metadata={
            "name": "PersonalGeography",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v37_0",
        },
    )
    code: None | str = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
            "required": True,
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
    price_ptconly: None | bool = field(
        default=None,
        metadata={
            "name": "PricePTCOnly",
            "type": "Attribute",
        },
    )
    booking_traveler_ref: None | str = field(
        default=None,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Attribute",
        },
    )
    accompanied_passenger: bool = field(
        default=False,
        metadata={
            "name": "AccompaniedPassenger",
            "type": "Attribute",
        },
    )
    residency_type: None | TypeResidency4 = field(
        default=None,
        metadata={
            "name": "ResidencyType",
            "type": "Attribute",
        },
    )
