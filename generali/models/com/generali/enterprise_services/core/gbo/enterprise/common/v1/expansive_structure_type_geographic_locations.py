from __future__ import annotations

from dataclasses import dataclass, field

from generali.models.com.generali.enterprise_services.core.gbo.common.v1.geography_type import (
    GeographyType,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1"
)


@dataclass(kw_only=True)
class ExpansiveStructureTypeGeographicLocations:
    class Meta:
        global_type = False

    geographic_location: list[GeographyType] = field(
        default_factory=list,
        metadata={
            "name": "GeographicLocation",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
