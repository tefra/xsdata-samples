from dataclasses import dataclass, field
from typing import List
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.vessel_type import (
    VesselType,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"
)


@dataclass
class CoverGbotypeVessels:
    class Meta:
        global_type = False

    vessel: List[VesselType] = field(
        default_factory=list,
        metadata={
            "name": "Vessel",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
