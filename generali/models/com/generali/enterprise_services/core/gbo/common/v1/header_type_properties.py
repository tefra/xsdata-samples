from dataclasses import dataclass, field
from typing import List

from generali.models.com.generali.enterprise_services.core.gbo.common.v1.header_type_properties_property import (
    HeaderTypePropertiesProperty,
)

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/common/v1"


@dataclass
class HeaderTypeProperties:
    class Meta:
        global_type = False

    property: List[HeaderTypePropertiesProperty] = field(
        default_factory=list,
        metadata={
            "name": "Property",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        },
    )
