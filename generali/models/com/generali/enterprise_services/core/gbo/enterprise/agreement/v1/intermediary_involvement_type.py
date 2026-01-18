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


@dataclass
class IntermediaryInvolvementType(OrganisationInvolvementType):
    organisation_role: IntermediaryRoleType | None = field(
        default=None,
        metadata={
            "name": "OrganisationRole",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        },
    )
    intermediary_type: IntermediaryTypeEnum | None = field(
        default=None,
        metadata={
            "name": "IntermediaryType",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        },
    )
