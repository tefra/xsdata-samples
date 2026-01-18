from __future__ import annotations

from dataclasses import dataclass, field

from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.date_time_type import (
    DateTimeType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.number_type import (
    NumberType,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.engineering_maintenance_type import (
    EngineeringMaintenanceType,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"
)


@dataclass(kw_only=True)
class EngineeringType:
    signoff_date: None | DateTimeType = field(
        default=None,
        metadata={
            "name": "SignoffDate",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    test_commission_days: None | NumberType = field(
        default=None,
        metadata={
            "name": "TestCommissionDays",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    maintenance_record: None | EngineeringMaintenanceType = field(
        default=None,
        metadata={
            "name": "MaintenanceRecord",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
