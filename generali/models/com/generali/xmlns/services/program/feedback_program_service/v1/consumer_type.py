from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = (
    "http://xmlns.generali.com/services/program/FeedbackProgramService/v1"
)


@dataclass
class ConsumerType:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
