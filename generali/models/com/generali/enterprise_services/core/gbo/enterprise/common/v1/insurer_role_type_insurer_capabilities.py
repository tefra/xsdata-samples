from dataclasses import dataclass, field

from generali.models.com.generali.enterprise_services.core.gbo.enterprise.common.v1.insurer_capability_type import (
    InsurerCapabilityType,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1"
)


@dataclass
class InsurerRoleTypeInsurerCapabilities:
    class Meta:
        global_type = False

    insurer_capability: list[InsurerCapabilityType] = field(
        default_factory=list,
        metadata={
            "name": "InsurerCapability",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
            "min_occurs": 1,
        },
    )
