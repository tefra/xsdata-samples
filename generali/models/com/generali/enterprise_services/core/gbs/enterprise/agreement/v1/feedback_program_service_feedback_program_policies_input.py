from dataclasses import dataclass, field
from typing import Optional
from generali.models.com.generali.xmlns.services.program.feedback_program_service.v1.feedback_program_policies import FeedbackProgramPolicies

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbs/enterprise/agreement/v1"


@dataclass
class FeedbackProgramServiceFeedbackProgramPoliciesInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["FeedbackProgramServiceFeedbackProgramPoliciesInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        feedback_program_policies: Optional[FeedbackProgramPolicies] = field(
            default=None,
            metadata={
                "name": "FeedbackProgramPolicies",
                "type": "Element",
                "namespace": "http://xmlns.generali.com/services/program/FeedbackProgramService/v1",
            }
        )
