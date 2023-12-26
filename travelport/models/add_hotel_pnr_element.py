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
from travelport.models.travel_compliance_data_1 import TravelComplianceData1

__NAMESPACE__ = "http://www.travelport.com/schema/sharedBooking_v52_0"


@dataclass
class AddHotelPnrElement:
    """
    Container for Hotel PNR elements to be added.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/sharedBooking_v52_0"

    guarantee: None | Guarantee1 = field(
        default=None,
        metadata={
            "name": "Guarantee",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        },
    )
    guest_information: None | GuestInformation = field(
        default=None,
        metadata={
            "name": "GuestInformation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/hotel_v52_0",
        },
    )
    associated_remark: list[AssociatedRemark3] = field(
        default_factory=list,
        metadata={
            "name": "AssociatedRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/hotel_v52_0",
            "max_occurs": 99,
        },
    )
    booking_source: None | BookingSource1 = field(
        default=None,
        metadata={
            "name": "BookingSource",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        },
    )
    hotel_special_request: None | str = field(
        default=None,
        metadata={
            "name": "HotelSpecialRequest",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/hotel_v52_0",
            "max_length": 250,
        },
    )
    corporate_discount_id: None | CorporateDiscountId1 = field(
        default=None,
        metadata={
            "name": "CorporateDiscountID",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        },
    )
    reservation_name: None | ReservationName1 = field(
        default=None,
        metadata={
            "name": "ReservationName",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        },
    )
    travel_compliance_data: list[TravelComplianceData1] = field(
        default_factory=list,
        metadata={
            "name": "TravelComplianceData",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 99,
        },
    )
    hotel_bedding: list[HotelBedding] = field(
        default_factory=list,
        metadata={
            "name": "HotelBedding",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/hotel_v52_0",
            "max_occurs": 99,
        },
    )
    loyalty_card: list[LoyaltyCard1] = field(
        default_factory=list,
        metadata={
            "name": "LoyaltyCard",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 99,
        },
    )
    reservation_locator_code: None | str = field(
        default=None,
        metadata={
            "name": "ReservationLocatorCode",
            "type": "Attribute",
            "required": True,
            "min_length": 5,
            "max_length": 8,
        },
    )
    booking_traveler_ref: None | str = field(
        default=None,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Attribute",
        },
    )
