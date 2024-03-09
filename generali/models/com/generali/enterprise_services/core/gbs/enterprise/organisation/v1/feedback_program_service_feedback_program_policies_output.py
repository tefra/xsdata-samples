from dataclasses import dataclass, field
from typing import Optional

from generali.models.com.generali.enterprise_services.core.gbs.enterprise.organisation.v1.feedback_program_service_feedback_program_policies_output_body import (
    FeedbackProgramServiceFeedbackProgramPoliciesOutputBody,
)

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbs/enterprise/organisation/v1"


@dataclass
class FeedbackProgramServiceFeedbackProgramPoliciesOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional[FeedbackProgramServiceFeedbackProgramPoliciesOutputBody] = (
        field(
            default=None,
            metadata={
                "name": "Body",
                "type": "Element",
            },
        )
    )
