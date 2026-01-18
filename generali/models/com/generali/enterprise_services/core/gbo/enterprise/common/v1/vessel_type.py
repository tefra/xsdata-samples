from __future__ import annotations

from dataclasses import dataclass, field

from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.number_type import (
    NumberType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.text_type import (
    TextType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.code_description_type import (
    CodeDescriptionType,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.common.v1.vehicle_type import (
    VehicleType,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1"
)


@dataclass(kw_only=True)
class VesselType(VehicleType):
    passenger_capacity: None | NumberType = field(
        default=None,
        metadata={
            "name": "PassengerCapacity",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    primary_port: None | TextType = field(
        default=None,
        metadata={
            "name": "PrimaryPort",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    vehicle_capacity: None | NumberType = field(
        default=None,
        metadata={
            "name": "VehicleCapacity",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    waters_navigated: None | CodeDescriptionType = field(
        default=None,
        metadata={
            "name": "WatersNavigated",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
