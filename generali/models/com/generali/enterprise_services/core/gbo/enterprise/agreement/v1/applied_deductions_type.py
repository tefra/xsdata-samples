from __future__ import annotations

from dataclasses import dataclass, field

from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.applied_deduction_type import (
    AppliedDeductionType,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"
)


@dataclass
class AppliedDeductionsType:
    applied_deduction: list[AppliedDeductionType] = field(
        default_factory=list,
        metadata={
            "name": "AppliedDeduction",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
