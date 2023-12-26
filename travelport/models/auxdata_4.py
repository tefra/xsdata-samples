from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/common_v33_0"


@dataclass
class Auxdata4:
    class Meta:
        name = "Auxdata"
        namespace = "http://www.travelport.com/schema/common_v33_0"

    entry: list[Auxdata4.Entry] = field(
        default_factory=list,
        metadata={
            "name": "Entry",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        },
    )

    @dataclass
    class Entry:
        reason: None | str = field(
            default=None,
            metadata={
                "name": "Reason",
                "type": "Element",
                "required": True,
            },
        )
        description: None | str = field(
            default=None,
            metadata={
                "name": "Description",
                "type": "Element",
                "required": True,
            },
        )
