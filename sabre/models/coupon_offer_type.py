from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass(kw_only=True)
class CouponOfferType:
    """
    Not used.
    """

    promo_id: None | object = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    corp_id: None | object = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    headline: None | object = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    discount_pctg: None | object = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
