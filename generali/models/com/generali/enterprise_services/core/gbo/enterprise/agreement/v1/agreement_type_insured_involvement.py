from dataclasses import dataclass, field
from typing import List
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.insured_involvement import InsuredInvolvement

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"


@dataclass
class AgreementTypeInsuredInvolvement:
    class Meta:
        global_type = False

    insured: List[InsuredInvolvement] = field(
        default_factory=list,
        metadata={
            "name": "Insured",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
