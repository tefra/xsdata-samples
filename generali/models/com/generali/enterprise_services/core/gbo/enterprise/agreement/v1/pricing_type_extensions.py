from dataclasses import dataclass, field
from typing import List
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.pricing_extension_type import (
    PricingExtensionType,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"
)


@dataclass
class PricingTypeExtensions:
    class Meta:
        global_type = False

    extension: List[PricingExtensionType] = field(
        default_factory=list,
        metadata={
            "name": "Extension",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
