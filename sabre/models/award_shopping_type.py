from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass(kw_only=True)
class AwardShoppingType:
    """
    Attributes:
        enable: Enable award shopping.
        use_ras: Use Redemption Availability Service
    """

    enable: None | bool = field(
        default=None,
        metadata={
            "name": "Enable",
            "type": "Attribute",
        },
    )
    use_ras: bool = field(
        default=False,
        metadata={
            "name": "UseRAS",
            "type": "Attribute",
        },
    )
