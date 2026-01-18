from __future__ import annotations

from dataclasses import dataclass, field

from generali.models.com.generali.enterprise_services.core.gbo.common.v1.base_identified_component_type import (
    BaseIdentifiedComponentType,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.pricing_interest_type_amount_types import (
    PricingInterestTypeAmountTypes,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"
)


@dataclass(kw_only=True)
class PricingInterestType(BaseIdentifiedComponentType):
    amount_types: None | PricingInterestTypeAmountTypes = field(
        default=None,
        metadata={
            "name": "AmountTypes",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
