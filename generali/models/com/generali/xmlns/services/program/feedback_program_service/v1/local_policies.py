from dataclasses import dataclass, field
from typing import Optional

from generali.models.com.generali.xmlns.services.program.feedback_program_service.v1.local_policy import (
    LocalPolicy,
)

__NAMESPACE__ = (
    "http://xmlns.generali.com/services/program/FeedbackProgramService/v1"
)


@dataclass
class LocalPolicies:
    class Meta:
        namespace = "http://xmlns.generali.com/services/program/FeedbackProgramService/v1"

    local_policy: Optional[LocalPolicy] = field(
        default=None,
        metadata={
            "name": "LocalPolicy",
            "type": "Element",
            "required": True,
        },
    )
