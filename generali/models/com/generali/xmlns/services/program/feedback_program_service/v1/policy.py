from dataclasses import dataclass, field
from typing import Optional

from generali.models.com.generali.xmlns.services.program.feedback_program_service.v1.errors import (
    Errors,
)
from generali.models.com.generali.xmlns.services.program.feedback_program_service.v1.local_policies import (
    LocalPolicies,
)

__NAMESPACE__ = (
    "http://xmlns.generali.com/services/program/FeedbackProgramService/v1"
)


@dataclass
class Policy:
    class Meta:
        namespace = "http://xmlns.generali.com/services/program/FeedbackProgramService/v1"

    policy_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PolicyID",
            "type": "Element",
            "required": True,
        },
    )
    status: Optional[str] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Element",
            "required": True,
        },
    )
    local_policies: Optional[LocalPolicies] = field(
        default=None,
        metadata={
            "name": "LocalPolicies",
            "type": "Element",
            "required": True,
        },
    )
    errors: Optional[Errors] = field(
        default=None,
        metadata={
            "name": "Errors",
            "type": "Element",
            "required": True,
        },
    )
