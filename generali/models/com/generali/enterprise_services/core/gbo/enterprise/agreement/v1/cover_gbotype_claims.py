from dataclasses import dataclass, field
from typing import List

from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.claim_type import (
    ClaimType,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"
)


@dataclass
class CoverGbotypeClaims:
    class Meta:
        global_type = False

    claim: List[ClaimType] = field(
        default_factory=list,
        metadata={
            "name": "Claim",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
