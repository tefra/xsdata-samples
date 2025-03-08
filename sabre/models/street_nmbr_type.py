from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass
class StreetNmbrType:
    """
    Street name; number on street.

    Attributes:
        value:
        po_box: Defines a Post Office Box number.
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 0,
            "max_length": 64,
        },
    )
    po_box: None | str = field(
        default=None,
        metadata={
            "name": "PO_Box",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 16,
        },
    )
