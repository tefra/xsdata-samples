from dataclasses import dataclass, field
from typing import List

from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.maintenance_type import (
    MaintenanceType,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"
)


@dataclass
class EngineeringMaintenanceTypeYears:
    class Meta:
        global_type = False

    maintenance: List[MaintenanceType] = field(
        default_factory=list,
        metadata={
            "name": "Maintenance",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "min_occurs": 1,
        },
    )
