from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/common_v38_0"


@dataclass(kw_only=True)
class ExchangedCoupon6:
    """
    The coupon numbers that were used in the exchange process to create the
    MCO.

    Parameters
    ----------
    ticket_number
        The ticket number for which the exchange coupons are present.
    coupon_number
        Coupon numbers that were exchanged specific to this ticket
    """

    class Meta:
        name = "ExchangedCoupon"
        namespace = "http://www.travelport.com/schema/common_v38_0"

    ticket_number: str = field(
        metadata={
            "name": "TicketNumber",
            "type": "Attribute",
            "required": True,
            "length": 13,
        }
    )
    coupon_number: None | str = field(
        default=None,
        metadata={
            "name": "CouponNumber",
            "type": "Attribute",
        },
    )
