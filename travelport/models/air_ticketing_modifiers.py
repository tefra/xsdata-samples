from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.air_pricing_info_ref import AirPricingInfoRef
from travelport.models.commission_1 import Commission1
from travelport.models.credit_card_auth_1 import CreditCardAuth1
from travelport.models.document_modifiers import DocumentModifiers
from travelport.models.form_of_payment_1 import FormOfPayment1
from travelport.models.payment_1 import Payment1
from travelport.models.ticket_endorsement import TicketEndorsement
from travelport.models.tour_code import TourCode

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class AirTicketingModifiers:
    """
    Modifiers used during ticketing.

    Parameters
    ----------
    document_modifiers
    air_pricing_info_ref
    tour_code
        Allows an agency to modify the tour code information during ticket
        issuance. Providers supported: Worldspan.
    ticket_endorsement
        Allows an agency to add user defined ticketing endorsements in the
        ticket. Providers supported: Worldspan.
    commission
        Allows an agency to add the commission to a new or different
        commission rate which will be applied at time of ticketing. The
        commission Modifier allows the user specify how the commission
        change is to applied. Providers supported: Worldspan.
    form_of_payment
        FormOfPayment information to be used as ticketing modifier at the
        time of ticketing. Providers supported: Galileo, Apollo, Worldspan.
    credit_card_auth
        CreditCardAuth information to be used as ticketing modifier at the
        time of ticketing. Providers supported: Galileo, Apollo, Worldspan.
    payment
        Provide Payment for FOP. Providers supported: Galileo, Apollo,
        Worldspan.
    plating_carrier
        The Plating Carrier used for this ticket
    ticketed_fare_override
        It is a modifier to allow re-issuance of tickets for stored fares
        which are already ticketed. Providers supported are 1P
    suppress_tax_and_fee
        Allow to suppress Taxand Fee in ticketing response.Providers
        supported: Worldspan.
    no_comparison_sfq
        1P - Set to "true" to include the no comparison overide #NC to
        override the existing SFQ and issue the ticket. Only valid for
        AirTicketingReq, not valid  for AirExchangeTicketingReq.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    document_modifiers: None | DocumentModifiers = field(
        default=None,
        metadata={
            "name": "DocumentModifiers",
            "type": "Element",
        },
    )
    air_pricing_info_ref: list[AirPricingInfoRef] = field(
        default_factory=list,
        metadata={
            "name": "AirPricingInfoRef",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    tour_code: None | TourCode = field(
        default=None,
        metadata={
            "name": "TourCode",
            "type": "Element",
        },
    )
    ticket_endorsement: list[TicketEndorsement] = field(
        default_factory=list,
        metadata={
            "name": "TicketEndorsement",
            "type": "Element",
            "max_occurs": 3,
        },
    )
    commission: None | Commission1 = field(
        default=None,
        metadata={
            "name": "Commission",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        },
    )
    form_of_payment: list[FormOfPayment1] = field(
        default_factory=list,
        metadata={
            "name": "FormOfPayment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
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
    payment: list[Payment1] = field(
        default_factory=list,
        metadata={
            "name": "Payment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
    plating_carrier: None | str = field(
        default=None,
        metadata={
            "name": "PlatingCarrier",
            "type": "Attribute",
            "length": 2,
        },
    )
    ticketed_fare_override: bool = field(
        default=False,
        metadata={
            "name": "TicketedFareOverride",
            "type": "Attribute",
        },
    )
    suppress_tax_and_fee: bool = field(
        default=False,
        metadata={
            "name": "SuppressTaxAndFee",
            "type": "Attribute",
        },
    )
    no_comparison_sfq: bool = field(
        default=False,
        metadata={
            "name": "NoComparisonSFQ",
            "type": "Attribute",
        },
    )
