from dataclasses import dataclass, field
from typing import Optional

from generali.models.com.generali.xmlns.services.program.feedback_program_service.v1.risk import (
    Risk,
)

__NAMESPACE__ = (
    "http://xmlns.generali.com/services/program/FeedbackProgramService/v1"
)


@dataclass
class Risks:
    class Meta:
        namespace = "http://xmlns.generali.com/services/program/FeedbackProgramService/v1"

    risk: Risk | None = field(
        default=None,
        metadata={
            "name": "Risk",
            "type": "Element",
            "required": True,
        },
    )
