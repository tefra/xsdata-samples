from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.air_pricing_payment import AirPricingPayment
from travelport.models.air_pricing_ticketing_modifiers import AirPricingTicketingModifiers
from travelport.models.associated_remark_1 import AssociatedRemark1
from travelport.models.credit_card_auth_1 import CreditCardAuth1
from travelport.models.loyalty_card_1 import LoyaltyCard1
from travelport.models.ssr_1 import Ssr1
from travelport.models.travel_compliance_data_1 import TravelComplianceData1

__NAMESPACE__ = "http://www.travelport.com/schema/sharedBooking_v52_0"


@dataclass
class AddAirPnrElement:
    """
    Container for PNR elements to be added.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/sharedBooking_v52_0"

    air_pricing_payment: list[AirPricingPayment] = field(
        default_factory=list,
        metadata={
            "name": "AirPricingPayment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "max_occurs": 30,
        }
    )
    associated_remark: list[AssociatedRemark1] = field(
        default_factory=list,
        metadata={
            "name": "AssociatedRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "max_occurs": 99,
        }
    )
    air_pricing_ticketing_modifiers: list[AirPricingTicketingModifiers] = field(
        default_factory=list,
        metadata={
            "name": "AirPricingTicketingModifiers",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "max_occurs": 99,
        }
    )
    credit_card_auth: list[CreditCardAuth1] = field(
        default_factory=list,
        metadata={
            "name": "CreditCardAuth",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 99,
        }
    )
    ssr: list[Ssr1] = field(
        default_factory=list,
        metadata={
            "name": "SSR",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 99,
        }
    )
    loyalty_card: list[LoyaltyCard1] = field(
        default_factory=list,
        metadata={
            "name": "LoyaltyCard",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 99,
        }
    )
    travel_compliance_data: list[TravelComplianceData1] = field(
        default_factory=list,
        metadata={
            "name": "TravelComplianceData",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 99,
        }
    )
    booking_traveler_ref: None | str = field(
        default=None,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Attribute",
        }
    )
