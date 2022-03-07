from dataclasses import dataclass, field
from typing import List, Optional
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.common.v1.insurer_capability_type import InsurerCapabilityType
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.common.v1.organisation_role_type import OrganisationRoleType

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1"


@dataclass
class InsurerRoleType(OrganisationRoleType):
    insurer_capabilities: Optional["InsurerRoleType.InsurerCapabilities"] = field(
        default=None,
        metadata={
            "name": "InsurerCapabilities",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
            "required": True,
        }
    )

    @dataclass
    class InsurerCapabilities:
        insurer_capability: List[InsurerCapabilityType] = field(
            default_factory=list,
            metadata={
                "name": "InsurerCapability",
                "type": "Element",
                "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
                "min_occurs": 1,
            }
        )
