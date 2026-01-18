from __future__ import annotations

from dataclasses import dataclass, field

from generali.models.com.generali.enterprise_services.core.gbo.enterprise.common.v1.physical_object_group_type import (
    PhysicalObjectGroupType,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1"
)


@dataclass
class PhysicalObjectGroupRoleType:
    physical_object_group: PhysicalObjectGroupType | None = field(
        default=None,
        metadata={
            "name": "PhysicalObjectGroup",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
            "required": True,
        },
    )
