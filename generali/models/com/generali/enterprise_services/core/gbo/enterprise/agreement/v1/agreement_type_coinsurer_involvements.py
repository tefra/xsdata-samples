from __future__ import annotations

from dataclasses import dataclass, field

from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.coinsurer_involvement_type import (
    CoinsurerInvolvementType,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"
)


@dataclass
class AgreementTypeCoinsurerInvolvements:
    class Meta:
        global_type = False

    coinsurer: list[CoinsurerInvolvementType] = field(
        default_factory=list,
        metadata={
            "name": "Coinsurer",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
