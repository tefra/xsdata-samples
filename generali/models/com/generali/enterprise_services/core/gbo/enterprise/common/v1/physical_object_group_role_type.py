from dataclasses import dataclass, field
from typing import Optional
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.common.v1.physical_object_group_type import (
    PhysicalObjectGroupType,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1"
)


@dataclass
class PhysicalObjectGroupRoleType:
    physical_object_group: Optional[PhysicalObjectGroupType] = field(
        default=None,
        metadata={
            "name": "PhysicalObjectGroup",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
            "required": True,
        },
    )
