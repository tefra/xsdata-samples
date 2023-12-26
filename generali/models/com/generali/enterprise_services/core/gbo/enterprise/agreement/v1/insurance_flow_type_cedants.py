from dataclasses import dataclass, field
from typing import List
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.cedant_involvement_type import (
    CedantInvolvementType,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"
)


@dataclass
class InsuranceFlowTypeCedants:
    class Meta:
        global_type = False

    cedant: List[CedantInvolvementType] = field(
        default_factory=list,
        metadata={
            "name": "Cedant",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
