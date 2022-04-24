from dataclasses import dataclass, field
from typing import Optional
from generali.models.com.generali.enterprise_services.core.gbs.enterprise.organisation.v1.agreement_interface_notify_agreement_output_body import AgreementInterfaceNotifyAgreementOutputBody

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbs/enterprise/organisation/v1"


@dataclass
class AgreementInterfaceNotifyAgreementOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional[AgreementInterfaceNotifyAgreementOutputBody] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )
