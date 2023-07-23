from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.associated_remark_3 import AssociatedRemark3
from travelport.models.booking_source_1 import BookingSource1
from travelport.models.corporate_discount_id_1 import CorporateDiscountId1
from travelport.models.guarantee_1 import Guarantee1
from travelport.models.guest_information import GuestInformation
from travelport.models.hotel_bedding import HotelBedding
from travelport.models.loyalty_card_1 import LoyaltyCard1
from travelport.models.reservation_name_1 import ReservationName1
from travelport.models.third_party_information_1 import ThirdPartyInformation1
from travelport.models.travel_compliance_data_1 import TravelComplianceData1

__NAMESPACE__ = "http://www.travelport.com/schema/universal_v52_0"


@dataclass
class HotelAdd:
    """
    Parameters
    ----------
    loyalty_card
    guarantee
    guest_information
    associated_remark
    booking_source
    hotel_special_request
    corporate_discount_id
    reservation_name
    third_party_information
    travel_compliance_data
    hotel_bedding
        Specify desired optional bed types. Applicable for optional bed
        types:RollawayAdult,RollawayChild,or Crib if supported by the hotel
        supplier. Providers :1G/1V/1P
    booking_confirmation
    reservation_locator_code
    booking_traveler_ref
        BookingTravelerRef will be used to specify BookingTraveler in UR.
        Currently this will be used to LoyaltyCard modification. Later this
        can used for other elements which are associated with
        BookngTraveler.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    loyalty_card: list[LoyaltyCard1] = field(
        default_factory=list,
        metadata={
            "name": "LoyaltyCard",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    guarantee: None | Guarantee1 = field(
        default=None,
        metadata={
            "name": "Guarantee",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    guest_information: None | GuestInformation = field(
        default=None,
        metadata={
            "name": "GuestInformation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/hotel_v52_0",
        }
    )
    associated_remark: list[AssociatedRemark3] = field(
        default_factory=list,
        metadata={
            "name": "AssociatedRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/hotel_v52_0",
            "max_occurs": 999,
        }
    )
    booking_source: None | BookingSource1 = field(
        default=None,
        metadata={
            "name": "BookingSource",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    hotel_special_request: None | str = field(
        default=None,
        metadata={
            "name": "HotelSpecialRequest",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/hotel_v52_0",
            "max_length": 250,
        }
    )
    corporate_discount_id: None | CorporateDiscountId1 = field(
        default=None,
        metadata={
            "name": "CorporateDiscountID",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    reservation_name: None | ReservationName1 = field(
        default=None,
        metadata={
            "name": "ReservationName",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    third_party_information: None | ThirdPartyInformation1 = field(
        default=None,
        metadata={
            "name": "ThirdPartyInformation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    travel_compliance_data: list[TravelComplianceData1] = field(
        default_factory=list,
        metadata={
            "name": "TravelComplianceData",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    hotel_bedding: list[HotelBedding] = field(
        default_factory=list,
        metadata={
            "name": "HotelBedding",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/hotel_v52_0",
            "max_occurs": 999,
        }
    )
    booking_confirmation: None | str = field(
        default=None,
        metadata={
            "name": "BookingConfirmation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/hotel_v52_0",
            "max_length": 32,
        }
    )
    reservation_locator_code: None | str = field(
        default=None,
        metadata={
            "name": "ReservationLocatorCode",
            "type": "Attribute",
            "required": True,
            "min_length": 5,
            "max_length": 8,
        }
    )
    booking_traveler_ref: None | str = field(
        default=None,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Attribute",
        }
    )
