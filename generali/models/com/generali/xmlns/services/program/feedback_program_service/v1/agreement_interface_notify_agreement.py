
from generali.models.com.generali.xmlns.services.program.feedback_program_service.v1.agreement_interface_notify_agreement_input import AgreementInterfaceNotifyAgreementInput
from generali.models.com.generali.xmlns.services.program.feedback_program_service.v1.agreement_interface_notify_agreement_output import AgreementInterfaceNotifyAgreementOutput

__NAMESPACE__ = "http://xmlns.generali.com/services/program/FeedbackProgramService/v1"


class AgreementInterfaceNotifyAgreement:
    style = "document"
    location = "REPLACE_WITH_ACTUAL_URL"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://generali.com/enterprise-services/core/gbs/enterprise/agreement/v1/notify"
    input = AgreementInterfaceNotifyAgreementInput
    output = AgreementInterfaceNotifyAgreementOutput
