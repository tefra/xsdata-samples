from dataclasses import dataclass, field
from typing import List
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.insurance_flow_type import InsuranceFlowType

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"


@dataclass
class CoverGbotypeInsuranceFlows:
    class Meta:
        global_type = False

    insurance_flow: List[InsuranceFlowType] = field(
        default_factory=list,
        metadata={
            "name": "InsuranceFlow",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "min_occurs": 1,
        }
    )
