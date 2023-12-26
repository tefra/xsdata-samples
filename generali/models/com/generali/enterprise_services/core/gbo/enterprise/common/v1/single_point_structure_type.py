from dataclasses import dataclass, field
from typing import Optional
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.geography_type import (
    GeographyType,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.common.v1.structure_type import (
    StructureType,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1"
)


@dataclass
class SinglePointStructureType(StructureType):
    geographic_location: Optional[GeographyType] = field(
        default=None,
        metadata={
            "name": "GeographicLocation",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
