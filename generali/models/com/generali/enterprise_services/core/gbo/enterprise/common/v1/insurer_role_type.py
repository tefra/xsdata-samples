from __future__ import annotations

from dataclasses import dataclass, field

from generali.models.com.generali.enterprise_services.core.gbo.enterprise.common.v1.insurer_role_type_insurer_capabilities import (
    InsurerRoleTypeInsurerCapabilities,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.common.v1.organisation_role_type import (
    OrganisationRoleType,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1"
)


@dataclass
class InsurerRoleType(OrganisationRoleType):
    insurer_capabilities: InsurerRoleTypeInsurerCapabilities | None = field(
        default=None,
        metadata={
            "name": "InsurerCapabilities",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
            "required": True,
        },
    )
