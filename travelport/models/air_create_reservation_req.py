from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

from travelport.models.action_status_1 import ActionStatus1
from travelport.models.air_create_reservation_req_check_price_variance_type import (
    AirCreateReservationReqCheckPriceVarianceType,
)
from travelport.models.air_pricing_solution import AirPricingSolution
from travelport.models.air_pricing_ticketing_modifiers import (
    AirPricingTicketingModifiers,
)
from travelport.models.associated_remark_1 import AssociatedRemark1
from travelport.models.auto_seat_assignment import AutoSeatAssignment
from travelport.models.base_create_with_form_of_payment_req_1 import (
    BaseCreateWithFormOfPaymentReq1,
)
from travelport.models.delivery_info_1 import DeliveryInfo1
from travelport.models.payment_1 import Payment1
from travelport.models.pocket_itinerary_remark import PocketItineraryRemark
from travelport.models.point_of_sale_1 import PointOfSale1
from travelport.models.review_booking_1 import ReviewBooking1
from travelport.models.specific_seat_assignment import SpecificSeatAssignment
from travelport.models.supplier_locator_1 import SupplierLocator1
from travelport.models.third_party_information_1 import ThirdPartyInformation1
from travelport.models.type_retain_reservation import TypeRetainReservation

__NAMESPACE__ = "http://www.travelport.com/schema/universal_v52_0"


@dataclass
class AirCreateReservationReq(BaseCreateWithFormOfPaymentReq1):
    """
    Request to store an air itinerary and create initial PNR.

    Parameters
    ----------
    supplier_locator
        Provider: 1G,1V,1P,ACH,SDK.
    third_party_information
        Provider: SDK.
    point_of_sale
        Provider: 1G,1V.
    air_pricing_solution
        Provider: 1G,1V,1P,ACH,SDK. SplitReservation can include up 16
        AirPricingSolutions.
    action_status
        Provider: 1G,1V,1P,ACH,SDK.
    payment
        Provider: 1G,1V,1P,ACH.
    delivery_info
        Provider: ACH.
    auto_seat_assignment
        Provider: 1G,1V,1P.
    specific_seat_assignment
        Provider: 1G,1V,1P,ACH.
    associated_remark
        Provider: 1G,1V,1P,ACH,SDK.
    pocket_itinerary_remark
        Provider: 1P.
    review_booking
        Provider: 1G,1V-Review Booking or Queue Minders is to add the
        reminders in the Provider Reservation along with the date time and
        Queue details. On the date time defined in reminders, the message
        along with the PNR goes to the desired Queue.
    air_pricing_ticketing_modifiers
        AirPricing TicketingModifier information used to associate Ticketing
        Modifiers with one or more AirPricingInfos/ProviderReservationInfo
        for 1G,1V,1P
    retain_reservation
        Provider: 1G,1V,1P
    source
    override_mct
        Provider: 1G,1V.
    restrict_waitlist
        Restrict Book if it sells a Waitlisted AirSegment. Provider: 1G,1V
    create_passive_for_hold
        Creates a background passive segment for an ACH hold booking.
    channel_id
        A Channel ID is 4 alpha-numeric characters used to activate the
        Search Control Console filter for a specific group of travelers
        being served by the agency credential.
    nscc
        Allows the agency to bypass/override the Search Control Console
        rule.
    check_price_variance_type
        Valid values are "Amount" (default) or "Percentage".
    check_price_variance_value
        Price variance tolerance in currency or percentage. Booking allowed
        if Price Difference ≤ Price Variance.
    split_reservation
        Creates multi host PNRs per AirPricingSolution if true,Creates
        single host PNR if false or not included in the request.
    prefer_complete_itinerary
        Applicable only for book requests with multiple AirPricingSolutions.
        True – Cancel the booking request if there is a booking failure for
        one of the AirPricingSolutions. False – Continue booking other
        AirPricingSolutions even if there is a booking failure.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    supplier_locator: list[SupplierLocator1] = field(
        default_factory=list,
        metadata={
            "name": "SupplierLocator",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
    third_party_information: list[ThirdPartyInformation1] = field(
        default_factory=list,
        metadata={
            "name": "ThirdPartyInformation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
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
    air_pricing_solution: list[AirPricingSolution] = field(
        default_factory=list,
        metadata={
            "name": "AirPricingSolution",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "min_occurs": 1,
            "max_occurs": 16,
        },
    )
    action_status: list[ActionStatus1] = field(
        default_factory=list,
        metadata={
            "name": "ActionStatus",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
    payment: list[Payment1] = field(
        default_factory=list,
        metadata={
            "name": "Payment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
    delivery_info: None | DeliveryInfo1 = field(
        default=None,
        metadata={
            "name": "DeliveryInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        },
    )
    auto_seat_assignment: list[AutoSeatAssignment] = field(
        default_factory=list,
        metadata={
            "name": "AutoSeatAssignment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "max_occurs": 999,
        },
    )
    specific_seat_assignment: list[SpecificSeatAssignment] = field(
        default_factory=list,
        metadata={
            "name": "SpecificSeatAssignment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "max_occurs": 999,
        },
    )
    associated_remark: list[AssociatedRemark1] = field(
        default_factory=list,
        metadata={
            "name": "AssociatedRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "max_occurs": 999,
        },
    )
    pocket_itinerary_remark: list[PocketItineraryRemark] = field(
        default_factory=list,
        metadata={
            "name": "PocketItineraryRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "max_occurs": 999,
        },
    )
    review_booking: list[ReviewBooking1] = field(
        default_factory=list,
        metadata={
            "name": "ReviewBooking",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
    air_pricing_ticketing_modifiers: list[AirPricingTicketingModifiers] = (
        field(
            default_factory=list,
            metadata={
                "name": "AirPricingTicketingModifiers",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v52_0",
                "max_occurs": 99,
            },
        )
    )
    retain_reservation: TypeRetainReservation = field(
        default=TypeRetainReservation.NONE,
        metadata={
            "name": "RetainReservation",
            "type": "Attribute",
        },
    )
    source: None | str = field(
        default=None,
        metadata={
            "name": "Source",
            "type": "Attribute",
            "max_length": 50,
        },
    )
    override_mct: bool = field(
        default=False,
        metadata={
            "name": "OverrideMCT",
            "type": "Attribute",
        },
    )
    restrict_waitlist: bool = field(
        default=False,
        metadata={
            "name": "RestrictWaitlist",
            "type": "Attribute",
        },
    )
    create_passive_for_hold: bool = field(
        default=False,
        metadata={
            "name": "CreatePassiveForHold",
            "type": "Attribute",
        },
    )
    channel_id: None | str = field(
        default=None,
        metadata={
            "name": "ChannelId",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 4,
        },
    )
    nscc: None | str = field(
        default=None,
        metadata={
            "name": "NSCC",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 3,
        },
    )
    check_price_variance_type: AirCreateReservationReqCheckPriceVarianceType = field(
        default=AirCreateReservationReqCheckPriceVarianceType.AMOUNT,
        metadata={
            "name": "CheckPriceVarianceType",
            "type": "Attribute",
        },
    )
    check_price_variance_value: Decimal = field(
        default=Decimal("0.0"),
        metadata={
            "name": "CheckPriceVarianceValue",
            "type": "Attribute",
        },
    )
    split_reservation: bool = field(
        default=False,
        metadata={
            "name": "SplitReservation",
            "type": "Attribute",
        },
    )
    prefer_complete_itinerary: bool = field(
        default=True,
        metadata={
            "name": "PreferCompleteItinerary",
            "type": "Attribute",
        },
    )
