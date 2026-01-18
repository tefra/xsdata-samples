from __future__ import annotations

from dataclasses import dataclass, field

from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.underwriter_role_type_underwriter_type import (
    UnderwriterRoleTypeUnderwriterType,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"
)


@dataclass(kw_only=True)
class UnderwriterRoleType:
    underwriter_type: UnderwriterRoleTypeUnderwriterType = field(
        metadata={
            "name": "UnderwriterType",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        }
    )
