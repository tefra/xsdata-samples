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
        }
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
        }
    )
    level: Optional[str] = field(
        default=None,
        metadata={
            "name": "Level",
            "type": "Element",
        }
    )
