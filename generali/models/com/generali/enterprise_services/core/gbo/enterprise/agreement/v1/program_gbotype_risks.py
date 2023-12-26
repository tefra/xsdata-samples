from dataclasses import dataclass, field
from typing import List
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.risk_type import (
    RiskType,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"
)


@dataclass
class ProgramGbotypeRisks:
    class Meta:
        global_type = False

    risk: List[RiskType] = field(
        default_factory=list,
        metadata={
            "name": "Risk",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
