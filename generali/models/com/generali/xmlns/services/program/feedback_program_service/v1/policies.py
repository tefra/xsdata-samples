from dataclasses import dataclass, field
from typing import Optional

from generali.models.com.generali.xmlns.services.program.feedback_program_service.v1.policy import (
    Policy,
)

__NAMESPACE__ = (
    "http://xmlns.generali.com/services/program/FeedbackProgramService/v1"
)


@dataclass
class Policies:
    class Meta:
        namespace = "http://xmlns.generali.com/services/program/FeedbackProgramService/v1"

    policy: Optional[Policy] = field(
        default=None,
        metadata={
            "name": "Policy",
            "type": "Element",
            "required": True,
        },
    )
