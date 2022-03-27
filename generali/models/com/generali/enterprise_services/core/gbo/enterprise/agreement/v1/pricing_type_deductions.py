from dataclasses import dataclass, field
from typing import List
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.pricing_deduction_type import PricingDeductionType

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"


@dataclass
class PricingTypeDeductions:
    class Meta:
        global_type = False

    deduction: List[PricingDeductionType] = field(
        default_factory=list,
        metadata={
            "name": "Deduction",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
