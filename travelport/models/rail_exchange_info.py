from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/rail_v52_0"


@dataclass
class RailExchangeInfo:
    """
    Exchange information for the rail booking.

    Parameters
    ----------
    refund_amount
    cancellation_fee
    exchange_amount
    approximate_refund_amount
    approximate_cancellation_fee
    approximate_exchange_amount
        The Converted total price in Default Currency for this entity
        including base price and all taxes.
    retain_amount
        Amount retained by a rail vendor for future use at the vendor’s
        site.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v52_0"

    refund_amount: None | str = field(
        default=None,
        metadata={
            "name": "RefundAmount",
            "type": "Attribute",
        },
    )
    cancellation_fee: None | str = field(
        default=None,
        metadata={
            "name": "CancellationFee",
            "type": "Attribute",
        },
    )
    exchange_amount: None | str = field(
        default=None,
        metadata={
            "name": "ExchangeAmount",
            "type": "Attribute",
        },
    )
    approximate_refund_amount: None | str = field(
        default=None,
        metadata={
            "name": "ApproximateRefundAmount",
            "type": "Attribute",
        },
    )
    approximate_cancellation_fee: None | str = field(
        default=None,
        metadata={
            "name": "ApproximateCancellationFee",
            "type": "Attribute",
        },
    )
    approximate_exchange_amount: None | str = field(
        default=None,
        metadata={
            "name": "ApproximateExchangeAmount",
            "type": "Attribute",
        },
    )
    retain_amount: None | str = field(
        default=None,
        metadata={
            "name": "RetainAmount",
            "type": "Attribute",
        },
    )
