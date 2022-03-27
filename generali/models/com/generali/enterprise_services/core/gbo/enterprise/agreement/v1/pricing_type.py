from dataclasses import dataclass, field
from typing import Optional
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.pricing_type_deductibles import PricingTypeDeductibles
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.pricing_type_deductions import PricingTypeDeductions
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.pricing_type_extensions import PricingTypeExtensions
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.pricing_type_layers import PricingTypeLayers
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.pricing_type_limits import PricingTypeLimits
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.pricing_type_pricing_amounts import PricingTypePricingAmounts

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"


@dataclass
class PricingType:
    involvement_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "InvolvementType",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    producing_country_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProducingCountryName",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    layers: Optional[PricingTypeLayers] = field(
        default=None,
        metadata={
            "name": "Layers",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    deductions: Optional[PricingTypeDeductions] = field(
        default=None,
        metadata={
            "name": "Deductions",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    extensions: Optional[PricingTypeExtensions] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    deductibles: Optional[PricingTypeDeductibles] = field(
        default=None,
        metadata={
            "name": "Deductibles",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    limits: Optional[PricingTypeLimits] = field(
        default=None,
        metadata={
            "name": "Limits",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    pricing_amounts: Optional[PricingTypePricingAmounts] = field(
        default=None,
        metadata={
            "name": "PricingAmounts",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
