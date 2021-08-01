from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "urn:vpro:media:2009"


@dataclass
class RepeatType:
    class Meta:
        name = "repeatType"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    is_rerun: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isRerun",
            "type": "Attribute",
            "required": True,
        }
    )
