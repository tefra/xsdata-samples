from __future__ import annotations
from dataclasses import dataclass, field
from decimal import Decimal
from travelport.models.refund_remark_1 import RefundRemark1

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class AirRefundInfo:
    """
    Provides results of a refund quote.

    Parameters
    ----------
    refund_remark
    refund_amount
    retain_amount
    refund_fee
        Refund fee for ACH/1P
    refundable_taxes
        1P - None : All taxes are not refundable. Unknown : Refundability of
        taxes are not known.
    filed_currency
        1P  Currency of filed CAT33 refund fee
    conversion_rate
        1P - Currency conversion rate used for conversion between
        FiledCurrency and PCC base currency in which the response is
        returned.
    taxes
        1P - The total value of taxes.
    original_ticket_total
        1P - The original ticket amount.
    forfeit_amount
    retain
        This indicates whether any amount is retained by the provider.
    refund
        This indicates whether carrier/host supports refund for the
        correcponding pnr.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    refund_remark: list[RefundRemark1] = field(
        default_factory=list,
        metadata={
            "name": "RefundRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    refund_amount: None | str = field(
        default=None,
        metadata={
            "name": "RefundAmount",
            "type": "Attribute",
        }
    )
    retain_amount: None | str = field(
        default=None,
        metadata={
            "name": "RetainAmount",
            "type": "Attribute",
        }
    )
    refund_fee: None | str = field(
        default=None,
        metadata={
            "name": "RefundFee",
            "type": "Attribute",
        }
    )
    refundable_taxes: None | str = field(
        default=None,
        metadata={
            "name": "RefundableTaxes",
            "type": "Attribute",
        }
    )
    filed_currency: None | str = field(
        default=None,
        metadata={
            "name": "FiledCurrency",
            "type": "Attribute",
            "length": 3,
        }
    )
    conversion_rate: None | Decimal = field(
        default=None,
        metadata={
            "name": "ConversionRate",
            "type": "Attribute",
        }
    )
    taxes: None | str = field(
        default=None,
        metadata={
            "name": "Taxes",
            "type": "Attribute",
        }
    )
    original_ticket_total: None | str = field(
        default=None,
        metadata={
            "name": "OriginalTicketTotal",
            "type": "Attribute",
        }
    )
    forfeit_amount: None | str = field(
        default=None,
        metadata={
            "name": "ForfeitAmount",
            "type": "Attribute",
        }
    )
    retain: bool = field(
        default=False,
        metadata={
            "name": "Retain",
            "type": "Attribute",
        }
    )
    refund: bool = field(
        default=False,
        metadata={
            "name": "Refund",
            "type": "Attribute",
        }
    )
