from dataclasses import dataclass, field
from typing import Optional
from generali.models.com.generali.enterprise_services.core.gbm.enterprise.agreement.v1.notify_program_gbmrequest import NotifyProgramGbmrequest

__NAMESPACE__ = "http://xmlns.generali.com/services/program/FeedbackProgramService/v1"


@dataclass
class AgreementInterfaceNotifyAgreementInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["AgreementInterfaceNotifyAgreementInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        notify_program_gbmrequest: Optional[NotifyProgramGbmrequest] = field(
            default=None,
            metadata={
                "name": "NotifyProgramGBMRequest",
                "type": "Element",
                "namespace": "http://generali.com/enterprise-services/core/gbm/enterprise/agreement/v1",
            }
        )
