from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass
class ProcessingMessageType:
    """
    Message generated per for particular date and leg.

    Attributes:
        pricing_source: Pricing source.
        message: Message text
    """

    pricing_source: None | str = field(
        default=None,
        metadata={
            "name": "PricingSource",
            "type": "Attribute",
            "required": True,
            "pattern": r"[0-9A-Z_]{1,13}",
        },
    )
    message: None | str = field(
        default=None,
        metadata={
            "name": "Message",
            "type": "Attribute",
            "required": True,
        },
    )
