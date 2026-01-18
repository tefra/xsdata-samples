from __future__ import annotations

from dataclasses import dataclass, field

from generali.models.com.generali.xmlns.services.program.feedback_program_service.v1.feedback_program_policies import (
    FeedbackProgramPolicies,
)

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbs/enterprise/organisation/v1"


@dataclass(kw_only=True)
class FeedbackProgramServiceFeedbackProgramPoliciesInputBody:
    class Meta:
        global_type = False

    feedback_program_policies: FeedbackProgramPolicies = field(
        metadata={
            "name": "FeedbackProgramPolicies",
            "type": "Element",
            "namespace": "http://xmlns.generali.com/services/program/FeedbackProgramService/v1",
        }
    )
