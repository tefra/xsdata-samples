from dataclasses import dataclass, field
from typing import Optional
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.number_type import (
    NumberType,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.common.v1.expansive_structure_type_geographic_locations import (
    ExpansiveStructureTypeGeographicLocations,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.common.v1.structure_type import (
    StructureType,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1"
)


@dataclass
class ExpansiveStructureType(StructureType):
    number: Optional[NumberType] = field(
        default=None,
        metadata={
            "name": "Number",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    geographic_locations: Optional[
        ExpansiveStructureTypeGeographicLocations
    ] = field(
        default=None,
        metadata={
            "name": "GeographicLocations",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
