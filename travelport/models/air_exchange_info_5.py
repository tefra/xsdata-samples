from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_fare_pull_5 import TypeFarePull5
from travelport.models.type_fee_info_5 import TypeFeeInfo5
from travelport.models.type_tax_5 import TypeTax5
from travelport.models.type_tax_info_5 import TypeTaxInfo5

__NAMESPACE__ = "http://www.travelport.com/schema/common_v34_0"


@dataclass
class AirExchangeInfo5:
    """
    Provides results of a exchange quote.

    Parameters
    ----------
    total_penalty_tax_info
    paid_tax
    ticket_fee_info
        Used for rapid reprice. Providers: 1G/1V/1P/1S/1A
    reason
        Used for rapid reprice. The reason code or text is returned if the
        PricingTag is not equal to A, and explains why A was not returned.
        Providers: 1G/1V/1P/1S/1A
    fee_info
    tax_info
        Itinerary level taxes
    exchange_amount
    base_fare
    equivalent_base_fare
    taxes
    change_fee
    forfeit_amount
    refundable
    exchangeable
    first_class_upgrade
    ticket_by_date
    pricing_tag
    equivalent_change_fee
    equivalent_exchange_amount
    add_collection
    residual_value
    total_residual_value
    original_flight_value
    flown_segment_value
    bulk_ticket_advisory
    fare_pull
    refund
        Total refund amount.
    """

    class Meta:
        name = "AirExchangeInfo"
        namespace = "http://www.travelport.com/schema/common_v34_0"

    total_penalty_tax_info: None | AirExchangeInfo5.TotalPenaltyTaxInfo = (
        field(
            default=None,
            metadata={
                "name": "TotalPenaltyTaxInfo",
                "type": "Element",
            },
        )
    )
    paid_tax: list[TypeTax5] = field(
        default_factory=list,
        metadata={
            "name": "PaidTax",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    ticket_fee_info: list[AirExchangeInfo5.TicketFeeInfo] = field(
        default_factory=list,
        metadata={
            "name": "TicketFeeInfo",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    reason: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Reason",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    fee_info: list[TypeFeeInfo5] = field(
        default_factory=list,
        metadata={
            "name": "FeeInfo",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    tax_info: list[TypeTaxInfo5] = field(
        default_factory=list,
        metadata={
            "name": "TaxInfo",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    exchange_amount: None | str = field(
        default=None,
        metadata={
            "name": "ExchangeAmount",
            "type": "Attribute",
            "required": True,
        },
    )
    base_fare: None | str = field(
        default=None,
        metadata={
            "name": "BaseFare",
            "type": "Attribute",
        },
    )
    equivalent_base_fare: None | str = field(
        default=None,
        metadata={
            "name": "EquivalentBaseFare",
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
    change_fee: None | str = field(
        default=None,
        metadata={
            "name": "ChangeFee",
            "type": "Attribute",
        },
    )
    forfeit_amount: None | str = field(
        default=None,
        metadata={
            "name": "ForfeitAmount",
            "type": "Attribute",
        },
    )
    refundable: None | bool = field(
        default=None,
        metadata={
            "name": "Refundable",
            "type": "Attribute",
        },
    )
    exchangeable: None | bool = field(
        default=None,
        metadata={
            "name": "Exchangeable",
            "type": "Attribute",
        },
    )
    first_class_upgrade: None | bool = field(
        default=None,
        metadata={
            "name": "FirstClassUpgrade",
            "type": "Attribute",
        },
    )
    ticket_by_date: None | str = field(
        default=None,
        metadata={
            "name": "TicketByDate",
            "type": "Attribute",
        },
    )
    pricing_tag: None | str = field(
        default=None,
        metadata={
            "name": "PricingTag",
            "type": "Attribute",
        },
    )
    equivalent_change_fee: None | str = field(
        default=None,
        metadata={
            "name": "EquivalentChangeFee",
            "type": "Attribute",
        },
    )
    equivalent_exchange_amount: None | str = field(
        default=None,
        metadata={
            "name": "EquivalentExchangeAmount",
            "type": "Attribute",
        },
    )
    add_collection: None | str = field(
        default=None,
        metadata={
            "name": "AddCollection",
            "type": "Attribute",
        },
    )
    residual_value: None | str = field(
        default=None,
        metadata={
            "name": "ResidualValue",
            "type": "Attribute",
        },
    )
    total_residual_value: None | str = field(
        default=None,
        metadata={
            "name": "TotalResidualValue",
            "type": "Attribute",
        },
    )
    original_flight_value: None | str = field(
        default=None,
        metadata={
            "name": "OriginalFlightValue",
            "type": "Attribute",
        },
    )
    flown_segment_value: None | str = field(
        default=None,
        metadata={
            "name": "FlownSegmentValue",
            "type": "Attribute",
        },
    )
    bulk_ticket_advisory: None | bool = field(
        default=None,
        metadata={
            "name": "BulkTicketAdvisory",
            "type": "Attribute",
        },
    )
    fare_pull: None | TypeFarePull5 = field(
        default=None,
        metadata={
            "name": "FarePull",
            "type": "Attribute",
        },
    )
    refund: None | str = field(
        default=None,
        metadata={
            "name": "Refund",
            "type": "Attribute",
        },
    )

    @dataclass
    class TotalPenaltyTaxInfo:
        penalty_tax_info: list[TypeTax5] = field(
            default_factory=list,
            metadata={
                "name": "PenaltyTaxInfo",
                "type": "Element",
                "max_occurs": 999,
            },
        )
        total_penalty_tax: None | str = field(
            default=None,
            metadata={
                "name": "TotalPenaltyTax",
                "type": "Attribute",
            },
        )

    @dataclass
    class TicketFeeInfo:
        base: None | str = field(
            default=None,
            metadata={
                "name": "Base",
                "type": "Attribute",
            },
        )
        tax: None | str = field(
            default=None,
            metadata={
                "name": "Tax",
                "type": "Attribute",
            },
        )
        total: None | str = field(
            default=None,
            metadata={
                "name": "Total",
                "type": "Attribute",
            },
        )
