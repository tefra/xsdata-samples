from dataclasses import dataclass, field
from typing import List

from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.pricing_interest_type import (
    PricingInterestType,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"
)


@dataclass
class PricingTypeLimits:
    class Meta:
        global_type = False

    limit: List[PricingInterestType] = field(
        default_factory=list,
        metadata={
            "name": "Limit",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
