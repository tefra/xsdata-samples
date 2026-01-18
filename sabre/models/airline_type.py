from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass(kw_only=True)
class AirlineType:
    """
    Attributes:
        operating: Operating airline code
        marketing: Marketing airline code
    """

    operating: str = field(
        metadata={
            "name": "Operating",
            "type": "Attribute",
            "required": True,
            "pattern": r"[0-9A-Z]{2,3}",
        }
    )
    marketing: str = field(
        metadata={
            "name": "Marketing",
            "type": "Attribute",
            "required": True,
            "pattern": r"[0-9A-Z]{2,3}",
        }
    )
