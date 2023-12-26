from dataclasses import dataclass, field
from typing import Optional
from generali.models.com.generali.xmlns.services.program.feedback_program_service.v1.error_item import (
    ErrorItem,
)

__NAMESPACE__ = (
    "http://xmlns.generali.com/services/program/FeedbackProgramService/v1"
)


@dataclass
class Errors:
    class Meta:
        namespace = "http://xmlns.generali.com/services/program/FeedbackProgramService/v1"

    error_item: Optional[ErrorItem] = field(
        default=None,
        metadata={
            "name": "ErrorItem",
            "type": "Element",
            "required": True,
        },
    )
