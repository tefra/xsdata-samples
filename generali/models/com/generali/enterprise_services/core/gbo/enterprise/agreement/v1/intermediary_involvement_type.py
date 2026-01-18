from __future__ import annotations

from dataclasses import dataclass, field

from generali.models.com.generali.enterprise_services.core.gbo.enterprise.common.v1.intermediary_role_type import (
    IntermediaryRoleType,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.common.v1.intermediary_type_enum import (
    IntermediaryTypeEnum,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.common.v1.organisation_involvement_type import (
    OrganisationInvolvementType,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"
)


@dataclass(kw_only=True)
class IntermediaryInvolvementType(OrganisationInvolvementType):
    organisation_role: IntermediaryRoleType = field(
        metadata={
            "name": "OrganisationRole",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        }
    )
    intermediary_type: IntermediaryTypeEnum = field(
        metadata={
            "name": "IntermediaryType",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        }
    )
