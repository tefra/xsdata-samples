from __future__ import annotations

from dataclasses import dataclass, field

from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.pricing_amount_type import (
    PricingAmountType,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"
)


@dataclass(kw_only=True)
class PricingTypePricingAmounts:
    class Meta:
        global_type = False

    pricing_amount: list[PricingAmountType] = field(
        default_factory=list,
        metadata={
            "name": "PricingAmount",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
