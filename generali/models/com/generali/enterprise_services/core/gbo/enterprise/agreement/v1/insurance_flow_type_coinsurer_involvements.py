from dataclasses import dataclass, field
from typing import List

from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.coinsurer_involvement_type import (
    CoinsurerInvolvementType,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"
)


@dataclass
class InsuranceFlowTypeCoinsurerInvolvements:
    class Meta:
        global_type = False

    coinsurer: List[CoinsurerInvolvementType] = field(
        default_factory=list,
        metadata={
            "name": "Coinsurer",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
