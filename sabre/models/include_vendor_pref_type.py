from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass
class IncludeVendorPrefType:
    """
    Consider only these carriers for this leg.

    Attributes:
        code: Identifies a company by the company code.
    """

    code: None | str = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 8,
        },
    )
