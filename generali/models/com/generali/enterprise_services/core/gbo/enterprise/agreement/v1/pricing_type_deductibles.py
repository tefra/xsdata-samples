from __future__ import annotations

from dataclasses import dataclass, field

from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.pricing_interest_type import (
    PricingInterestType,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"
)


@dataclass(kw_only=True)
class PricingTypeDeductibles:
    class Meta:
        global_type = False

    deductible: list[PricingInterestType] = field(
        default_factory=list,
        metadata={
            "name": "Deductible",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
