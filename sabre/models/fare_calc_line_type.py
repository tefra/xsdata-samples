from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass
class FareCalcLineType:
    """
    IntelliSell Type.
    """

    info: None | str = field(
        default=None,
        metadata={
            "name": "Info",
            "type": "Attribute",
        },
    )
