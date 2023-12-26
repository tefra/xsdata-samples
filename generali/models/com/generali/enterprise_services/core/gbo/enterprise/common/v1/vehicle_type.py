from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDate
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.code_type import (
    CodeType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.text_type import (
    TextType,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.common.v1.risk_element_type import (
    RiskElementType,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1"
)


@dataclass
class VehicleType(RiskElementType):
    manufactured_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ManufacturedDate",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    manufacturer: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "Manufacturer",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    model: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "Model",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    vehicle_identifier: Optional[CodeType] = field(
        default=None,
        metadata={
            "name": "VehicleIdentifier",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
