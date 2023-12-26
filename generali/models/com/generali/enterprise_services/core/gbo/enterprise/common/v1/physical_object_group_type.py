from dataclasses import dataclass, field
from typing import List, Optional
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.common.v1.risk_element_type import (
    RiskElementType,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1"
)


@dataclass
class PhysicalObjectGroupType:
    physical_object: List[RiskElementType] = field(
        default_factory=list,
        metadata={
            "name": "PhysicalObject",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
            "min_occurs": 1,
        },
    )
    max_allowed: Optional[int] = field(
        default=None,
        metadata={
            "name": "maxAllowed",
            "type": "Attribute",
        },
    )
