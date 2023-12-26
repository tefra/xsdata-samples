from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"
)


@dataclass
class PricingPremiumType:
    gross: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Gross",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    actual: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Actual",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    minimum_acceptable: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MinimumAcceptable",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
