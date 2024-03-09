from dataclasses import dataclass, field
from typing import Optional

from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.insured_involvement_type import (
    InsuredInvolvementType,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.common.v1.insured_role_type import (
    InsuredRoleType,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"
)


@dataclass
class InsuredInvolvement:
    insured_role: Optional[InsuredRoleType] = field(
        default=None,
        metadata={
            "name": "InsuredRole",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        },
    )
    type_value: Optional[InsuredInvolvementType] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        },
    )
