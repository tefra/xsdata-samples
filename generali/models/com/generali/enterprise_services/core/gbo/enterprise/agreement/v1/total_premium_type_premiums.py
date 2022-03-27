from dataclasses import dataclass, field
from typing import List
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.premium_type import PremiumType

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"


@dataclass
class TotalPremiumTypePremiums:
    class Meta:
        global_type = False

    premium: List[PremiumType] = field(
        default_factory=list,
        metadata={
            "name": "Premium",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
