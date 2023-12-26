from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.air_pricing_info import AirPricingInfo
from travelport.models.fare_note import FareNote
from travelport.models.fee_info import FeeInfo
from travelport.models.tax_info import TaxInfo
from travelport.models.type_result_message_1 import TypeResultMessage1

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class AirPricePoint:
    """
    The container which holds the Non Solutioned result.

    Parameters
    ----------
    air_pricing_info
    air_pricing_result_message
    fee_info
        Supported by ACH only
    fare_note
    tax_info
        Itinerary level taxes
    key
    total_price
        The total price for this entity including base price and all taxes.
    base_price
        Represents the base price for this entity. This does not include any
        taxes or surcharges.
    approximate_total_price
        The Converted total price in Default Currency for this entity
        including base price and all taxes.
    approximate_base_price
        The Converted base price in Default Currency for this entity. This
        does not include any taxes or surcharges.
    equivalent_base_price
        Represents the base price in the related currency for this entity.
        This does not include any taxes or surcharges.
    taxes
        The aggregated amount of all the taxes that are associated with this
        entity. See the associated TaxInfo array for a breakdown of the
        individual taxes.
    fees
        The aggregated amount of all the fees that are associated with this
        entity. See the associated FeeInfo array for a breakdown of the
        individual fees.
    services
        The total cost for all optional services.
    approximate_taxes
        The Converted tax amount in Default Currency.
    approximate_fees
        The Converted fee amount in Default Currency.
    complete_itinerary
        This attribute is used to return whether complete Itinerary is
        present in the AirPricePoint structure or not. If set to true means
        AirPricePoint contains the result for full requested itinerary.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    air_pricing_info: list[AirPricingInfo] = field(
        default_factory=list,
        metadata={
            "name": "AirPricingInfo",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    air_pricing_result_message: list[TypeResultMessage1] = field(
        default_factory=list,
        metadata={
            "name": "AirPricingResultMessage",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    fee_info: list[FeeInfo] = field(
        default_factory=list,
        metadata={
            "name": "FeeInfo",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    fare_note: list[FareNote] = field(
        default_factory=list,
        metadata={
            "name": "FareNote",
            "type": "Element",
            "max_occurs": 99,
        },
    )
    tax_info: list[TaxInfo] = field(
        default_factory=list,
        metadata={
            "name": "TaxInfo",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        },
    )
    total_price: None | str = field(
        default=None,
        metadata={
            "name": "TotalPrice",
            "type": "Attribute",
        },
    )
    base_price: None | str = field(
        default=None,
        metadata={
            "name": "BasePrice",
            "type": "Attribute",
        },
    )
    approximate_total_price: None | str = field(
        default=None,
        metadata={
            "name": "ApproximateTotalPrice",
            "type": "Attribute",
        },
    )
    approximate_base_price: None | str = field(
        default=None,
        metadata={
            "name": "ApproximateBasePrice",
            "type": "Attribute",
        },
    )
    equivalent_base_price: None | str = field(
        default=None,
        metadata={
            "name": "EquivalentBasePrice",
            "type": "Attribute",
        },
    )
    taxes: None | str = field(
        default=None,
        metadata={
            "name": "Taxes",
            "type": "Attribute",
        },
    )
    fees: None | str = field(
        default=None,
        metadata={
            "name": "Fees",
            "type": "Attribute",
        },
    )
    services: None | str = field(
        default=None,
        metadata={
            "name": "Services",
            "type": "Attribute",
        },
    )
    approximate_taxes: None | str = field(
        default=None,
        metadata={
            "name": "ApproximateTaxes",
            "type": "Attribute",
        },
    )
    approximate_fees: None | str = field(
        default=None,
        metadata={
            "name": "ApproximateFees",
            "type": "Attribute",
        },
    )
    complete_itinerary: bool = field(
        default=True,
        metadata={
            "name": "CompleteItinerary",
            "type": "Attribute",
        },
    )
