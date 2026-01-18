from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.action_status_1 import ActionStatus1
from travelport.models.associated_remark_3 import AssociatedRemark3
from travelport.models.base_create_with_form_of_payment_req_1 import (
    BaseCreateWithFormOfPaymentReq1,
)
from travelport.models.booking_source_1 import BookingSource1
from travelport.models.email_1 import Email1
from travelport.models.guarantee_1 import Guarantee1
from travelport.models.guest_information import GuestInformation
from travelport.models.host_token_1 import HostToken1
from travelport.models.hotel_bedding import HotelBedding
from travelport.models.hotel_commission import HotelCommission
from travelport.models.hotel_property import HotelProperty
from travelport.models.hotel_rate_detail import HotelRateDetail
from travelport.models.hotel_special_request import HotelSpecialRequest
from travelport.models.hotel_stay import HotelStay
from travelport.models.phone_number_1 import PhoneNumber1
from travelport.models.point_of_sale_1 import PointOfSale1
from travelport.models.promotion_code import PromotionCode
from travelport.models.reservation_name_1 import ReservationName1
from travelport.models.review_booking_1 import ReviewBooking1
from travelport.models.third_party_information_1 import ThirdPartyInformation1

__NAMESPACE__ = "http://www.travelport.com/schema/universal_v52_0"


@dataclass(kw_only=True)
class HotelCreateReservationReq(BaseCreateWithFormOfPaymentReq1):
    """
    Request to create a hotel reservation.

    Parameters
    ----------
    email
    phone_number
    hotel_rate_detail
    hotel_property
    third_party_information
    hotel_stay
    guarantee
    hotel_special_request
    point_of_sale
    promotion_code
        Used to specify promotional code include in the booking
    booking_source
        Specify alternate booking source
    hotel_bedding
    guest_information
    associated_remark
    reservation_name
        If specified then it will be used for GDS reservation otherwise
        first booking traveler will be used.
    action_status
    host_token
    review_booking
        Review Booking or Queue Minders is to add the reminders in the
        Provider Reservation along with the date time and Queue details. On
        the date time defined in reminders, the message along with the PNR
        goes to the desired Queue.
    hotel_commission
        This element indicates hotel commission applied during hotel
        booking.  Provider supported 1P.
    user_acceptance
        If true, traveler has reviewed and accepted all policies,
        restrictions, and terms and conditions prior to booking. Default,
        false.
    mandatory_rate_match
        If true, hotel will not be booked if there is a rate discrepancy.
        Default is false. Supported providers: 1g,1v,1p.
    status_code
        Hotel Segment Status Code.Supported Providers:1P.
    booking_confirmation
        Hotel Booking Confirmation Number for passive hotel segment.
        Supported Providers:1P.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    email: list[Email1] = field(
        default_factory=list,
        metadata={
            "name": "Email",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
    phone_number: list[PhoneNumber1] = field(
        default_factory=list,
        metadata={
            "name": "PhoneNumber",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
    hotel_rate_detail: list[HotelRateDetail] = field(
        default_factory=list,
        metadata={
            "name": "HotelRateDetail",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/hotel_v52_0",
            "min_occurs": 1,
            "max_occurs": 99,
        },
    )
    hotel_property: HotelProperty = field(
        metadata={
            "name": "HotelProperty",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/hotel_v52_0",
            "required": True,
        }
    )
    third_party_information: None | ThirdPartyInformation1 = field(
        default=None,
        metadata={
            "name": "ThirdPartyInformation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        },
    )
    hotel_stay: HotelStay = field(
        metadata={
            "name": "HotelStay",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/hotel_v52_0",
            "required": True,
        }
    )
    guarantee: None | Guarantee1 = field(
        default=None,
        metadata={
            "name": "Guarantee",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        },
    )
    hotel_special_request: None | HotelSpecialRequest = field(
        default=None,
        metadata={
            "name": "HotelSpecialRequest",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/hotel_v52_0",
        },
    )
    point_of_sale: None | PointOfSale1 = field(
        default=None,
        metadata={
            "name": "PointOfSale",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        },
    )
    promotion_code: None | PromotionCode = field(
        default=None,
        metadata={
            "name": "PromotionCode",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/hotel_v52_0",
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
    hotel_bedding: list[HotelBedding] = field(
        default_factory=list,
        metadata={
            "name": "HotelBedding",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/hotel_v52_0",
            "max_occurs": 4,
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
            "max_occurs": 9999,
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
    action_status: None | ActionStatus1 = field(
        default=None,
        metadata={
            "name": "ActionStatus",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        },
    )
    host_token: None | HostToken1 = field(
        default=None,
        metadata={
            "name": "HostToken",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        },
    )
    review_booking: list[ReviewBooking1] = field(
        default_factory=list,
        metadata={
            "name": "ReviewBooking",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 9999,
        },
    )
    hotel_commission: None | HotelCommission = field(
        default=None,
        metadata={
            "name": "HotelCommission",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/hotel_v52_0",
        },
    )
    user_acceptance: bool = field(
        default=False,
        metadata={
            "name": "UserAcceptance",
            "type": "Attribute",
        },
    )
    mandatory_rate_match: bool = field(
        default=False,
        metadata={
            "name": "MandatoryRateMatch",
            "type": "Attribute",
        },
    )
    status_code: None | str = field(
        default=None,
        metadata={
            "name": "StatusCode",
            "type": "Attribute",
            "length": 2,
            "white_space": "collapse",
        },
    )
    booking_confirmation: None | str = field(
        default=None,
        metadata={
            "name": "BookingConfirmation",
            "type": "Attribute",
            "max_length": 32,
        },
    )
