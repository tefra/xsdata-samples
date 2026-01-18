from __future__ import annotations

from dataclasses import dataclass, field

from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.amount_type import (
    AmountType,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.common.v1.premium_basis_type_basis import (
    PremiumBasisTypeBasis,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1"
)


@dataclass(kw_only=True)
class PremiumBasisType:
    value: AmountType = field(
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
            "required": True,
        }
    )
    basis: PremiumBasisTypeBasis = field(
        metadata={
            "name": "Basis",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
            "required": True,
        }
    )
