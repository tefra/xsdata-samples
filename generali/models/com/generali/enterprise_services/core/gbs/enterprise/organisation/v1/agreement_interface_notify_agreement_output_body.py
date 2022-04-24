from dataclasses import dataclass, field
from typing import Optional
from generali.models.com.generali.enterprise_services.core.gbm.enterprise.agreement.v1.notify_program_gbmresponse import NotifyProgramGbmresponse
from generali.models.com.generali.enterprise_services.core.gbs.enterprise.organisation.v1.agreement_interface_notify_agreement_output_body_fault import AgreementInterfaceNotifyAgreementOutputBodyFault

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbs/enterprise/organisation/v1"


@dataclass
class AgreementInterfaceNotifyAgreementOutputBody:
    class Meta:
        global_type = False

    notify_program_gbmresponse: Optional[NotifyProgramGbmresponse] = field(
        default=None,
        metadata={
            "name": "NotifyProgramGBMResponse",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbm/enterprise/agreement/v1",
        }
    )
    fault: Optional[AgreementInterfaceNotifyAgreementOutputBodyFault] = field(
        default=None,
        metadata={
            "name": "Fault",
            "type": "Element",
            "namespace": "http://schemas.xmlsoap.org/soap/envelope/",
        }
    )
