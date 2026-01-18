from __future__ import annotations

from dataclasses import dataclass, field

from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.pricing_type_deductibles import (
    PricingTypeDeductibles,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.pricing_type_deductions import (
    PricingTypeDeductions,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.pricing_type_extensions import (
    PricingTypeExtensions,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.pricing_type_layers import (
    PricingTypeLayers,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.pricing_type_limits import (
    PricingTypeLimits,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.pricing_type_pricing_amounts import (
    PricingTypePricingAmounts,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"
)


@dataclass
class PricingType:
    involvement_type: str | None = field(
        default=None,
        metadata={
            "name": "InvolvementType",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    producing_country_name: str | None = field(
        default=None,
        metadata={
            "name": "ProducingCountryName",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    layers: PricingTypeLayers | None = field(
        default=None,
        metadata={
            "name": "Layers",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    deductions: PricingTypeDeductions | None = field(
        default=None,
        metadata={
            "name": "Deductions",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    extensions: PricingTypeExtensions | None = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    deductibles: PricingTypeDeductibles | None = field(
        default=None,
        metadata={
            "name": "Deductibles",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    limits: PricingTypeLimits | None = field(
        default=None,
        metadata={
            "name": "Limits",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    pricing_amounts: PricingTypePricingAmounts | None = field(
        default=None,
        metadata={
            "name": "PricingAmounts",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
