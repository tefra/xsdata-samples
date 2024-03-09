from dataclasses import dataclass, field
from typing import List

from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.premium_factor_type import (
    PremiumFactorType,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"
)


@dataclass
class ProgramGbotypePremiumFactors:
    class Meta:
        global_type = False

    premium_factor: List[PremiumFactorType] = field(
        default_factory=list,
        metadata={
            "name": "PremiumFactor",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
