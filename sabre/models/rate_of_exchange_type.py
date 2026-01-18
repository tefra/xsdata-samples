from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass(kw_only=True)
class RateOfExchangeType:
    """
    Attributes:
        value: Exchange rate
    """

    value: None | float = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Attribute",
        },
    )
