from dataclasses import dataclass, field
from typing import Optional

from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.amount_type import (
    AmountType,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1"
)


@dataclass
class PremiumAllocationType:
    country_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "CountryCode",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
            "required": True,
            "pattern": r"[A-Z][A-Z]",
        },
    )
    beginning_of_year: Optional[AmountType] = field(
        default=None,
        metadata={
            "name": "BeginningOfYear",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
            "required": True,
        },
    )
    beginning_of_year_local_share: Optional[AmountType] = field(
        default=None,
        metadata={
            "name": "BeginningOfYearLocalShare",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
            "required": True,
        },
    )
