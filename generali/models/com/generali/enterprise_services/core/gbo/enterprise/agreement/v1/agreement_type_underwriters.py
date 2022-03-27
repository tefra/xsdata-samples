from dataclasses import dataclass, field
from typing import List
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.underwriter_involvement import UnderwriterInvolvement

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"


@dataclass
class AgreementTypeUnderwriters:
    class Meta:
        global_type = False

    underwriter: List[UnderwriterInvolvement] = field(
        default_factory=list,
        metadata={
            "name": "Underwriter",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "min_occurs": 1,
        }
    )
