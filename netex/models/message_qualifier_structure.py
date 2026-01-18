from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class MessageQualifierStructure:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
