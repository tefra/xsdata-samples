from __future__ import annotations

from dataclasses import dataclass, field

from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.number_type import (
    NumberType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.numeric_type import (
    NumericType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.text_type import (
    TextType,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.common.v1.vehicle_type import (
    VehicleType,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1"
)


@dataclass(kw_only=True)
class TrainType(VehicleType):
    number_of_carriages: None | NumberType = field(
        default=None,
        metadata={
            "name": "NumberOfCarriages",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    primary_depot: None | TextType = field(
        default=None,
        metadata={
            "name": "PrimaryDepot",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    seated_capacity: None | NumericType = field(
        default=None,
        metadata={
            "name": "SeatedCapacity",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    standing_capacity: None | NumberType = field(
        default=None,
        metadata={
            "name": "StandingCapacity",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    total_capacity: None | NumberType = field(
        default=None,
        metadata={
            "name": "TotalCapacity",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
