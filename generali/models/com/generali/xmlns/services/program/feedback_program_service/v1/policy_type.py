from __future__ import annotations

from dataclasses import dataclass, field

from generali.models.com.generali.xmlns.services.program.feedback_program_service.v1.errors_type import (
    ErrorsType,
)
from generali.models.com.generali.xmlns.services.program.feedback_program_service.v1.local_policies import (
    LocalPolicies,
)
from generali.models.com.generali.xmlns.services.program.feedback_program_service.v1.status import (
    Status,
)

__NAMESPACE__ = (
    "http://xmlns.generali.com/services/program/FeedbackProgramService/v1"
)


@dataclass
class PolicyType:
    policy_id: str | None = field(
        default=None,
        metadata={
            "name": "PolicyID",
            "type": "Element",
            "namespace": "http://xmlns.generali.com/services/program/FeedbackProgramService/v1",
            "required": True,
        },
    )
    status: Status | None = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Element",
            "namespace": "http://xmlns.generali.com/services/program/FeedbackProgramService/v1",
        },
    )
    local_policies: LocalPolicies | None = field(
        default=None,
        metadata={
            "name": "LocalPolicies",
            "type": "Element",
            "namespace": "http://xmlns.generali.com/services/program/FeedbackProgramService/v1",
            "required": True,
        },
    )
    errors: ErrorsType | None = field(
        default=None,
        metadata={
            "name": "Errors",
            "type": "Element",
            "namespace": "http://xmlns.generali.com/services/program/FeedbackProgramService/v1",
        },
    )
