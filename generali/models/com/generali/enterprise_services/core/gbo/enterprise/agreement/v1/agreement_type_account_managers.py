from __future__ import annotations

from dataclasses import dataclass, field

from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.account_manager_involvement_type import (
    AccountManagerInvolvementType,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"
)


@dataclass(kw_only=True)
class AgreementTypeAccountManagers:
    class Meta:
        global_type = False

    account_manager: list[AccountManagerInvolvementType] = field(
        default_factory=list,
        metadata={
            "name": "AccountManager",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "min_occurs": 1,
        },
    )
