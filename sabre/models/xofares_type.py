from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass
class XofaresType:
    """
    XOFares indicator.
    """

    class Meta:
        name = "XOFaresType"

    value: None | bool = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Attribute",
            "required": True,
        },
    )
