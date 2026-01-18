from __future__ import annotations

from dataclasses import dataclass, field

from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.pricing_extension_type import (
    PricingExtensionType,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"
)


@dataclass(kw_only=True)
class PricingTypeExtensions:
    class Meta:
        global_type = False

    extension: list[PricingExtensionType] = field(
        default_factory=list,
        metadata={
            "name": "Extension",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
