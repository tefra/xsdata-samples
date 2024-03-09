from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/common_v34_0"


@dataclass
class Remark7:
    """A textual remark container to hold any printable text.

    (max 512 chars)
    """

    class Meta:
        name = "Remark"
        namespace = "http://www.travelport.com/schema/common_v34_0"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        },
    )
