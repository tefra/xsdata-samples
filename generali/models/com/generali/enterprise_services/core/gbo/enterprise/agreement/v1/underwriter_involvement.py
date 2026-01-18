from __future__ import annotations

from dataclasses import dataclass, field

from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.underwriter_role_type import (
    UnderwriterRoleType,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.common.v1.contact_involvement import (
    ContactInvolvement,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"
)


@dataclass(kw_only=True)
class UnderwriterInvolvement(ContactInvolvement):
    underwriter_role: UnderwriterRoleType = field(
        metadata={
            "name": "UnderwriterRole",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        }
    )
