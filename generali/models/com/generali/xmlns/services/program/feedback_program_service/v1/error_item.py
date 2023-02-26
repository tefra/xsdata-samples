from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://xmlns.generali.com/services/program/FeedbackProgramService/v1"


@dataclass
class ErrorItem:
    class Meta:
        namespace = "http://xmlns.generali.com/services/program/FeedbackProgramService/v1"

    code: Optional[str] = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Element",
            "required": True,
        }
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "required": True,
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "required": True,
        }
    )
    level: Optional[str] = field(
        default=None,
        metadata={
            "name": "Level",
            "type": "Element",
            "required": True,
        }
    )
