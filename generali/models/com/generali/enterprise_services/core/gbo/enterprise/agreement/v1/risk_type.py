from dataclasses import dataclass, field
from typing import Optional
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.risk_element_involvement_type import RiskElementInvolvementType

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"


@dataclass
class RiskType:
    risk_element: Optional[RiskElementInvolvementType] = field(
        default=None,
        metadata={
            "name": "RiskElement",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        }
    )
