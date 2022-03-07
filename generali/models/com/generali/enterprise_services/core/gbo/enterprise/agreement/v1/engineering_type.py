from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.engineering_maintenance_type import EngineeringMaintenanceType

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"


@dataclass
class EngineeringType:
    signoff_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "SignoffDate",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    test_commission_days: Optional[int] = field(
        default=None,
        metadata={
            "name": "TestCommissionDays",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    maintenance_record: Optional[EngineeringMaintenanceType] = field(
        default=None,
        metadata={
            "name": "MaintenanceRecord",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
