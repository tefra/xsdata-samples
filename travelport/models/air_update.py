from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.accounting_remark_1 import AccountingRemark1
from travelport.models.air_pricing_adjustment import AirPricingAdjustment
from travelport.models.air_pricing_payment import AirPricingPayment
from travelport.models.air_pricing_ticketing_modifiers import (
    AirPricingTicketingModifiers,
)
from travelport.models.air_segment import AirSegment
from travelport.models.air_segment_special_update import (
    AirSegmentSpecialUpdate,
)
from travelport.models.associated_remark_1 import AssociatedRemark1
from travelport.models.auto_seat_assignment import AutoSeatAssignment
from travelport.models.credit_card_auth_1 import CreditCardAuth1
from travelport.models.delivery_info_1 import DeliveryInfo1
from travelport.models.general_remark_1 import GeneralRemark1
from travelport.models.loyalty_card_1 import LoyaltyCard1
from travelport.models.optional_services_info import OptionalServicesInfo
from travelport.models.pocket_itinerary_remark import PocketItineraryRemark
from travelport.models.specific_seat_assignment import SpecificSeatAssignment
from travelport.models.ssr_1 import Ssr1
from travelport.models.third_party_information_1 import ThirdPartyInformation1
from travelport.models.travel_compliance_data_1 import TravelComplianceData1

__NAMESPACE__ = "http://www.travelport.com/schema/universal_v52_0"


@dataclass
class AirUpdate:
    """
    Parameters
    ----------
    accounting_remark
    air_segment
    credit_card_auth
    air_pricing_adjustment
    air_pricing_ticketing_modifiers
        Ticketing modifiers to be updated.
    delivery_info
    air_segment_special_update
    loyalty_card
    ssr
    general_remark
    auto_seat_assignment
    specific_seat_assignment
    air_pricing_payment
    associated_remark
    pocket_itinerary_remark
    optional_services_info
    third_party_information
    travel_compliance_data
    reservation_locator_code
    booking_traveler_ref
    restrict_waitlist
        Restrict Update if it modifies a Waitlisted AirSegment. Provider:
        1G,1V,1P
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    accounting_remark: list[AccountingRemark1] = field(
        default_factory=list,
        metadata={
            "name": "AccountingRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
    air_segment: list[AirSegment] = field(
        default_factory=list,
        metadata={
            "name": "AirSegment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "max_occurs": 999,
        },
    )
    credit_card_auth: list[CreditCardAuth1] = field(
        default_factory=list,
        metadata={
            "name": "CreditCardAuth",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
    air_pricing_adjustment: list[AirPricingAdjustment] = field(
        default_factory=list,
        metadata={
            "name": "AirPricingAdjustment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "max_occurs": 999,
        },
    )
    air_pricing_ticketing_modifiers: list[
        AirPricingTicketingModifiers
    ] = field(
        default_factory=list,
        metadata={
            "name": "AirPricingTicketingModifiers",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
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
    air_segment_special_update: None | AirSegmentSpecialUpdate = field(
        default=None,
        metadata={
            "name": "AirSegmentSpecialUpdate",
            "type": "Element",
        },
    )
    loyalty_card: list[LoyaltyCard1] = field(
        default_factory=list,
        metadata={
            "name": "LoyaltyCard",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
    ssr: list[Ssr1] = field(
        default_factory=list,
        metadata={
            "name": "SSR",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
    general_remark: list[GeneralRemark1] = field(
        default_factory=list,
        metadata={
            "name": "GeneralRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
    auto_seat_assignment: None | AutoSeatAssignment = field(
        default=None,
        metadata={
            "name": "AutoSeatAssignment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
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
    air_pricing_payment: None | AirPricingPayment = field(
        default=None,
        metadata={
            "name": "AirPricingPayment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
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
    optional_services_info: None | OptionalServicesInfo = field(
        default=None,
        metadata={
            "name": "OptionalServicesInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
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
    travel_compliance_data: list[TravelComplianceData1] = field(
        default_factory=list,
        metadata={
            "name": "TravelComplianceData",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
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
    restrict_waitlist: bool = field(
        default=False,
        metadata={
            "name": "RestrictWaitlist",
            "type": "Attribute",
        },
    )
