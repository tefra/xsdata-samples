from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class FareRuleLongRef:
    """
    A reference to an Long Text Rule in a Shared List.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        },
    )
