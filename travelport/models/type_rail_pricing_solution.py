from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.rail_journey import RailJourney
from travelport.models.rail_journey_ref import RailJourneyRef
from travelport.models.rail_pricing_info import RailPricingInfo

__NAMESPACE__ = "http://www.travelport.com/schema/rail_v52_0"


@dataclass
class TypeRailPricingSolution:
    """
    Common RailPricingSolution container.

    Parameters
    ----------
    rail_journey
    rail_journey_ref
    rail_pricing_info
    key
    offer_id
        OfferID must be included if the RailCreateReq contains a price.  If
        the RailCreateReq is used for the Direct Book function, the OfferID
        is not included.
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
    provider_code
    supplier_code
    host_token_ref
        HostTokenRef will reference the value in HostTokenList/HostToken @
        Key
    reference
        Offer Reference required for Booking(eg.TL).
    """

    class Meta:
        name = "typeRailPricingSolution"

    rail_journey: list[RailJourney] = field(
        default_factory=list,
        metadata={
            "name": "RailJourney",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/rail_v52_0",
            "max_occurs": 999,
        },
    )
    rail_journey_ref: list[RailJourneyRef] = field(
        default_factory=list,
        metadata={
            "name": "RailJourneyRef",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/rail_v52_0",
            "max_occurs": 999,
        },
    )
    rail_pricing_info: list[RailPricingInfo] = field(
        default_factory=list,
        metadata={
            "name": "RailPricingInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/rail_v52_0",
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
    offer_id: None | int = field(
        default=None,
        metadata={
            "name": "OfferId",
            "type": "Attribute",
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
    provider_code: None | str = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "required": True,
            "min_length": 2,
            "max_length": 5,
        },
    )
    supplier_code: None | str = field(
        default=None,
        metadata={
            "name": "SupplierCode",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 5,
        },
    )
    host_token_ref: None | str = field(
        default=None,
        metadata={
            "name": "HostTokenRef",
            "type": "Attribute",
        },
    )
    reference: None | str = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Attribute",
        },
    )
