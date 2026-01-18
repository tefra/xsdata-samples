from dataclasses import dataclass, field
from typing import Optional

from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.underwriter_role_type import (
    UnderwriterRoleType,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.common.v1.contact_involvement import (
    ContactInvolvement,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"
)


@dataclass
class UnderwriterInvolvement(ContactInvolvement):
    underwriter_role: UnderwriterRoleType | None = field(
        default=None,
        metadata={
            "name": "UnderwriterRole",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        },
    )
