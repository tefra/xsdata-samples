from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/rail_v52_0"


@dataclass(kw_only=True)
class JourneyRemark:
    """
    A Remark for a Journey.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v52_0"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    category: None | str = field(
        default=None,
        metadata={
            "name": "Category",
            "type": "Attribute",
        },
    )
