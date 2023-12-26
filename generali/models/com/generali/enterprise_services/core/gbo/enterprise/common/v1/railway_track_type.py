from dataclasses import dataclass, field
from typing import Optional
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.common.v1.expansive_structure_type import (
    ExpansiveStructureType,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1"
)


@dataclass
class RailwayTrackType(ExpansiveStructureType):
    electrified: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Electrified",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
            "required": True,
        },
    )
