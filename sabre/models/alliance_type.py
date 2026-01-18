from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass(kw_only=True)
class AllianceType:
    """
    Attributes:
        code: Identifies an alliance by the alliance code.
    """

    code: str = field(
        metadata={
            "name": "Code",
            "type": "Attribute",
            "required": True,
            "length": 2,
        }
    )
