from dataclasses import dataclass, field
from typing import Optional

from generali.models.com.generali.enterprise_services.core.gbo.common.v1.base_identified_component_type import (
    BaseIdentifiedComponentType,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.pricing_interest_type_amount_types import (
    PricingInterestTypeAmountTypes,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"
)


@dataclass
class PricingInterestType(BaseIdentifiedComponentType):
    amount_types: Optional[PricingInterestTypeAmountTypes] = field(
        default=None,
        metadata={
            "name": "AmountTypes",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
