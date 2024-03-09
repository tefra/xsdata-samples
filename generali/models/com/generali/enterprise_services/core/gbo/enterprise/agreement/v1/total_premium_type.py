from dataclasses import dataclass, field
from typing import Optional

from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.code_type import (
    CodeType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.numeric_type import (
    NumericType,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.instalment_plans_type import (
    InstalmentPlansType,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.total_premium_type_premiums import (
    TotalPremiumTypePremiums,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.warranty_enum import (
    WarrantyEnum,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"
)


@dataclass
class TotalPremiumType:
    warranty_applies_after_days: Optional[NumericType] = field(
        default=None,
        metadata={
            "name": "WarrantyAppliesAfterDays",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        },
    )
    ppwbasis: Optional[WarrantyEnum] = field(
        default=None,
        metadata={
            "name": "PPWBasis",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    instalment_plans: Optional[InstalmentPlansType] = field(
        default=None,
        metadata={
            "name": "InstalmentPlans",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    currency: Optional[CodeType] = field(
        default=None,
        metadata={
            "name": "Currency",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        },
    )
    premiums: Optional[TotalPremiumTypePremiums] = field(
        default=None,
        metadata={
            "name": "Premiums",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
