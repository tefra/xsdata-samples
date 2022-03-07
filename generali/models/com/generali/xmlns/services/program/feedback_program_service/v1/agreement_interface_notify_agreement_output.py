from dataclasses import dataclass, field
from typing import Optional
from generali.models.com.generali.enterprise_services.core.gbm.enterprise.agreement.v1.notify_program_gbmresponse import NotifyProgramGbmresponse

__NAMESPACE__ = "http://xmlns.generali.com/services/program/FeedbackProgramService/v1"


@dataclass
class AgreementInterfaceNotifyAgreementOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["AgreementInterfaceNotifyAgreementOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        notify_program_gbmresponse: Optional[NotifyProgramGbmresponse] = field(
            default=None,
            metadata={
                "name": "NotifyProgramGBMResponse",
                "type": "Element",
                "namespace": "http://generali.com/enterprise-services/core/gbm/enterprise/agreement/v1",
            }
        )
        fault: Optional["AgreementInterfaceNotifyAgreementOutput.Body.Fault"] = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
