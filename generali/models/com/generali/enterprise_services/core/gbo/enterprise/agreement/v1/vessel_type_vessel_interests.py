from dataclasses import dataclass, field
from typing import List
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.vessel_interest_type import VesselInterestType

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"


@dataclass
class VesselTypeVesselInterests:
    class Meta:
        global_type = False

    vessel_interest: List[VesselInterestType] = field(
        default_factory=list,
        metadata={
            "name": "VesselInterest",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
