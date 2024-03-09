from dataclasses import dataclass, field
from typing import List

from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.account_manager_involvement_type import (
    AccountManagerInvolvementType,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"
)


@dataclass
class AgreementTypeAccountManagers:
    class Meta:
        global_type = False

    account_manager: List[AccountManagerInvolvementType] = field(
        default_factory=list,
        metadata={
            "name": "AccountManager",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "min_occurs": 1,
        },
    )
