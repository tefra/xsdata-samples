from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/common_v32_0"


@dataclass
class LocatorCode2:
    """
    A locator code that identifies a PNR or searches for one.
    """

    class Meta:
        name = "LocatorCode"
        namespace = "http://www.travelport.com/schema/common_v32_0"

    value: str = field(
        default="",
        metadata={
            "min_length": 1,
        },
    )
