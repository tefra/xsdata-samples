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


@dataclass(kw_only=True)
class PolicyType:
    policy_id: str = field(
        metadata={
            "name": "PolicyID",
            "type": "Element",
            "namespace": "http://xmlns.generali.com/services/program/FeedbackProgramService/v1",
            "required": True,
        }
    )
    status: None | Status = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Element",
            "namespace": "http://xmlns.generali.com/services/program/FeedbackProgramService/v1",
        },
    )
    local_policies: LocalPolicies = field(
        metadata={
            "name": "LocalPolicies",
            "type": "Element",
            "namespace": "http://xmlns.generali.com/services/program/FeedbackProgramService/v1",
            "required": True,
        }
    )
    errors: None | ErrorsType = field(
        default=None,
        metadata={
            "name": "Errors",
            "type": "Element",
            "namespace": "http://xmlns.generali.com/services/program/FeedbackProgramService/v1",
        },
    )
