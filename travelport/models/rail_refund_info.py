from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/rail_v52_0"


@dataclass
class RailRefundInfo:
    """
    Information about refund.

    Parameters
    ----------
    refund_amount
        Amount refunded back to customer.
    cancellation_fee
        Cancellation penalty imposed by the distributor.
    refund
        Indicates whether vendor offers refund on rail reservation.
    retain
        Indicates whether vendor retains the amount to be used later.
    retain_amount
        Amount retained by rail vendor for futute exchange/rail book at rail
        vendor site.
    net_amount
        Net total amount to be refunded or retained by the vendor.
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
    refund: None | bool = field(
        default=None,
        metadata={
            "name": "Refund",
            "type": "Attribute",
        },
    )
    retain: None | bool = field(
        default=None,
        metadata={
            "name": "Retain",
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
    net_amount: None | str = field(
        default=None,
        metadata={
            "name": "NetAmount",
            "type": "Attribute",
        },
    )
