from dataclasses import dataclass, field

from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.cedant_involvement_type import (
    CedantInvolvementType,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"
)


@dataclass
class CoverGbotypeCedants:
    class Meta:
        global_type = False

    cedant: list[CedantInvolvementType] = field(
        default_factory=list,
        metadata={
            "name": "Cedant",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
