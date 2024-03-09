from dataclasses import dataclass, field
from typing import Optional

from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.numeric_type import (
    NumericType,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"
)


@dataclass
class PricingPremiumType:
    gross: Optional[NumericType] = field(
        default=None,
        metadata={
            "name": "Gross",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    actual: Optional[NumericType] = field(
        default=None,
        metadata={
            "name": "Actual",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    minimum_acceptable: Optional[NumericType] = field(
        default=None,
        metadata={
            "name": "MinimumAcceptable",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
