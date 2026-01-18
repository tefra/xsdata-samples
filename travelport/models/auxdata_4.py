from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/common_v33_0"


@dataclass(kw_only=True)
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

    @dataclass(kw_only=True)
    class Entry:
        reason: str = field(
            metadata={
                "name": "Reason",
                "type": "Element",
                "required": True,
            }
        )
        description: str = field(
            metadata={
                "name": "Description",
                "type": "Element",
                "required": True,
            }
        )
