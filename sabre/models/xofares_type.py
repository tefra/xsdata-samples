from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass(kw_only=True)
class XofaresType:
    """
    XOFares indicator.
    """

    class Meta:
        name = "XOFaresType"

    value: bool = field(
        metadata={
            "name": "Value",
            "type": "Attribute",
            "required": True,
        }
    )
