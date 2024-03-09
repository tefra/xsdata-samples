from dataclasses import dataclass, field
from typing import Optional

from generali.models.com.generali.enterprise_services.core.gbs.enterprise.organisation.v1.feedback_program_service_feedback_program_policies_output_body_fault import (
    FeedbackProgramServiceFeedbackProgramPoliciesOutputBodyFault,
)
from generali.models.com.generali.xmlns.services.program.feedback_program_service.v1.feedback_program_policies_response import (
    FeedbackProgramPoliciesResponse,
)

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbs/enterprise/organisation/v1"


@dataclass
class FeedbackProgramServiceFeedbackProgramPoliciesOutputBody:
    class Meta:
        global_type = False

    feedback_program_policies_response: Optional[
        FeedbackProgramPoliciesResponse
    ] = field(
        default=None,
        metadata={
            "name": "FeedbackProgramPoliciesResponse",
            "type": "Element",
            "namespace": "http://xmlns.generali.com/services/program/FeedbackProgramService/v1",
        },
    )
    fault: Optional[
        FeedbackProgramServiceFeedbackProgramPoliciesOutputBodyFault
    ] = field(
        default=None,
        metadata={
            "name": "Fault",
            "type": "Element",
            "namespace": "http://schemas.xmlsoap.org/soap/envelope/",
        },
    )
