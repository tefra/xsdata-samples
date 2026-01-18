from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.accounting_remark_1 import AccountingRemark1
from travelport.models.air_pricing_info import AirPricingInfo
from travelport.models.air_pricing_payment import AirPricingPayment
from travelport.models.air_pricing_ticketing_modifiers import (
    AirPricingTicketingModifiers,
)
from travelport.models.air_segment import AirSegment
from travelport.models.air_segment_pricing_modifiers import (
    AirSegmentPricingModifiers,
)
from travelport.models.associated_remark_1 import AssociatedRemark1
from travelport.models.auto_seat_assignment import AutoSeatAssignment
from travelport.models.brand_info import BrandInfo
from travelport.models.credit_card_auth_1 import CreditCardAuth1
from travelport.models.delivery_info_1 import DeliveryInfo1
from travelport.models.fee_info import FeeInfo
from travelport.models.general_remark_1 import GeneralRemark1
from travelport.models.host_token_1 import HostToken1
from travelport.models.involuntary_change import InvoluntaryChange
from travelport.models.loyalty_card_1 import LoyaltyCard1
from travelport.models.optional_services_info import OptionalServicesInfo
from travelport.models.payment_1 import Payment1
from travelport.models.pocket_itinerary_remark import PocketItineraryRemark
from travelport.models.specific_seat_assignment import SpecificSeatAssignment
from travelport.models.ssr_1 import Ssr1
from travelport.models.supplier_locator_1 import SupplierLocator1
from travelport.models.third_party_information_1 import ThirdPartyInformation1
from travelport.models.travel_compliance_data_1 import TravelComplianceData1

__NAMESPACE__ = "http://www.travelport.com/schema/universal_v52_0"


@dataclass(kw_only=True)
class AirAdd:
    """
    Parameters
    ----------
    accounting_remark
    supplier_locator
    air_segment
    air_pricing_info
    credit_card_auth
    delivery_info
    payment
    ssr
    loyalty_card
    auto_seat_assignment
    specific_seat_assignment
    general_remark
    fee_info
    host_token
    air_pricing_ticketing_modifiers
    optional_services_info
    air_pricing_payment
    associated_remark
    pocket_itinerary_remark
    third_party_information
    air_segment_pricing_modifiers
    travel_compliance_data
    brand_info
    involuntary_change
    reservation_locator_code
    booking_traveler_ref
    restrict_waitlist
        Restrict Update if it sells a Waitlisted AirSegment. Provider:
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
            "max_occurs": 99,
        },
    )
    supplier_locator: list[SupplierLocator1] = field(
        default_factory=list,
        metadata={
            "name": "SupplierLocator",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 99,
        },
    )
    air_segment: list[AirSegment] = field(
        default_factory=list,
        metadata={
            "name": "AirSegment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "max_occurs": 99,
        },
    )
    air_pricing_info: list[AirPricingInfo] = field(
        default_factory=list,
        metadata={
            "name": "AirPricingInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "max_occurs": 99,
        },
    )
    credit_card_auth: list[CreditCardAuth1] = field(
        default_factory=list,
        metadata={
            "name": "CreditCardAuth",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 99,
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
    payment: list[Payment1] = field(
        default_factory=list,
        metadata={
            "name": "Payment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 99,
        },
    )
    ssr: list[Ssr1] = field(
        default_factory=list,
        metadata={
            "name": "SSR",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
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
            "max_occurs": 99,
        },
    )
    general_remark: list[GeneralRemark1] = field(
        default_factory=list,
        metadata={
            "name": "GeneralRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 99,
        },
    )
    fee_info: list[FeeInfo] = field(
        default_factory=list,
        metadata={
            "name": "FeeInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "max_occurs": 99,
        },
    )
    host_token: list[HostToken1] = field(
        default_factory=list,
        metadata={
            "name": "HostToken",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 99,
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
    optional_services_info: None | OptionalServicesInfo = field(
        default=None,
        metadata={
            "name": "OptionalServicesInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
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
            "max_occurs": 99,
        },
    )
    pocket_itinerary_remark: list[PocketItineraryRemark] = field(
        default_factory=list,
        metadata={
            "name": "PocketItineraryRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "max_occurs": 99,
        },
    )
    third_party_information: list[ThirdPartyInformation1] = field(
        default_factory=list,
        metadata={
            "name": "ThirdPartyInformation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 99,
        },
    )
    air_segment_pricing_modifiers: list[AirSegmentPricingModifiers] = field(
        default_factory=list,
        metadata={
            "name": "AirSegmentPricingModifiers",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "max_occurs": 99,
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
    brand_info: list[BrandInfo] = field(
        default_factory=list,
        metadata={
            "name": "BrandInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "max_occurs": 99,
        },
    )
    involuntary_change: None | InvoluntaryChange = field(
        default=None,
        metadata={
            "name": "InvoluntaryChange",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
        },
    )
    reservation_locator_code: str = field(
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
        },
    )
    restrict_waitlist: bool = field(
        default=False,
        metadata={
            "name": "RestrictWaitlist",
            "type": "Attribute",
        },
    )
