from dataclasses import dataclass, field

from generali.models.com.generali.xmlns.services.program.feedback_program_service.v1.feedback_program_policies import (
    FeedbackProgramPolicies,
)

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbs/enterprise/organisation/v1"


@dataclass
class FeedbackProgramServiceFeedbackProgramPoliciesInputBody:
    class Meta:
        global_type = False

    feedback_program_policies: FeedbackProgramPolicies | None = field(
        default=None,
        metadata={
            "name": "FeedbackProgramPolicies",
            "type": "Element",
            "namespace": "http://xmlns.generali.com/services/program/FeedbackProgramService/v1",
        },
    )
