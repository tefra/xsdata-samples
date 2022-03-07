from dataclasses import dataclass, field
from typing import List, Optional
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.geography_type import GeographyType
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.common.v1.structure_type import StructureType

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1"


@dataclass
class ExpansiveStructureType(StructureType):
    number: Optional[int] = field(
        default=None,
        metadata={
            "name": "Number",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        }
    )
    geographic_locations: Optional["ExpansiveStructureType.GeographicLocations"] = field(
        default=None,
        metadata={
            "name": "GeographicLocations",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        }
    )

    @dataclass
    class GeographicLocations:
        geographic_location: List[GeographyType] = field(
            default_factory=list,
            metadata={
                "name": "GeographicLocation",
                "type": "Element",
                "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
            }
        )
