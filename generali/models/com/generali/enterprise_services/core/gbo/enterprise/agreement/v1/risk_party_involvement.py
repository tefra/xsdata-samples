from dataclasses import dataclass, field

from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.risk_involvement import (
    RiskInvolvement,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.common.v1.insured_role_type import (
    InsuredRoleType,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"
)


@dataclass
class RiskPartyInvolvement(RiskInvolvement):
    insured_role: InsuredRoleType | None = field(
        default=None,
        metadata={
            "name": "InsuredRole",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        },
    )
