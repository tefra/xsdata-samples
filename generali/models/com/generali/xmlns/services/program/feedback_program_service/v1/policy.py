from __future__ import annotations

from dataclasses import dataclass, field

from generali.models.com.generali.xmlns.services.program.feedback_program_service.v1.errors import (
    Errors,
)
from generali.models.com.generali.xmlns.services.program.feedback_program_service.v1.local_policies import (
    LocalPolicies,
)

__NAMESPACE__ = (
    "http://xmlns.generali.com/services/program/FeedbackProgramService/v1"
)


@dataclass(kw_only=True)
class Policy:
    class Meta:
        namespace = "http://xmlns.generali.com/services/program/FeedbackProgramService/v1"

    policy_id: str = field(
        metadata={
            "name": "PolicyID",
            "type": "Element",
            "required": True,
        }
    )
    status: str = field(
        metadata={
            "name": "Status",
            "type": "Element",
            "required": True,
        }
    )
    local_policies: LocalPolicies = field(
        metadata={
            "name": "LocalPolicies",
            "type": "Element",
            "required": True,
        }
    )
    errors: Errors = field(
        metadata={
            "name": "Errors",
            "type": "Element",
            "required": True,
        }
    )
