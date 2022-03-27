from dataclasses import dataclass, field
from typing import List
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.common.v1.premium_allocation_type import PremiumAllocationType

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"


@dataclass
class PremiumTypePremiumAllocations:
    class Meta:
        global_type = False

    premium_allocation: List[PremiumAllocationType] = field(
        default_factory=list,
        metadata={
            "name": "PremiumAllocation",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
