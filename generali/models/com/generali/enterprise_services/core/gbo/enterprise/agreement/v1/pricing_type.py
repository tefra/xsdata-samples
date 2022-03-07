from dataclasses import dataclass, field
from typing import List, Optional
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.pricing_amount_type import PricingAmountType
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.pricing_deduction_type import PricingDeductionType
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.pricing_extension_type import PricingExtensionType
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.pricing_interest_type import PricingInterestType
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.pricing_layer_type import PricingLayerType

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
    layers: Optional["PricingType.Layers"] = field(
        default=None,
        metadata={
            "name": "Layers",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    deductions: Optional["PricingType.Deductions"] = field(
        default=None,
        metadata={
            "name": "Deductions",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    extensions: Optional["PricingType.Extensions"] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    deductibles: Optional["PricingType.Deductibles"] = field(
        default=None,
        metadata={
            "name": "Deductibles",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    limits: Optional["PricingType.Limits"] = field(
        default=None,
        metadata={
            "name": "Limits",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    pricing_amounts: Optional["PricingType.PricingAmounts"] = field(
        default=None,
        metadata={
            "name": "PricingAmounts",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )

    @dataclass
    class Layers:
        layer: List[PricingLayerType] = field(
            default_factory=list,
            metadata={
                "name": "Layer",
                "type": "Element",
                "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            }
        )

    @dataclass
    class Deductions:
        deduction: List[PricingDeductionType] = field(
            default_factory=list,
            metadata={
                "name": "Deduction",
                "type": "Element",
                "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            }
        )

    @dataclass
    class Extensions:
        extension: List[PricingExtensionType] = field(
            default_factory=list,
            metadata={
                "name": "Extension",
                "type": "Element",
                "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            }
        )

    @dataclass
    class Deductibles:
        deductible: List[PricingInterestType] = field(
            default_factory=list,
            metadata={
                "name": "Deductible",
                "type": "Element",
                "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            }
        )

    @dataclass
    class Limits:
        limit: List[PricingInterestType] = field(
            default_factory=list,
            metadata={
                "name": "Limit",
                "type": "Element",
                "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            }
        )

    @dataclass
    class PricingAmounts:
        pricing_amount: List[PricingAmountType] = field(
            default_factory=list,
            metadata={
                "name": "PricingAmount",
                "type": "Element",
                "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            }
        )
