from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = (
    "http://xmlns.generali.com/services/program/FeedbackProgramService/v1"
)


@dataclass(kw_only=True)
class ErrorItem:
    class Meta:
        namespace = "http://xmlns.generali.com/services/program/FeedbackProgramService/v1"

    code: str = field(
        metadata={
            "name": "Code",
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
    type_value: str = field(
        metadata={
            "name": "Type",
            "type": "Element",
            "required": True,
        }
    )
    level: str = field(
        metadata={
            "name": "Level",
            "type": "Element",
            "required": True,
        }
    )
