from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/uprofileCommon_v30_0"


@dataclass
class Auxdata2:
    class Meta:
        name = "Auxdata"
        namespace = "http://www.travelport.com/schema/uprofileCommon_v30_0"

    entry: list[Auxdata2.Entry] = field(
        default_factory=list,
        metadata={
            "name": "Entry",
            "type": "Element",
            "min_occurs": 1,
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
