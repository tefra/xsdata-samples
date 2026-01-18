from __future__ import annotations

from dataclasses import dataclass, field

from generali.models.com.generali.enterprise_services.core.gbs.enterprise.organisation.v1.agreement_interface_notify_agreement_input_body import (
    AgreementInterfaceNotifyAgreementInputBody,
)

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbs/enterprise/organisation/v1"


@dataclass
class AgreementInterfaceNotifyAgreementInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: AgreementInterfaceNotifyAgreementInputBody | None = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        },
    )
