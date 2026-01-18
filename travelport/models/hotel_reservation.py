from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.associated_remark_3 import AssociatedRemark3
from travelport.models.base_reservation_1 import BaseReservation1
from travelport.models.booking_source_1 import BookingSource1
from travelport.models.booking_traveler_ref_1 import BookingTravelerRef1
from travelport.models.cancel_info import CancelInfo
from travelport.models.email_1 import Email1
from travelport.models.guarantee_1 import Guarantee1
from travelport.models.guest_information import GuestInformation
from travelport.models.hotel_bedding import HotelBedding
from travelport.models.hotel_commission import HotelCommission
from travelport.models.hotel_detail_item import HotelDetailItem
from travelport.models.hotel_property import HotelProperty
from travelport.models.hotel_rate_detail import HotelRateDetail
from travelport.models.hotel_special_request import HotelSpecialRequest
from travelport.models.hotel_stay import HotelStay
from travelport.models.phone_number_1 import PhoneNumber1
from travelport.models.promotion_code import PromotionCode
from travelport.models.reservation_name_1 import ReservationName1
from travelport.models.sell_message_1 import SellMessage1
from travelport.models.third_party_information_1 import ThirdPartyInformation1
from travelport.models.type_adapted_room_guest_allocation import (
    TypeAdaptedRoomGuestAllocation,
)
from travelport.models.type_hotel_rate_description import (
    TypeHotelRateDescription,
)

__NAMESPACE__ = "http://www.travelport.com/schema/hotel_v52_0"


@dataclass(kw_only=True)
class HotelReservation(BaseReservation1):
    """
    The complete Hotel Reservation.

    Parameters
    ----------
    booking_traveler_ref
    reservation_name
    third_party_information
    email
    phone_number
    hotel_property
    hotel_rate_detail
    hotel_stay
    hotel_special_request
    guarantee
    promotion_code
        Specifies promotional code used in hotel booking
    booking_source
        Specify alternate booking source
    hotel_bedding
    guest_information
    associated_remark
    sell_message
    hotel_commission
        HotelCommission text indicates commision while hotel reservation.
        Provider supported 1P.
    cancel_info
    total_reservation_price
        The total price for the entire stay, including fees, for all rooms
        in the booking.
    hotel_detail_item
    adapted_room_guest_allocation
        This element defines how the aggregators or hotel property have
        allocated the guests to the rooms. Only displayed when Requested
        guest allocation is different from the Adapted room guest
        allocation.
    status
        Reservation IATA status code, 2 byte.
    booking_confirmation
    cancel_confirmation
    provider_reservation_info_ref
        Provider reservation reference key.
    travel_order
        To identify the appropriate sequence for Air/Car/Hotel segments
        based on travel dates.
    provider_segment_order
        To identify the appropriate travel sequence for Air/Car/Hotel/Rail
        segments/reservations in the provider reservation.
    passive_provider_reservation_info_ref
        Passive Provider reservation reference key.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    booking_traveler_ref: list[BookingTravelerRef1] = field(
        default_factory=list,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
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
    third_party_information: None | ThirdPartyInformation1 = field(
        default=None,
        metadata={
            "name": "ThirdPartyInformation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        },
    )
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
    hotel_property: HotelProperty = field(
        metadata={
            "name": "HotelProperty",
            "type": "Element",
            "required": True,
        }
    )
    hotel_rate_detail: list[HotelRateDetail] = field(
        default_factory=list,
        metadata={
            "name": "HotelRateDetail",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 99,
        },
    )
    hotel_stay: HotelStay = field(
        metadata={
            "name": "HotelStay",
            "type": "Element",
            "required": True,
        }
    )
    hotel_special_request: None | HotelSpecialRequest = field(
        default=None,
        metadata={
            "name": "HotelSpecialRequest",
            "type": "Element",
        },
    )
    guarantee: None | Guarantee1 = field(
        default=None,
        metadata={
            "name": "Guarantee",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        },
    )
    promotion_code: None | PromotionCode = field(
        default=None,
        metadata={
            "name": "PromotionCode",
            "type": "Element",
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
            "max_occurs": 4,
        },
    )
    guest_information: None | GuestInformation = field(
        default=None,
        metadata={
            "name": "GuestInformation",
            "type": "Element",
        },
    )
    associated_remark: list[AssociatedRemark3] = field(
        default_factory=list,
        metadata={
            "name": "AssociatedRemark",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    sell_message: list[SellMessage1] = field(
        default_factory=list,
        metadata={
            "name": "SellMessage",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
    hotel_commission: None | HotelCommission = field(
        default=None,
        metadata={
            "name": "HotelCommission",
            "type": "Element",
        },
    )
    cancel_info: None | CancelInfo = field(
        default=None,
        metadata={
            "name": "CancelInfo",
            "type": "Element",
        },
    )
    total_reservation_price: None | HotelReservation.TotalReservationPrice = (
        field(
            default=None,
            metadata={
                "name": "TotalReservationPrice",
                "type": "Element",
            },
        )
    )
    hotel_detail_item: list[HotelDetailItem] = field(
        default_factory=list,
        metadata={
            "name": "HotelDetailItem",
            "type": "Element",
            "max_occurs": 99,
        },
    )
    adapted_room_guest_allocation: (
        None | HotelReservation.AdaptedRoomGuestAllocation
    ) = field(
        default=None,
        metadata={
            "name": "AdaptedRoomGuestAllocation",
            "type": "Element",
        },
    )
    status: str = field(
        metadata={
            "name": "Status",
            "type": "Attribute",
            "required": True,
        }
    )
    booking_confirmation: None | str = field(
        default=None,
        metadata={
            "name": "BookingConfirmation",
            "type": "Attribute",
        },
    )
    cancel_confirmation: None | str = field(
        default=None,
        metadata={
            "name": "CancelConfirmation",
            "type": "Attribute",
        },
    )
    provider_reservation_info_ref: None | str = field(
        default=None,
        metadata={
            "name": "ProviderReservationInfoRef",
            "type": "Attribute",
        },
    )
    travel_order: None | int = field(
        default=None,
        metadata={
            "name": "TravelOrder",
            "type": "Attribute",
        },
    )
    provider_segment_order: None | int = field(
        default=None,
        metadata={
            "name": "ProviderSegmentOrder",
            "type": "Attribute",
            "max_inclusive": 999,
        },
    )
    passive_provider_reservation_info_ref: None | str = field(
        default=None,
        metadata={
            "name": "PassiveProviderReservationInfoRef",
            "type": "Attribute",
        },
    )

    @dataclass(kw_only=True)
    class TotalReservationPrice:
        """
        Parameters
        ----------
        room_rate_description
        total_price
            The amount of the total price, including fees for all rooms in
            the booking.
        approx_total_price
            The approximate amount of the total hotel price, including fees,
            in another currency.
        """

        room_rate_description: list[TypeHotelRateDescription] = field(
            default_factory=list,
            metadata={
                "name": "RoomRateDescription",
                "type": "Element",
                "max_occurs": 99,
            },
        )
        total_price: None | str = field(
            default=None,
            metadata={
                "name": "TotalPrice",
                "type": "Attribute",
            },
        )
        approx_total_price: None | str = field(
            default=None,
            metadata={
                "name": "ApproxTotalPrice",
                "type": "Attribute",
            },
        )

    @dataclass(kw_only=True)
    class AdaptedRoomGuestAllocation:
        """
        Parameters
        ----------
        room
            Individual room. Multiple occurrences if there are multiple
            rooms in the request. Maximum number of rooms may vary by
            supplier or aggregator.
        """

        room: list[TypeAdaptedRoomGuestAllocation] = field(
            default_factory=list,
            metadata={
                "name": "Room",
                "type": "Element",
                "min_occurs": 1,
                "max_occurs": 9,
            },
        )
