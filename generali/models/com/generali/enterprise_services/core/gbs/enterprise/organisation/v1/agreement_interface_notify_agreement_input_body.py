from __future__ import annotations

from dataclasses import dataclass, field

from generali.models.com.generali.enterprise_services.core.gbm.enterprise.agreement.v1.notify_program_gbmrequest import (
    NotifyProgramGbmrequest,
)

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbs/enterprise/organisation/v1"


@dataclass
class AgreementInterfaceNotifyAgreementInputBody:
    class Meta:
        global_type = False

    notify_program_gbmrequest: None | NotifyProgramGbmrequest = field(
        default=None,
        metadata={
            "name": "NotifyProgramGBMRequest",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbm/enterprise/agreement/v1",
        },
    )
