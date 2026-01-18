from __future__ import annotations

from dataclasses import dataclass, field

from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.reinsurer_involvement_type import (
    ReinsurerInvolvementType,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"
)


@dataclass(kw_only=True)
class InsuranceFlowTypeReinsurers:
    class Meta:
        global_type = False

    reinsurer: list[ReinsurerInvolvementType] = field(
        default_factory=list,
        metadata={
            "name": "Reinsurer",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "min_occurs": 1,
        },
    )
