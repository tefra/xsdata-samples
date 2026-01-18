from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass(kw_only=True)
class SideTripType:
    """
    Attributes:
        number: Side trip number
        start: Side trip start
        end: Side trip end
    """

    number: None | int = field(
        default=None,
        metadata={
            "name": "Number",
            "type": "Attribute",
        },
    )
    start: None | bool = field(
        default=None,
        metadata={
            "name": "Start",
            "type": "Attribute",
        },
    )
    end: None | bool = field(
        default=None,
        metadata={
            "name": "End",
            "type": "Attribute",
        },
    )
