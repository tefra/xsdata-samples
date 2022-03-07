from dataclasses import dataclass, field
from typing import List, Optional
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.base_identified_component_type import BaseIdentifiedComponentType
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.pricing_interest_amount_type import PricingInterestAmountType

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"


@dataclass
class PricingInterestType(BaseIdentifiedComponentType):
    amount_types: Optional["PricingInterestType.AmountTypes"] = field(
        default=None,
        metadata={
            "name": "AmountTypes",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )

    @dataclass
    class AmountTypes:
        amount_type: List[PricingInterestAmountType] = field(
            default_factory=list,
            metadata={
                "name": "AmountType",
                "type": "Element",
                "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            }
        )
