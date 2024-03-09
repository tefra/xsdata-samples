from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


@dataclass
class Auxdata1:
    class Meta:
        name = "Auxdata"
        namespace = "http://www.travelport.com/schema/common_v52_0"

    entry: list[Auxdata1.Entry] = field(
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
