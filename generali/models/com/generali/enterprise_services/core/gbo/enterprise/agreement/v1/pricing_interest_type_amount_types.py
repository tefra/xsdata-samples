from dataclasses import dataclass, field
from typing import List
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.pricing_interest_amount_type import (
    PricingInterestAmountType,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"
)


@dataclass
class PricingInterestTypeAmountTypes:
    class Meta:
        global_type = False

    amount_type: List[PricingInterestAmountType] = field(
        default_factory=list,
        metadata={
            "name": "AmountType",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
