from dataclasses import dataclass, field

from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.instalment_plans_type_instalment_plan import (
    InstalmentPlansTypeInstalmentPlan,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"
)


@dataclass
class InstalmentPlansType:
    instalment_plan: list[InstalmentPlansTypeInstalmentPlan] = field(
        default_factory=list,
        metadata={
            "name": "InstalmentPlan",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
