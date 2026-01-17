from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

from xsdata.models.datatype import XmlDate

from travelport.models.type_form_of_refund import TypeFormOfRefund
from travelport.models.type_itinerary_code import TypeItineraryCode
from travelport.models.type_pricing_type import TypePricingType

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class PricingDetails:
    """
    Used for rapid reprice.

    This is a response element. Additional information about how pricing
    was obtain, messages, etc. Providers: 1G/1V/1P/1S/1A.

    Parameters
    ----------
    advisory_message
        Advisory messages returned from the host.
    endorsement_text
        Endorsement text returned from the host.
    waiver_text
        Waiver text returned from the host.
    low_fare_pricing
        This tells if Low Fare Finder was used.
    low_fare_found
        This tells if the lowest fare was found.
    penalty_applies
        This tells if penalties apply.
    discount_applies
        This tells if a discount applies.
    itinerary_type
        Values allowed are International or Domestic. This tells if the
        itinerary is international or domestic.
    validating_vendor_code
        The vendor code of the validating carrier.
    for_ticketing_on_date
        The ticketing date of the itinerary.
    last_date_to_ticket
        The last date to issue the ticket.
    form_of_refund
        How the refund will be issued. Values will be MCO or FormOfPayment
    account_code
    bankers_selling_rate
        The selling rate at time of quote.
    pricing_type
        Ties with the RepricingModifiers sent in the request and tells how
        the itinerary was priced.
    conversion_rate
        The conversion rate at the time of quote.
    rate_of_exchange
        The exchange rate at time of quote.
    original_ticket_currency
        The currency of the original ticket.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    advisory_message: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdvisoryMessage",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    endorsement_text: list[str] = field(
        default_factory=list,
        metadata={
            "name": "EndorsementText",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    waiver_text: None | str = field(
        default=None,
        metadata={
            "name": "WaiverText",
            "type": "Element",
        },
    )
    low_fare_pricing: bool = field(
        default=False,
        metadata={
            "name": "LowFarePricing",
            "type": "Attribute",
        },
    )
    low_fare_found: bool = field(
        default=False,
        metadata={
            "name": "LowFareFound",
            "type": "Attribute",
        },
    )
    penalty_applies: bool = field(
        default=False,
        metadata={
            "name": "PenaltyApplies",
            "type": "Attribute",
        },
    )
    discount_applies: bool = field(
        default=False,
        metadata={
            "name": "DiscountApplies",
            "type": "Attribute",
        },
    )
    itinerary_type: None | TypeItineraryCode = field(
        default=None,
        metadata={
            "name": "ItineraryType",
            "type": "Attribute",
        },
    )
    validating_vendor_code: None | str = field(
        default=None,
        metadata={
            "name": "ValidatingVendorCode",
            "type": "Attribute",
            "length": 2,
        },
    )
    for_ticketing_on_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "ForTicketingOnDate",
            "type": "Attribute",
        },
    )
    last_date_to_ticket: None | XmlDate = field(
        default=None,
        metadata={
            "name": "LastDateToTicket",
            "type": "Attribute",
        },
    )
    form_of_refund: None | TypeFormOfRefund = field(
        default=None,
        metadata={
            "name": "FormOfRefund",
            "type": "Attribute",
        },
    )
    account_code: None | str = field(
        default=None,
        metadata={
            "name": "AccountCode",
            "type": "Attribute",
        },
    )
    bankers_selling_rate: None | Decimal = field(
        default=None,
        metadata={
            "name": "BankersSellingRate",
            "type": "Attribute",
        },
    )
    pricing_type: None | TypePricingType = field(
        default=None,
        metadata={
            "name": "PricingType",
            "type": "Attribute",
        },
    )
    conversion_rate: None | Decimal = field(
        default=None,
        metadata={
            "name": "ConversionRate",
            "type": "Attribute",
        },
    )
    rate_of_exchange: None | Decimal = field(
        default=None,
        metadata={
            "name": "RateOfExchange",
            "type": "Attribute",
        },
    )
    original_ticket_currency: None | str = field(
        default=None,
        metadata={
            "name": "OriginalTicketCurrency",
            "type": "Attribute",
            "length": 3,
        },
    )
