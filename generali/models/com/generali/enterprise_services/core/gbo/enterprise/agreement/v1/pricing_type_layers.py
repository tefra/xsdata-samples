from dataclasses import dataclass, field
from typing import List
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.pricing_layer_type import PricingLayerType

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"


@dataclass
class PricingTypeLayers:
    class Meta:
        global_type = False

    layer: List[PricingLayerType] = field(
        default_factory=list,
        metadata={
            "name": "Layer",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
