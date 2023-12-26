from dataclasses import dataclass
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.common.v1.aircraft_type import (
    AircraftType,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1"
)


@dataclass
class HelicopterType(AircraftType):
    pass
