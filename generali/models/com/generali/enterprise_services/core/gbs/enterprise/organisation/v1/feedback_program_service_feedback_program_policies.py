from generali.models.com.generali.enterprise_services.core.gbs.enterprise.organisation.v1.feedback_program_service_feedback_program_policies_input import (
    FeedbackProgramServiceFeedbackProgramPoliciesInput,
)
from generali.models.com.generali.enterprise_services.core.gbs.enterprise.organisation.v1.feedback_program_service_feedback_program_policies_output import (
    FeedbackProgramServiceFeedbackProgramPoliciesOutput,
)

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbs/enterprise/organisation/v1"


class FeedbackProgramServiceFeedbackProgramPolicies:
    uri = "#UP_policy"
    style = "document"
    location = "https://services-dev.generali.co.uk/services/external/GIP/v1/FeedbackProgramService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "FeedbackProgramPolicies"
    input = FeedbackProgramServiceFeedbackProgramPoliciesInput
    output = FeedbackProgramServiceFeedbackProgramPoliciesOutput
