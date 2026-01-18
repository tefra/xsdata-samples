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


@dataclass(kw_only=True)
class PricingType:
    involvement_type: None | str = field(
        default=None,
        metadata={
            "name": "InvolvementType",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    producing_country_name: None | str = field(
        default=None,
        metadata={
            "name": "ProducingCountryName",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    layers: None | PricingTypeLayers = field(
        default=None,
        metadata={
            "name": "Layers",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    deductions: None | PricingTypeDeductions = field(
        default=None,
        metadata={
            "name": "Deductions",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    extensions: None | PricingTypeExtensions = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    deductibles: None | PricingTypeDeductibles = field(
        default=None,
        metadata={
            "name": "Deductibles",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    limits: None | PricingTypeLimits = field(
        default=None,
        metadata={
            "name": "Limits",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    pricing_amounts: None | PricingTypePricingAmounts = field(
        default=None,
        metadata={
            "name": "PricingAmounts",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
